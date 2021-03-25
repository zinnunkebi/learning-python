import cv2

img_compare01 = cv2.imread('./image/compare01.png')
img_compare02 = cv2.imread('./image/compare02.png')
img_compare03 = cv2.imread('./image/compare03.png')
img_compare04 = cv2.imread('./image/compare04.png')
img_compare05 = cv2.imread('./image/compare05.png')
img_compare06 = cv2.imread('./image/compare06.png')
img_compare07 = cv2.imread('./image/compare07.png')

histograms = [ cv2.calcHist([img_compare01], [0], None, [256], [0, 256])
              ,cv2.calcHist([img_compare02], [0], None, [256], [0, 256])
              ,cv2.calcHist([img_compare03], [0], None, [256], [0, 256])
              ,cv2.calcHist([img_compare04], [0], None, [256], [0, 256])
              ,cv2.calcHist([img_compare05], [0], None, [256], [0, 256])
              ,cv2.calcHist([img_compare06], [0], None, [256], [0, 256])
              ,cv2.calcHist([img_compare07], [0], None, [256], [0, 256])
             ]

hist_cnt=len(histograms)

for i in range(hist_cnt):
    for j in range(hist_cnt):
        ret = cv2.compareHist(histograms[i], histograms[j], 0)
        print('compare [compare0' + str(i+1) + '.png:compare0' + str(j+1) + '.png] =' ,ret)
