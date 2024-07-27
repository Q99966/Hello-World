
import cv2
import time
import math
from cvzone.HandTrackingModule import HandDetector  # 导入手部检测模块
 
#（1）视频捕获
cap = cv2.VideoCapture(0)  # 0代表电脑自带的摄像头
cap.set(3, 1280)  # 设置图像显示窗口的宽
cap.set(4, 720)   # 设置图像显示窗口的高
img3=cv2.imread('white.png')



 
pTime = 0  # 处理一帧图像的初始时间
 
changed = None # 初始状态不需要改变矩形颜色
 
color = (255,255,0)  # 可移动物体的默认颜色
 
medColor = (255,0,0)  # 中指和食指指尖中点的初始颜色
 
w, h = 150, 150   # 矩形宽和高
 
#（2）在频幕上构造物体的函数
def creObj(img, color, ptx, pty, w, h):
 
    # 透明矩形参数设置
    alphaReserve = 0.6  # 透明度
    BChannel, GChannel, RChannel = color  # 设置矩形颜色 
    yMin, yMax = pty, pty+h  # 矩形框的y坐标范围
    xMin, xMax = ptx, ptx+w  # 矩形框的y坐标范围
    
    # 绘制透明矩形
    img[yMin:yMax, xMin:xMax, 0] = img[yMin:yMax, xMin:xMax, 0] * alphaReserve + BChannel * (1 - alphaReserve)
    img[yMin:yMax, xMin:xMax, 1] = img[yMin:yMax, xMin:xMax, 1] * alphaReserve + GChannel * (1 - alphaReserve)
    img[yMin:yMax, xMin:xMax, 2] = img[yMin:yMax, xMin:xMax, 2] * alphaReserve + RChannel * (1 - alphaReserve)
 
    # 美化边界框
    line = 35 # 边缘线段长度
    cv2.rectangle(img, (ptx,pty), (ptx+w,pty+h), (255,0,255), 2) # 边框
    cv2.line(img, (ptx,pty), (ptx,pty+line), (0,255,255), 5)  # 左上角
    cv2.line(img, (ptx,pty), (ptx+line,pty), (0,255,255), 5) 
    cv2.line(img, (ptx+w,pty), (ptx+w-line,pty), (0,255,255), 5)  # 右上角
    cv2.line(img, (ptx+w,pty), (ptx+w,pty+line), (0,255,255), 5)   
    cv2.line(img, (ptx,pty+h), (ptx+line,pty+h), (0,255,255), 5)  # 左下角
    cv2.line(img, (ptx,pty+h), (ptx,pty+h-line), (0,255,255), 5) 
    cv2.line(img, (ptx+w,pty+h), (ptx+w-line,pty+h), (0,255,255), 5)  # 右下角
    cv2.line(img, (ptx+w,pty+h), (ptx+w,pty+h-line), (0,255,255), 5) 
    
    # 返回绘制后的图像
    return img
 
#（3）接收手部检测方法
detector = HandDetector(staticMode=False,maxHands=1,detectionCon=0.8,minTrackCon=0.5)   # 手部跟踪的最小置信度
 
#（4）在屏幕上创建初始矩形
ptList = []  # 存放每个矩形的左上角坐标
 
# 通过循环创建9个矩形，初始排列方式为3行3列
for i in range(3):  # 3行
    for j in range(4):  # 3列
    
        # 指定每个矩形的左上角坐标
        ptx = 200 * j + 100  # x坐标，起始位置为x=100，水平方向两个矩形间隔200个像素
        pty = 200 * i + 100  # y坐标，起始位置为y=100，每次换行下移200个像素
        
        # 将每个矩形的左上角坐标保存起来
        ptList.append([ptx, pty])
 
