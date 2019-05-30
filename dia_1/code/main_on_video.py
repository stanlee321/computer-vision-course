import numpy as np
import cv2


red_threshold = 55
green_threshold = 55
blue_threshold = 200

cap = cv2.VideoCapture('03. color selection-bNOWJ9wdmhk.mp4')

while True:
    ret, image = cap.read()
    print(image)

    if ret:
        color_select = np.copy(image)

        rgb_threshold = [red_threshold, green_threshold, blue_threshold]

        # Identify pixels below the threshold
        thresholds = (image[:,:,0] < rgb_threshold[0]) | (image[:,:,1] < rgb_threshold[1]) | (image[:,:,2] < rgb_threshold[2])
                    
        color_select[thresholds] = [0,0,0]

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        cv2.imshow('Cap', color_select)

cap.release()
cv2.destroyAllWindows()
