from djitellopy import tello
import KeyPress_Module as kp
import numpy as np
from time import sleep
import cv2
import math

# https://www.youtube.com/watch?v=LmEcyQnfpDA&t=1344s
# 이동속도를 설정하는 이유?
# 0.0 포인트에서 드론이 이동한다 하였을때, 드론이 초속몇cm를 이동하는지에 따라서
# 그리드에 좌표를 적어야 하기 때문이다.
# 회전이나 곡선이 없이 그냥 직진을 한다하면 그리드에서 인식되는것은 ㅡ ㅣ 이런식으로
# 작성이 되기때문이다.
# 제일좋은것은 알고리즘 위의 유투브 주소에 들어가서 보는것이 제일 좋다.
# Keyboard_Control 을 갖고와서 코드 작성



######## PARAMETERS ########### 매게변수 속도와 각속도

fSpeed = 117 / 10  # Forward Speed in cm/s   (15cm/s)
# 전진 스피드 기본값 설정 초당 센티미터터 117cm를 10초동안 얼마나 이동했냐?
# 아래보면 기본 설정이 15 로 되어있기 때문에 느린것이다. 즉 15cm를 10초동안
# 얼마나 이동했냐 가 그리드에 맵핑이 되는것이다.
aSpeed = 360 / 10  # Angular Speed Degrees/s  (50d/s)
# 각속도 360도가 회전하는것이므로, 360도를 10초동안 앵글을 튼다는이야기,
# 기본 각속도의 값은 50
interval = 0.25 # 실제간격은 0.25 (이것이 리스폰스? 드론과정볼르 주고받는?)

dInterval = fSpeed * interval # 디스턴스 인터벌은 전진속도에 설정한 간격을 곱한값

aInterval = aSpeed * interval # a인터벌은 속도에 간격을 곱한것,

#한단위 움직일때마다 거리와 각도가 입력된다
###############################################

x, y = 500, 500 #500,500의 좌표입니다. 1000,1000을 사용하기때문에 정 중앙입니다.
a = 0 # 이동을 했는데 좌표값을 매번 0 이라고 업데이트하면 좌표가 찍히지않는다,
# 그래서 아래보면 d=0 이라 해서 여기서 만듬
yaw = 0
kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
points = [(0,0), (0,0)]

def getKeyboardInput():
    # 키 포인트를 입력할때마다 각 값이 저장되게 함.

    lr, fb, ud, yv = 0, 0, 0, 0
    # lr = 왼쪽 오른쪽
    # fb = 드론의 앞뒤
    # ud = 드론의 상승 , 하강
    # yv = 드론의 각도
    # 키보드 컨트롤에서 보면, 오른쪽 앞 상승 오른쪽각틀기는 + 값으로 설정,
    # 키보드 컨트롤에서 보면, 왼쪽 뒤 하강 왼쪽각도 틀기는 - 값으로 설정이 되어서,
    # 아래의 값들을보면 - , +로 한설정을해서 이동이 용이하게 기능을 저장하였다.
    speed = 15 # 기본 스피드
    aspeed = 50
    global x, y, yaw, a
    d = 0
    # d로 저장한것은 좌표값을 받은값에서 더하기를 하기위해서
    if kp.getKey("LEFT"):
        lr = -speed
        d = dInterval
        a = -180

    elif kp.getKey("RIGHT"):
        lr = speed
        d = -dInterval
        a = 180

    if kp.getKey("UP"):
        fb = speed
        d = dInterval
        a = 270

    elif kp.getKey("DOWN"):
        fb = -speed
        d = -dInterval
        a = -90

    if kp.getKey("w"):
        ud = speed

    elif kp.getKey("s"):
        ud = -speed

    if kp.getKey("a"):
        yv = -aspeed
        yaw -= aInterval

    elif kp.getKey("d"):
        yv = aspeed
        yaw += aInterval

    if kp.getKey("q"): me.land(); sleep(3)

    if kp.getKey("e"): me.takeoff()

    sleep(interval)
    a += yaw # 각도는 +가 yaw 와같다 (오른쪽)
    x += int(d * math.cos(math.radians(a))) # x는 00에서 정수입력을 한거리 ,코사인
    y += int(d * math.sin(math.radians(a))) # 라디안을 사용할것이라 라디안으로 변경
    return [lr, fb, ud, yv, x, y]

def drawPoints(img, points):
    # 이미지에 그림을 그릴것인데, 포인트 아래설정,

    for point in points:
        cv2.circle(img, point, 5, (0, 0, 255), cv2.FILLED) # 원설정
        #img,point 좌표자리에 x , y 로 대신할수도 있다.
    cv2.circle(img, points[-1], 8, (0, 255,0), cv2.FILLED) # 원 설정
    cv2.putText(img,f'({(points[-1][0]-500)/100},{(points[-1][1]-500)/100})m',
                (points[-1][0] + 10, points[-1][1] + 30), cv2.FONT_HERSHEY_PLAIN, 1,
                (255, 0, 255), 1)

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = np.zeros((1000, 1000, 3), np.uint8) # 검은색 이미지생성, 정의
    # np.unit8 = 2^8 이므로 256과 같은값 0 to 255 에 값이 저장됨
    if (points[-1][0] != vals[4] or points[-1][1] != vals[5]):
        points.append((vals[4], vals[5]))

    drawPoints(img, points) # 그림을 그릴때마다 def drawpoints 불러옴
    cv2.imshow("Output", img)
    cv2.waitKey(1)