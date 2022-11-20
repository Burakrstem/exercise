#!/usr/bin/env python3
import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

#kopru kurulur
#dugum baslatilir
#kameradan gelen veriye abone olunur
#gelen veri kopru aracılıgıyla BGR formatina getirilir
#istenilen islemler yapilir
#dugumu calistirilabilir yap

class Kamera():
    def __init__(self):
        rospy.init_node("camera_node")
        self.bridge=CvBridge()
        rospy.Subscriber("camera/rgb/image_raw",Image,self.callbackCamera)

        self.loop_rate=rospy.Rate(1)
        rospy.spin()
    
    def callbackCamera(self,msg):
        img=self.bridge.imgmsg_to_cv2(msg,"bgr8")
        cv2.imshow("Robot kamerasi",img)
        cv2.waitKey(1)

x=Kamera()

