import numpy as np


def compute_intersection(set_1,set_2):
    '''计算两个集合之间的交集
    :param set_1: a array of dimensions (n1, 4), anchor表示成(xmin, ymin, xmax, ymax)
    :param set_2: a array of dimensions (n2, 4), anchor表示成(xmin, ymin, xmax, ymax)
    :return intersection: a array of shape (n1,n2)
    '''
    lower_bounds=np.maximum(set_1[:,:2].reshape(-1,1,2),set_2[:,:2].reshape(1,-1,2)) # (n1,n2,2)
    upper_bounds=np.minimum(set_1[:,2:].reshape(-1,1,2),set_2[:,2:].reshape(1,-1,2)) # (n1,n2,2)

    intersection=np.clip(upper_bounds-lower_bounds,a_min=0,a_max=None)  # (n1,n2,2)

    return intersection[:,:,0]*intersection[:,:,1]


def compute_iou(set_1,set_2):
    '''计算两个集合之间的IOU
    :param set_1: a array of dimensions (n1, 4), anchor表示成(xmin, ymin, xmax, ymax)
    :param set_2: a array of dimensions (n2, 4), anchor表示成(xmin, ymin, xmax, ymax)
    :return iou: a array of shape (n1,n2)
    '''
    intersection=compute_intersection(set_1,set_2) # (n1,n2)
    area_set_1=(set_1[:,2]-set_1[0])*(set_1[:,3]-set_1[:,1])   # (n1,)
    area_set_2 = (set_2[:, 2] - set_2[0]) * (set_2[:, 3] - set_2[:, 1]) # (n2,)

    union=area_set_1.reshape(-1,1)+area_set_2.reshape(1,-1)-intersection # (n1,n2)

    return intersection/union # (n1,n2)

#############  MAIN ####################3
def assign_anchor(anchors,gt_boxes,iou_threshold=0.5):
    '''
    为每个anchor 分配一个真实的边框,配对
    :param anchors:  待分配的anchor, shape:（na, 4）
    :param gt_boxes: 真实边界框(bounding box), shape:（nb, 4）
    :param iou_threshold: 预先设定的阈值
    :return:  assigned_idx: shape: (na, ), 每个anchor分配的真实gt_boxes对应的索引, 若未分配任何bb则为-1
    '''
    na=anchors.shape[0]
    nb=gt_boxes.shape[0]
    iou=compute_intersection(anchors,gt_boxes)
    assighed_idx=np.zeros(na)-1  # 初始化全为-1

    iou_cp=iou.copy()
    for j in range(nb):
        i=np.argmax(iou_cp[:,j])
        assighed_idx[i]=j
        iou_cp[i,:]=float('-inf')

    for i in np.where(assighed_idx==-1)[0]:
        j=np.argmax(iou[i,:])
        if iou[i][j]>iou_threshold:
            assighed_idx[i]=j

    return assighed_idx


def xy_to_cxcy(boxes):
    '''
    将(x_min, y_min, x_max, y_max)形式的anchor转换成(center_x, center_y, w, h)形式的
    :param boxes:  bounding boxes in boundary coordinates, a array of size (n_boxes, 4)
    :return: bounding boxes in center-size coordinates, a array of size (n_boxes, 4)
    '''
    return np.cat([(boxes[:,2:]+boxes[:,:2])/2,boxes[:,2:]-boxes[:,:2]],axis=1)


def multiAnchorTarget(anchors,labels):
    '''为每个anchor 标注偏移量和类别
    :param anchors: 输入的锚框, multiAnthorBoxGenerator, shape:  (1,anchors_num_,4)
    :param labels: 真实标签, shape为(bn, 每张图片最多的真实锚框数, 5)
    第二维中，如果给定图片没有这么多锚框, 可以先用-1填充空白, 最后一维中的元素为[类别标签, 四个坐标值]
    :return
        列表, [bbox_offset, bbox_mask, cls_labels]
        bbox_offset: 每个锚框的标注偏移量，形状为(bn，锚框总数*4)
        bbox_mask: 形状同bbox_offset, 每个锚框的掩码, 一一对应上面的偏移量, 负类锚框(背景)对应的掩码均为0, 正类锚框的掩码均为1
        cls_labels: 每个锚框的标注类别, 其中0表示为背景, 形状为(bn，锚框总数)
    '''
    bn=labels.shape[0]

    def multiBoxTargetOne(anc,lab,eps=1e-6):
        """
        multiAnchorTarget 辅助函数, 处理batch中的一个
        Args:
            anc: shape of (锚框总数, 4)
            lab: shape of (真实锚框数, 5), 5代表[类别标签, 四个坐标值]
            eps: 一个极小值, 防止log0
        Returns:
            offset: (锚框总数*4, )
            bbox_mask: (锚框总数*4, ), 0代表背景, 1代表非背景
            cls_labels: (锚框总数, 4), 0代表背景
        """
        an=anc.shape[0]
        assigned_idx=assign_anchor(anc,labels[:,1:])
        bbox_mask=np.repeat((assigned_idx>=0).float().reshape(-1,1),4,axis=-1)

        cls_labels=np.zeros(an,np.int)  # [锚框总数,]
        assigned_bb=np.zeros((an,4),np.float32) # [锚框总数,4]

        for i in range(an):
            bb_idx=assigned_idx[i]
            if bb_idx>=0: # 非背景
                cls_labels[i]=lab[bb_idx,0]+1 # 注意+1
                assigned_bb[i]=lab[bb_idx,1:]

        center_anc=xy_to_cxcy(anc)
        center_assigned_bb=xy_to_cxcy(assigned_bb)

        offset_xy=10.0*(center_assigned_bb[:,:2]-center_anc[:,:2])/center_anc[:,2:] # (锚框总数,2)
        offset_wh=5.0*(np.log(eps+center_assigned_bb[:,2:]/center_anc[:,2:]))      # (锚框总数,2)

        offset=np.concatenate((offset_xy,offset_wh),axis=-1)*bbox_mask     # (锚框总数,4)
        return offset.flatten(),bbox_mask.flatten(),cls_labels

    batch_offset=[]
    batch_mask=[]
    batch_cls_labels=[]
    for b in range(bn):
        offset,bbox_mask,cls_labels=multiBoxTargetOne(anchors[0,:,:],labels[b,:,:])
        batch_offset.append(offset)
        batch_mask.append(bbox_mask)
        batch_cls_labels.append(cls_labels)
    bbox_offset=np.stack(batch_offset)
    bbox_mask=np.stack(batch_mask)
    cls_labels=np.stack(batch_cls_labels)
    return bbox_offset,bbox_mask,cls_labels



if __name__ == '__main__':
    anchors=np.array([[0,0,1,1],[0.1,0.1,0.9,0.9],[0.1,0.5,0.4,0.6],[0.2,0.2,1.2,1.2]])
    gt_boxes=np.array([[0.1,0,0.9,1],[0,0.1,0.8,0.9]])
    print(assign_anchor(anchors,gt_boxes,0.7))



