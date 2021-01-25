from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()

print(me.get_battery())# 배터리 출력

#me.move_forward(30) #앞으로 가 30cm
# me.send_rc_control(0,50,0,0) # 앞으로 50 속도로 ㄱ
# me.send_rc_control(0,-50,0,0) # 뒤로 50 속도로 ㄱ
# me.send_rc_control(50,0,0,0) # 오른쪽으로 50 속도로 가
# me.send_rc_control(-50,0,0,0) # 왼쪽쪽으로 50 속도로 가
# me.send_rc_control(0,0,0,50) # 오른쪽으로 각도 50도 틀어
# me.send_rc_control(0,0,0,-50) # 왼쪽으로 각도 50도 틀어

#me.send_rc_control(0,200,0,0)
#sleep(4)
#me.send_rc_control(0,-200,0,0)

