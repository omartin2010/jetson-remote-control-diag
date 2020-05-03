import traceback
import cv2
import imagezmq

imageHub = imagezmq.ImageHub(
    open_port='tcp://192.168.32.57:5555',
    REQ_REP=False)
while True:
    try:
        (source, frame) = imageHub.recv_image()
        window_name = 'JetsonTX2Cam'
        cv2.namedWindow(window_name, flags=cv2.WINDOW_NORMAL)
        cv2.imshow(window_name, frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            cv2.destroyAllWindows()
            break
    except:
        print(f'problem : {traceback.print_exc()}')
        break
