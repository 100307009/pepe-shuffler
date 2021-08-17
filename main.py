from PIL import Image
import random

def main(imgIn, imgOut, passwd):


  im = Image.open(imgIn)
  #split in RGBA channels
  rgba = list(im.split())


  #define random seed for repeatable results
  random.seed(passwd)
  
  #shuffle pixels
  for channel in rgba:
    pixShuffle(channel)

  im = Image.merge(im.mode, rgba)
  im.save(imgOut)
  print("conversion",imgIn,">",imgOut," DONE")


def pixShuffle(channel):

  #make array of all combinations of pixel positions
  XY=[]
  for x in list(range(channel.size[0])):
    for y in list(range(channel.size[1])):
      XY.append([x, y])
  
  #shuffles all pairs
  random.shuffle(XY)
  print(XY[0])
  #loads pixel map
  px = channel.load()

  #just swaps two pixels
  while(len(XY)>1):
    xya=XY.pop()
    xyb=XY.pop()
    a=px[xya[0], xya[1]]
    b=px[xyb[0], xyb[1]]
    px[xya[0], xya[1]] = b
    px[xyb[0], xyb[1]] = a

#encode
main("pepe.png", "out.png", "pepe")
#decode
main("out.png", "out2.png", "pepe")
