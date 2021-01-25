from djitellopy import tello
import cv2

me = tello.Tello()
me.connect()

print(me.get_battery())# 배터리 출력

me.stream_on()

while True:
    img = me.get_frame_read().fream #텔로드론에서 이미지 프레임불러옴, 원하는 이미지 크기 가능
    img = cv2.resize(img,(360,240)) # 사이즈 360 240 줄여서 프레임
    # 프레임 전송때문에 지연이 되는 경우가 있다. 경고문자가 뜨긴 하지만 큰 문제가없다 프레임이 줄어서 보이면 문제없음
    cv2.imshow("Image", img)
    cv2.waitKey(1)