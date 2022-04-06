import cv2
import time
import imutils
from PedestrianDetector import Detector
# import PoseEstimationModule as pem


# cap = cv2.VideoCapture('Module Base/PoseEstimationProject/PexelsVideos/dancing.mp4') # dancing video
cap = cv2.VideoCapture('Module Base/PoseEstimationProject/PexelsVideos/lecture.mp4') # lecture video
# cap = cv2.VideoCapture(r'D:\GitHub\RoboticsLabProject\RoboticsLab\Module Base\PoseEstimationProject\PexelsVideos\walking.mp4') # walking video
# cap = cv2.VideoCapture('PedestriansPics/alone.jpg') # walking video
# cap = cv2.VideoCapture('PedestriansPics/hide1.jpg') # walking video
# cap = cv2.VideoCapture('PedestriansPics/multiple.jpg') # walking video
# cap = cv2.VideoCapture(0) # Camputer Camera

pTime = 0
###############Pedestrian Detector implement #################
while True:
    success, img = cap.read()
    img = imutils.resize(img,width=600)
    img = Detector(img)
    # imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)


    # cv2.imshow("Image", img)
    cv2.waitKey(1)
########################################################################

#############################Pose Detection implement###########################################
# img = detector = pem.poseDetector()

# while True:
#     success, img = cap.read()
#     detector.findPose(img)
#     lmList = detector.findPosition(img, draw = False)
#     if len(lmList)!=0:
#         print(lmList[14])
#         cv2.circle(img, (lmList[14][1], lmList[14][2]), 5, (255, 0, 150), cv2.FILLED)

#     cTime = time.time()
#     fps = 1/(cTime-pTime)
#     pTime = cTime

#     cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

#     cv2.imshow("Image", img)
#     cv2.waitKey(1)



    ################################################################################