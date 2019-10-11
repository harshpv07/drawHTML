def capture():
    import cv2
    import time
    cap = cv2.VideoCapture(0)

    while(True):
        ret, frame = cap.read()
        cv2.imshow('frame',frame)
        time.sleep(0.1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        return frame