#（4）处理每一帧视频图像
while True:
        # 记录执行时间      
    cTime = time.time()
    
    # 返回是否读取成功和读取的图像
    success, img = cap.read()
    
    # 图像翻转，呈镜像关系
    img = cv2.flip(img, flipCode=1)  # 1代表水平翻转，0代表竖直翻转
    img2=cv2.resize(img3,(1280,720))
    
    
    
    #（5）手部关键点检测
    # 返回检测到的手部关键点信息，以及绘制关键点后的图像
    hands, img = detector.findHands(img, flipType=False)  # 由于上面翻转过图像了，这里就设置flipType不翻转   
    
    #（6）绘制可移动物体
    
    for index, pt in enumerate(ptList):  # 遍历所有矩形的左上角
        
        # 如果索引等于需要改变的矩形索引，就改变该矩形的颜色，否则就不变
        if index == changed:
            color = (0,0,255)
        else:
            color = (255,255,0)
        
        img2 = creObj(img2, color, pt[0], pt[1], w, h)
  
    #（7）计算食指和中指间的距离    
    if hands:  # 如果检测到手部信息才接下去执行
        
        # 将该只手的21个关键点坐标提取出来，hands是字典存放手信息
        lmList = hands[0]['lmList']
        
        # 获取食指指尖的坐标（像素坐标）
        finTip = lmList[8]  # 存放x和y坐标
        # 获取中指指尖坐标
        checkTip = lmList[12]
        mf=lmList[4]
        
        # 绘制食指和中指指尖的连线
        cv2.line(img2, finTip[:2], checkTip[:2], (255,0,0), 9)
        cv2.circle(img2, finTip[:2], 15, (255,0,0), cv2.FILLED) # 以食指尖为圆心画圆
        cv2.circle(img2, checkTip[:2], 15, (255,0,0), cv2.FILLED) # 以中指尖为圆心画圆
        # 以两指尖的中点为圆心画圆，如果距离小于规定值，颜色改变
        cv2.circle(img2, ((finTip[0]+checkTip[0])//2, (finTip[1]+checkTip[1])//2), 15, medColor, -1) 
        
        # 计算食指和中指间的距离
        distance = math.sqrt((finTip[0]-checkTip[0])**2 + (finTip[1]-checkTip[1])**2)
        
        # 如果距离小于80认为是选择物体，指尖指尖中点的颜色改变
        if distance < 80:
            medColor = (0,255,0)
        else:  # 如果大于80，就重置指尖中点颜色
            medColor = (255,0,0)
 
    #（8）判断食指指尖在哪个矩形的内部
        for index, pt in enumerate(ptList):  # 遍历所有矩形的左上角坐标
                
            ptx, pty = pt  # 提取每个矩形左上角的x和y坐标     
        
            # finTip保存食指指尖的x和y坐标
            if ptx<=finTip[0]<=ptx+w and pty<=finTip[1]<=pty+h:  # 如果食指指尖在某个矩形框内部
                
                # 记录下该矩形的索引
                changed = index
            
                # 如果食指和中指间的距离小于80，那就认为是移动物体
                if distance < 40:
                    # 让物体中心点位于指尖位置

                    
                    cx, cy = finTip[:2]
                    # 改变左上角坐标
                    pt = [cx-w//2, cy-h//2]
                    if math.sqrt((mf[0]-checkTip[0])**2 + (mf[1]-checkTip[1])**2) < 40:
                        del ptList[index]
                        break
                    
                    
                    elif ptList.count(pt) < 2:
                        
                        # 改变列表中的该索引对应的左上角坐标
                        ptList[index] = pt
                        
                        # 找到了就退出循环，代表一次只移动一个矩形
                        break
                    else:
                        del ptList[index]
                        break

                    

                    
                # 如果物体移动到了指定位置，那就松手
                else:  
                    # 重置矩形的颜色
                    color = (255,255,0)  
                    changed = None  
                    
    #（7）显示图像
      
    # 计算fps
    fps = 1/(cTime-pTime)
    # 重置起始时间
    pTime = cTime
    
    
    
    # 把fps显示在窗口上；img画板；取整的fps值；显示位置的坐标；设置字体；字体比例；颜色；厚度
    cv2.putText(img2, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)
    
    # 显示图像
    cv2.imshow('image', img2)  #窗口名，图像变量
    if cv2.waitKey(1) & 0xFF==27:  #每帧滞留1毫秒后消失
        break
 
# 释放视频资源
cap.release()
cv2.destroyAllWindows()