import cv2
import numpy as np

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)

# Now, we can reference specific pixels, like so:
px = img[55,55]

# Next, we could actually change a pixel:
img[55,55] = [255,255,255]

# Then re-reference:
px = img[55,55]
print(px)

# It should be different now. Next, we can reference an ROI, 
# or Region of Image, like so:


px = img[100:150,100:150]
print(px)

# We can also modify the ROI, like this:
img[100:150,100:150] = [255,255,255]

# We can reference certain characteristics of our image:

print(img.shape)
print(img.size)
print(img.dtype)

# And we can perform operations, like:


watch_face = img[37:111,107:194]
img[0:74,0:87] = watch_face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()