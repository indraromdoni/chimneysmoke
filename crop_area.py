import cv2
import json

vid = "rtsp://admin:adm12345@192.168.24.136/ISAPI/Streaming/channels/101/preview"
cap = cv2.VideoCapture(vid)
win = "Chimney"
cv2.namedWindow(win, cv2.WINDOW_NORMAL)
cv2.resizeWindow(win, 1280, 768)
ret, img = cap.read()
r = cv2.selectROI(win, img)
print(r)
kotak = json.dumps(r)
f = open("kotak.json", "+w")
f.write(kotak)
f.close
imCrop = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
cv2.imshow("Cropped", imCrop)
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()