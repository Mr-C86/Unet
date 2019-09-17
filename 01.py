cap = cv2.VideoCapture('/home/yzs/video/1.wmv')
if (cap.isOpened() == False):
    print("Error opening video stream or file")
while (cap.isOpened()):
    ret, img = cap.read()
    if ret == True:
        detector = Detector()
        new_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        boxes = detector.detect(new_img)
        for box in boxes:
            x_min, y_min, x_max, y_max = int(box[1]), int(box[2]), int(box[3]), int(box[4])
            k1, k2, k3, k4, k5, k6, k7, k8, k9, k10 = int(box[5]), int(box[6]), int(box[7]), int(box[8]), int(
                box[9]), int(
                box[10]), int(box[11]), int(box[12]), int(box[13]), int(box[14])
            print(k1, k2, k3, k4, k5, k6, k7, k8, k9, k10)
            cv2.rectangle(img, (x_min, y_min), (x_max, y_max), color=(0, 255, 0), thickness=1)
            cv2.putText(img, "cls: {}".format(box[0]), (x_min, y_min), cv2.FONT_HERSHEY_PLAIN, 0.8,
                        color=(0, 255, 0))
            points_list = [(k1, k2), (k3, k4), (k5, k6), (k7, k8), (k9, k10)]
            for point in points_list:
                cv2.circle(img, point, 1, color=(0, 0, 255), thickness=1)
        cv2.imshow('Frame', img)

        if cv2.waitKey(84) & 0xFF == ord('q'):
            break

    else:
        break
cap.release()
cv2.destroyAllWindows()