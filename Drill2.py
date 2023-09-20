from pico2d import *
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

num = 0
pos = [400,90]
dir = [(1,0),(0,1),(-1,0),(0,-1)]
curDir=0
deg = 0
flag = False
while True:
    grass.draw(400,30)
    character.draw(pos[0],pos[1])
    if not flag:
        pos[0] += dir[curDir][0] * 10
        pos[1] += dir[curDir][1] * 10
        update_canvas()
        check_pos = [pos[0] + 42 * dir[curDir][0],pos[1] + 92 * dir[curDir][1]]
        if check_pos[0] >= 800 and curDir == 0:
            curDir = 1
        elif check_pos[1] >= 600 and curDir == 1:
            curDir = 2
        elif check_pos[0] <= 0 and curDir == 2:
            curDir = 3
        elif check_pos[1] <=0 and curDir == 3:
            curDir = 0
            num = (num + 1) % 2
    if num % 2 == 1 and curDir == 0 and check_pos[0] <= 410 and check_pos[0] >= 390:
        flag = True
    if flag :
        pos[0] = math.cos(deg)*200 + 400
        pos[1] = math.sin(deg)*200 + 300
        deg += 0.1
    if deg >= math.pi * 2:
        deg = 0
        flag = False
        pos[0] = 400
        pos[1] = 90
        num = (num + 1) % 2
    delay(0.01)
    update_canvas()
    clear_canvas()

close_canvas()