from pico2d import *

open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')

x=0
while(x<800):
    clear_canvas()
    grass.draw_now(400,30)
    character.draw_now(x,90)
    x=x+2
    delay(0.01)

y=0
while(y<530):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(798,90+y)
    y=y+2
    delay(0.01)


x=0
while(x<780):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(778-x,598)
    x=x+2
    delay(0.01)

y=0
while(y<500):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(0,580-y)
    y=y+2
    delay(0.01)

close_canvas()
    
