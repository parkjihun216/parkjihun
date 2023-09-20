from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def render(x,y) :
     clear_canvas()
     grass.draw_now(400,30)
     character.draw_now(x,y)
     delay(0.01)

def run_circle() :
 print('Circle')
 cx = 400
 cy = 300
 r = 200

 for dig in range(0, 360, 5):
     x = cx + r*math.cos(dig / 360 * 2 * math.pi)
     y = cy + r*math.sin(dig / 360 * 2 * math.pi)
     render(x,y)
     

def run_ractangle() :
     print('Ractangle')

     for x in range (50,750,10) :
        render(x,90)

     for y in range (90,550,10) :
        render(750,y)

     for x in range (750,50,-10) :
        render(x,550)

     for y in range (550,90,-10) :
        render(50,y)


while True :

    run_circle()
    run_ractangle()

break

close_canvas()

