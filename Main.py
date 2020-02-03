import cv2
import numpy as np
import time

def capturarCor():
    vid = cv2.VideoCapture(0)
    file = "/home/jefersoneguido/repos/pisicultura_QualidadeDaAgua_cPythonEOpenCV/teste.png"

    while(1):
        _, image = vid.read()
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        # Seleciona as cores, fazer 
        lower_range = np.array([110,50,50])
        upper_range = np.array([130,255,255])

        mask = cv2.inRange(hsv,lower_range,upper_range)
        cv2.imshow('image_window_name',image)
        cv2.imshow('mask_window_namw',mask)
        cv2.waitKey(5)

    cv2.imwrite(file, image)
    cv2.destroyAllWindows()

 
if __name__ == '__main__':
    import sys
    #sys.exit(main(sys.argv))
    sys.exit(capturarCor())