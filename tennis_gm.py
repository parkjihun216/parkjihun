from pico2d import *


open_canvas()
background_image = load_image('court.png')
ball_image = load_image('Ball23_B.png')
hero_image = load_image('Hero.png')

ball_x, ball_y = 400, 300
ball_dx, ball_dy = 20, 10

hero_x, hero_y = 400, 50
hero_speed = 10

score = 0

left_key_down = False
right_key_down = False


start_time = get_time()


running = True
while running:
    clear_canvas()
    background_image.draw(get_canvas_width() // 2, get_canvas_height() // 2)


    ball_x += ball_dx
    ball_y += ball_dy
    if ball_x < 50 or ball_x > get_canvas_width() - 50:
        ball_dx = -ball_dx
    if ball_y < 50 or ball_y > get_canvas_height() - 50:
        ball_dy = -ball_dy
    ball_image.draw(ball_x, ball_y)


    if hero_x < 50:
        hero_x = 50
    if hero_x > get_canvas_width() - 50:
        hero_x = get_canvas_width() - 50
    hero_image.draw(hero_x, hero_y)


    if left_key_down:
        hero_x -= hero_speed
    if right_key_down:
        hero_x += hero_speed


    if ball_y <= 50 and (hero_x - 50 < ball_x < hero_x + 50):
        ball_dy = -ball_dy
        score += 1


    score_text = "Score: %d" % score



    current_time = get_time()
    elapsed_time = current_time - start_time


    if elapsed_time >= 180:
        running = False

    update_canvas()


    ev = get_events()
    for e in ev:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_LEFT:
                left_key_down = True
            elif e.key == SDLK_RIGHT:
                right_key_down = True
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                left_key_down = False
            elif e.key == SDLK_RIGHT:
                right_key_down = False

    delay(0.03)


close_canvas()
print("게임 종료, 점수:", score)