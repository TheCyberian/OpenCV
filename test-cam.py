import cv2


capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
    if ret:
        cv2.imshow('frame', frame)
        cv2.imshow('gray', gray)

    if cv2.waitKey(20) == ord('q'):
        break


capture.release()
cv2.destroyAllWindows()
