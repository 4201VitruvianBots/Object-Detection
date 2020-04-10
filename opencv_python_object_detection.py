import cv2
import numpy as np


def nothing(x):
    pass


cap = cv2.VideoCapture(0);

ret, frame1 = cap.read()
ret, frame2 = cap.read()
# tracking window will display a way to interact with values
cv2.namedWindow("Tracking")
# The 'L' Prefix means 'Lower' & the 'U' prefix means 'Upper' these upper and lower value limits determine in what
# range can a pixels' values can be 'H' is Hue. Hue is the pure color value of a pixel 'S' is saturation. Saturation
# is the intensity of the pixel's color 'V' is value. Value is the darkness of a pixel you can alter these filters to
# allow only certain things through the frame & onto the mask the mask the is put metaphorically on top of the frame
# and lets through the pixel underneath it. to test this out some more, just run this and alter the 'Tracking' window
# and monitor the 'mask' and 'res' windows in comparison to the 'frame' window to see how they are different and how
# they change with different track-bar values
cv2.createTrackbar('LH', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LS', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LV', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('UH', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('US', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('UV', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('activate', 'Tracking', 0, 1, nothing)

while cap.isOpened():

    # frame = cv2.imread('smarties.png')
    # _, frame = cap.read()

    hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos('LH', 'Tracking')
    l_s = cv2.getTrackbarPos('LS', 'Tracking')
    l_v = cv2.getTrackbarPos('LV', 'Tracking')
    u_h = cv2.getTrackbarPos('UH', 'Tracking')
    u_s = cv2.getTrackbarPos('US', 'Tracking')
    u_v = cv2.getTrackbarPos('UV', 'Tracking')
    if cv2.getTrackbarPos('LH', 'Tracking') - cv2.getTrackbarPos('UH', 'Tracking') >= 0:
        cv2.setTrackbarPos('LH', 'Tracking', cv2.getTrackbarPos('UH', 'Tracking') - 1)
        cv2.setTrackbarPos('UH', 'Tracking', cv2.getTrackbarPos('LH', 'Tracking') + 1)
    if cv2.getTrackbarPos('LS', 'Tracking') - cv2.getTrackbarPos('US', 'Tracking') >= 0:
        cv2.setTrackbarPos('LS', 'Tracking', cv2.getTrackbarPos('US', 'Tracking') - 1)
        cv2.setTrackbarPos('US', 'Tracking', cv2.getTrackbarPos('LS', 'Tracking') + 1)
    if cv2.getTrackbarPos('LV', 'Tracking') - cv2.getTrackbarPos('UV', 'Tracking') >= 0:
        cv2.setTrackbarPos('LV', 'Tracking', cv2.getTrackbarPos('UV', 'Tracking') - 1)
        cv2.setTrackbarPos('UV', 'Tracking', cv2.getTrackbarPos('LV', 'Tracking') + 1)

    onSwitch = cv2.getTrackbarPos('activate', 'Tracking')

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)
    kernel = np.ones((2, 2), np.uint8)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    res = cv2.bitwise_and(frame1, frame1, mask=opening)

    diff = cv2.absdiff(res, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # for contour in contours:
    #     (x, y, w, h) = cv2.boundingRect(contour)
    #
    #     if cv2.contourArea(contour) < 10 or cv2.contourArea(contour) > 1150:
    #         continue
    #     cv2.rectangle(res, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #     cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #     cv2.putText(res, '('+str(int(x+(w/2)))+', '+str(int(y+(h/2)))+')', (int(x+(w/2)), int(y+(h/2))), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
    #     cv2.putText(res, 'Status: {}'.format('movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    if onSwitch == 1:
        gray1 = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

        corners = cv2.goodFeaturesToTrack(gray1, 100, 0.1, 10)
        print(str(corners))
        # cv2.goodFeaturesToTrack()
        corners = np.int0(corners)

        for i in corners:
            x, y = i.ravel()
            pts = np.array([[x, y]], np.int32)
            pts = pts.reshape((-1, 1, 2))
            res = cv2.drawContours(res, pts, -1, (0, 255, 0), 3)
    cv2.imshow("frame", frame1)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    frame1 = frame2
    ret, frame2 = cap.read()

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
