# cv2 = opencv-python package, mediapipe = mediapipe package both added to the project
import cv2
import mediapipe as mp
import time

class FaceDetector():
    def __init__(self, minDetectionCon = 0.25):
        self.minDetectionCon = minDetectionCon
        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceDetection = mp.solutions.face_detection
        self.faceDetection = self.mpFaceDetection.FaceDetection(minDetectionCon)

    def findFaces(self, img, draw = True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)
        # print(self.results) # .faceDetection_landmarks
        bboxs = []
        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                       int(bboxC.width * iw), int(bboxC.height * ih)
                bboxs.append([id, bbox, detection.score])
                if draw:
                    img = self.betterDraw(img, bbox)
                    # cv2.rectangle(img, bbox, (255, 0, 150), 2)
                    cv2.putText(img, f'{int(detection.score[0]*100)}%', (bbox[0]+10, bbox[1]+30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 150), 2)
        return img, bboxs

    def betterDraw(self, img, bbox, l = 30, t = 5, rt = 1):
        x, y, w, h = bbox
        x1, y1 = x+w, y+h
        cv2.rectangle(img, bbox, (255, 0, 150), rt)
        # Top Left x,y
        cv2.line(img, (x, y), (x+l, y), (255, 0, 150), t)
        cv2.line(img, (x, y), (x, y+l), (255, 0, 150), t)
        # Top Right x1,y
        cv2.line(img, (x1, y), (x1-l, y), (255, 0, 150), t)
        cv2.line(img, (x1, y), (x1, y+l), (255, 0, 150), t)
        # Bottom left x,y1
        cv2.line(img, (x, y1), (x+l, y1), (255, 0, 150), t)
        cv2.line(img, (x, y1), (x, y1-l), (255, 0, 150), t)
        # Bottom Right x1,y1
        cv2.line(img, (x1, y1), (x1-l, y1), (255, 0, 150), t)
        cv2.line(img, (x1, y1), (x1, y1-l), (255, 0, 150), t)

        return img


def main():
    # cap = cv2.VideoCapture('PexelVideo/hiddenface.mp4')  # face video
    cap = cv2.VideoCapture('PexelVideo/multiface.mp4') # multi-face video
    # # cap = cv2.VideoCapture(0) # Camputer Camera
    pTime = 0
    detector = FaceDetector()

    while True:
        success, img = cap.read()
        img, bboxs = detector.findFaces(img)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (20, 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 150), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(5)

if __name__ == "__main__":
    main()