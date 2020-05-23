#比較明合成、二枚を比較して輝度の高いを重ねる
#
#

from PIL import Image
import numpy as np

#def read_img(img_name):
 #   img = Image.open(img_name)
  #  return img


#read_img('/home/tt/Pictures/IMGP4468.JPG')


# 元となる画像の読み込み
img1 = Image.open('/home/tt/Pictures/IMGP4468.JPG')
img2 = Image.open('/home/tt/Pictures/IMGP4496.JPG')
#オリジナル画像の幅と高さを取得
width1, height1 = img1.size
width2, height2 = img2.size

# オリジナル画像と同じサイズのImageオブジェクトを作成する
img1 = Image.new('RGB', (width1, height1))
img2 = Image.new('RGB', (width2, height2))

img1_pixels = []
for y in range(height1):
  for x in range(width1):
    # getpixel((x,y))で左からx番目,上からy番目のピクセルの色を取得し、img_pixelsに追加する
    img1_pixels.append(img1.getpixel((x,y)))

img2_pixels = []
for y in range(height2):
  for x in range(width2):
    # getpixel((x,y))で左からx番目,上からy番目のピクセルの色を取得し、img_pixelsに追加する
    img2_pixels.append(img2.getpixel((x,y)))
# あとで計算しやすいようにnumpyのarrayに変換しておく
img1_pixels = np.array(img2_pixels)

img1.show()
#img2.show()

for y in range(height1):
    for x in range(width1): 
      pixel1 = img1.getpixel(x, y)
      pixel2 = img2.getpixel(x, y)
