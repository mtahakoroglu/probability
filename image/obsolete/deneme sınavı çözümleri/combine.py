import cv2
import numpy as np
n = 5 # number of images
img1 = cv2.imread('IMG_20221107_165406.jpg')
img2 = cv2.imread('IMG_20221107_170326.jpg')
img3 = cv2.imread('IMG_20221107_171526.jpg')
img4 = cv2.imread('IMG_20221107_172517.jpg')
img5 = cv2.imread('IMG_20221107_173140.jpg')
(h, w) = img1.shape[0:2]
combined = np.zeros((h, n*w, img1.shape[2]), np.uint8)
combined[:,:w,:] = img1
combined[:,w:2*w,:] = img2
combined[:,2*w:3*w,:] = img3
combined[:,3*w:4*w,:] = img4
combined[:,4*w:5*w,:] = img5
cv2.imwrite('combined.jpg', combined, [cv2.IMWRITE_JPEG_QUALITY, 25])