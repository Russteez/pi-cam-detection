import cv2
import datetime
import imutils
import numpy as np
import n_folder
import time

protopath = "MobileNetSSD_deploy.prototxt"
modelpath = "MobileNetSSD_deploy.caffemodel"
detector = cv2.dnn.readNetFromCaffe(prototxt=protopath, caffeModel=modelpath)

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

def main():
    cap = cv2.VideoCapture(0)

    today = datetime.date.today()
    now = str(today)
    counter = 0

    while True:
        ret, frame = cap.read()
        frame = imutils.resize(frame, width=600)

        (H, W) = frame.shape[:2]

        blob = cv2.dnn.blobFromImage(frame, 0.007843, (W, H), 127.5)

        detector.setInput(blob)
        person_detections = detector.forward()

        for i in np.arange(0, person_detections.shape[2]):
            confidence = person_detections[0, 0, i, 2]
            if confidence > 0.5:
                idx = int(person_detections[0, 0, i, 1])
                fish = 1

                if CLASSES[idx] != "person":
                    continue

                person_box = person_detections[0, 0, i, 3:7] * np.array([W, H, W, H])
                (startX, startY, endX, endY) = person_box.astype("int")

                cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)


                cv2.imshow("Application", frame)
                k = cv2.waitKey(1)

                if fish == 1:
                    n_folder.folder()
                    img_name = "Pic{}.jpg".format(counter)
                    cv2.imwrite(f"{now}/{img_name}", frame)
                    print("screenshot has been taken")
                    counter += 1
                    time.sleep(5)

                else:
                    continue


cv2.destroyAllWindows()


main()
