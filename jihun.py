from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
hand = load_image('hand_arrow.png')
character = load_image('run_animation.png')

a,b = TUK_WIDTH//2, TUK_HEIGHT//2
p1 = random.randint(400,1000)
frame = 0
for i in range(0,p1,10) :
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        hand.draw(p1, p1)
        character.clip_draw(frame * 100, 0, 100, 100, i, i )
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)