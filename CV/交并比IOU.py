
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

if __name__ == '__main__':
    set_1=np.array([[0,0,1,1],[0.5,0.5,1.5,1.5]])
    set_2=np.array([[0.5,0.2,1.5,0.9],[2,2,3,3]])
    iou=compute_intersection(set_1,set_2)
    for u in iou:
        print(u)




