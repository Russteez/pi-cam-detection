import datetime
import cv2
import n_folder
import person_detection

def take_pic():
    # cam = cv2.VideoCapture(0)
    counter = 0
    today = datetime.date.today()
    now = str(today)

    while True:
        # ret, frame = cam.read()

        if not person_detection.ret:
            print("no frame detected")
            break

        cv2.imshow("Ready", person_detection.frame)
        k = cv2.waitKey(1)

        if k % 256 == 27:
            print("closing app")
            break

        elif k % 256 == 32:
            n_folder.folder()

            img_name = "Pic{}.jpg".format(counter)
            cv2.imwrite(f"{now}/{img_name}", person_detection.frame)
            print("screenshot has been taken")
            counter += 1

cv2.destroyAllWindows()

take_pic()