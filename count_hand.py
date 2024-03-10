import cv2
import os
import time
import hand as htm

cap = cv2.VideoCapture(0)
pTime = 0
FolderPath = "Fingers"
lst = os.listdir(FolderPath)
lst_2 = []
for i in lst:
    image = cv2.imread(f"{FolderPath}/{i}")
    #print(f"{FolderPath}/{i}")
    lst_2.append(image)

detetor = htm.handDetector(detectionCon=1)

figerid = [4,8,12,16,20]
while True:
    ret, frame = cap.read()
    frame = detetor.findHands(frame)
    lmList = detetor.findPosition(frame,draw=False)
    #print(lmList)

    if len(lmList) != 0:
        finger = []
        
        # viet cho ngon cai
        if lmList[figerid[0]][1] < lmList[figerid[0]-1][1]:
            finger.append(1)
        else:
            finger.append(0)

        # 4 ngon dai
        for id in range(1,5):

            if lmList[figerid[id]][2] < lmList[figerid[id]-2][2]:
                finger.append(1)
            else:
                finger.append(0)
        #print(finger)
        count_finger = finger.count(1)

        print(count_finger)
        h, w, c = lst_2[count_finger -1].shape
        frame[0:h,0:w] = lst_2[count_finger-1]

        # Ve  hinh so ngon tay
        #cv2.rectangle(frame,(0,132),(200,400),(0,0,0),-1)
        #cv2.putText(frame, str(count_finger), (10,390), cv2.FONT_HERSHEY_DUPLEX,10,(255,0,0),3)

    # Output FPS
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    #cv2.putText(frame, f"FPS: {int(fps)}", (150,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)


    cv2.imshow("alo alo", frame)

    if cv2.waitKey(100) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 