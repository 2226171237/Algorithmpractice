import numpy as np
import matplotlib.pyplot as plt

def multiAnthorBoxGenerator(h,w,s,r):
    '''
    生成多个锚框
    :param h int: 图像的高
    :param w int: 图像的宽
    :param s list[float]: 锚框大小
    :param r list[float]: 锚框长宽比
    :return: anthors (1,anchors_num_,4)  anchor=[left_up_x,left_up_y,right_bottom_x,right_bottom_y]
    '''
    pairs=[]
    for i in range(len(r)):
        pairs.append([s[0],r[i]**0.5])
    for i in range(1,len(s)):
        pairs.append([s[i],r[0]**0.5])

    pairs=np.array(pairs)

    ss1=pairs[:,0]*pairs[:,1] # s*sqrt(r)   W
    ss2=pairs[:,0]/pairs[:,1] # s/sqrt(r)   H

    base_anchors=np.stack([-ss1,-ss2,ss1,ss2],axis=1)/2   # (len(s)+len(r)-1,4)
    # 归一化到了0-1之间的坐标，有助于映射
    shifts_x=np.arange(0,w)/w
    shifts_y=np.arange(0,h)/h
    shift_x,shift_y=np.meshgrid(shifts_x,shifts_y)
    shift_x=shift_x.flatten()
    shift_y=shift_y.flatten()
    shifts=np.stack([shift_x,shift_y,shift_x,shift_y],axis=1)  # (hw,4)

    anchors=shifts.reshape((-1,1,4))+base_anchors.reshape((1,-1,4))  # (hw,len(s)+len(r)-1,4)

    return anchors.reshape((1,-1,4)) # (1,anchors_num_,4)


def plot_boxes(img,boxes):
    plt.figure()
    H,W=img.shape[:2]
    plt.imshow(img)
    colors=['r','g','b','k','y','m','c']
    for i,box in enumerate(boxes):
        x,y=box[0]*W,box[1]*H
        h,w=(box[3]-box[1])*H,(box[2]-box[0])*W
        plt.gca().add_patch(plt.Rectangle(
            xy=(x,y),width=w,height=h,edgecolor=colors[i%7],
            fill=False
        ))
    plt.show()

if __name__ == '__main__':
    img=np.zeros((5,5,3))+120
    img=img.astype(np.uint8)
    anchors=multiAnthorBoxGenerator(5,5,[0.5,0.25,0.15],[0.5,0.2,0.1])
    anchors=anchors.reshape(5,5,-1,4)
    plot_boxes(img,anchors[2,2])

