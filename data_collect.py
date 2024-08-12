import cv2

vid = "rtsp://admin:adm12345@192.168.24.136/ISAPI/Streaming/channels/101/preview"
cap = cv2.VideoCapture(vid)
win = "Chimney"
cv2.namedWindow(win)
cv2.resizeWindow(win, 1366, 768)
while True:
    ret, img = cap.read()
    if not ret:
        cap = cv2.VideoCapture(vid)
    cv2.imshow(win, img)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()