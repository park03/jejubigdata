import cv2 as cv
import numpy as np
from PIL import Image
import pygame

i = Image.open('rainbow.jpg')

width , height = i.size

print (width)

do = "sound1.mp3"
re = "sound2.mp3"
mi = "sound3.mp3"
pa = "sound4.mp3"
sol = "sound5.mp3"
ra = "sound6.mp3"
si = "sound7.mp3"


freq = 16000    # sampling rate, 44100(CD), 16000(Naver TTS), 24000(google TTS)
bitsize = -16   # signed 16 bit. support 8,-8,16,-16
channels = 1    # 1 is mono, 2 is stereo
buffer = 2048   # number of samples (experiment to get right sound)

pygame.mixer.init(freq, bitsize, channels, buffer)

def mouse_callback(event, x, y, flags, param):


    # 마우스 왼쪽 버튼 누를시 위치에 있는 픽셀값을 읽어와서 HSV로 변환합니다.
    if event == cv.EVENT_LBUTTONDOWN:
        #print(img_color[y, x])
        color = img_color[y, x]
        print (color)

        one_pixel = np.uint8([[color]])
        hsv = cv.cvtColor(one_pixel, cv.COLOR_BGR2HSV)
        hsv = hsv[0][0]

        if hsv[0] == 179 : 
            print ("red")
            pygame.mixer.music.load(do)
            pygame.mixer.music.play()

        elif hsv[0] == 12:
            print ("orange")
            pygame.mixer.music.load(re)
            pygame.mixer.music.play()

        elif hsv[0] == 29:
            print ("yellow")
            pygame.mixer.music.load(mi)
            pygame.mixer.music.play()

        elif hsv[0] == 69:
            print ("green")
            pygame.mixer.music.load(pa)
            pygame.mixer.music.play()

        elif hsv[0] == 99:
            print ("light blue")
            pygame.mixer.music.load(sol)
            pygame.mixer.music.play()

        elif hsv[0] == 118:
            print ("blue")
            pygame.mixer.music.load(ra)
            pygame.mixer.music.play()

        else:
            print("purple")
            pygame.mixer.music.load(si)
            pygame.mixer.music.play()
    

        print (hsv[0])



cv.namedWindow('img_color')
cv.setMouseCallback('img_color', mouse_callback)



while(True):
    img_color = cv.imread('rainbow.jpg')
    height, width = img_color.shape[:2]
    img_color = cv.resize(img_color, (width, height), interpolation=cv.INTER_AREA)

    cv.imshow('img_color', img_color)

    # ESC 키누르면 종료
    if cv.waitKey(1) & 0xFF == 27:
        break

cv.waitKey(0)
cv.destroyAllWindows()