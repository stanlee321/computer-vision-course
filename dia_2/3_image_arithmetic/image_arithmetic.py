import cv2
import numpy as np

# 500 x 250

img1 = cv2.imread('3D-Matplotlib-Example.png')
img1 = cv2.resize(img1, (500,250))
img2 = cv2.imread('monte-carlo-3d-graph.png')
img2 = cv2.resize(img2, (500,250))

add = img1+img2

# add = cv2.add(img1,img2)
# weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()