import cv2
import json
import time
import datetime

vid = "rtsp://admin:adm12345@192.168.24.136/ISAPI/Streaming/channels/101/preview"
cap = cv2.VideoCapture(vid)
win = "Chimney"
cv2.namedWindow(win, cv2.WINDOW_NORMAL)
cv2.resizeWindow(win, 1280, 768)
parent = "C:\\Users\\indra.romdoni\\Documents\\Aplikasi Python\\chimneysmoke\\dataImage\\"
tStart = int(time.time())
capInterval = 5
f = open('kotak.json', 'r')
r = json.load(f)
f.close
while True:
    ret, img = cap.read()
    crp = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    if not ret:
        cap = cv2.VideoCapture(vid)
    dt = datetime.datetime.fromtimestamp(int(time.time()))
    tCap = int(time.time())
    if tCap-tStart == capInterval:
        fb = cv2.imwrite("dckiln.jpg", crp)
        tStart = tCap
        print(f'{datetime.datetime.fromtimestamp(int(time.time()))} {fb}')
    cv2.imshow(win, crp)
    key = cv2.waitKey(3)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()