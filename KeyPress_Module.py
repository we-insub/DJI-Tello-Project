import pygame

def init():

    pygame.init()

    win = pygame.display.set_mode((400, 400)) # 사이즈지정

def getKey(keyName): # 키 지정 다른스크립트에서 호출할때 원하는키

    ans = False # 대답을 반환하기위해서 거짓으로 설정해둔다. 따라서 키를누르지않으면
    #반환값으로 키가 입력되지않으니 작동하지않음

    for eve in pygame.event.get(): pass
    #for문을 이용해서 불러온다.

    keyInput = pygame.key.get_pressed()
    # 키 입력을 받을 형식, 파이게임으로 작성을 해서 키를 입력 받을것이다.

    myKey = getattr(pygame, "K_{}".format(keyName))


    #print("K_{}".format(keyName))
    #"K_{REFT}" 형식 입니다.

    if keyInput[myKey]: # 내가 키를 눌렀다면 트루라면 출력

        ans = True # 키를눌렀다면 ans 는 트루이다.

    pygame.display.update() # 화면에 업데이트트

    return ans

def main():

    if getKey("LEFT"):

       #print("Left key pressed")
        pass

    if getKey("RIGHT"):

       #print("Right key Pressed")
        pass

if __name__ == "__main__":

    init()

    while True:

        main()

        # while 로 main 을 계속실행하고 돌면서 키를 누렀는지 확인하고
        # 그 값을 출력받는다.