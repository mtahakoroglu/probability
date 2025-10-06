import cv2
import numpy as np

img1 = cv2.imread('uniform distribution 1.jpg')
img2 = cv2.imread('uniform distribution 2.jpg')
(h1,w1,c) = img1.shape # (height, width, channel)
(h2,w2,c) = img2.shape # (height, width, channel)
h = 0
if (h1 != h2):
    if (h1 > h2):
        h = h2
        img1 = cv2.resize(img1, (int(w2), int(h2)), cv2.INTER_AREA)
    else:
        h = h1
        img2 = cv2.resize(img2, (int(w1), int(h1)), cv2.INTER_AREA)
img1 = cv2.putText(img1, '-1-', (2150,150), 0, 5, (0,255,0), 19, 0)
img2 = cv2.putText(img2, '-2-', (2150,150), 0, 5, (0,255,0), 19, 0)
# NumPy ile ayrı resimleri birleştirelim - 1 x 2
stereo = np.zeros((h,2*img1.shape[1],c), np.uint8)
stereo[:,0:img1.shape[1],:] = img1
stereo[:,img1.shape[1]:img1.shape[1]+img2.shape[1],:] = img2
s = 0.2
rimg = cv2.resize(stereo, (int(s*stereo.shape[1]), int(s*stereo.shape[0])), interpolation=cv2.INTER_AREA)
# resimleri görüntüle
cv2.imshow('stereo image', rimg)
cv2.imwrite('stereo image.jpg', rimg, [cv2.IMWRITE_JPEG_QUALITY,100])
cv2.waitKey(0)
