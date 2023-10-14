from pico2d import *

# 초기화
open_canvas()
background_image = load_image('court.png')
ball_image = load_image('Ball23_B.png')
hero_image = load_image('Hero.png')

ball_x, ball_y = 400, 300
ball_dx, ball_dy = 5, 5  # 공의 이동 속도

hero_x, hero_y = 400, 50
hero_speed = 10  # 패들의 이동 속도

score = 0

# 방향키 입력 변수
left_key_down = False
right_key_down = False

# 게임 루프
running = True
while running:
    clear_canvas()
    background_image.draw(get_canvas_width() // 2, get_canvas_height() // 2)

    # 테니스 공 이동 및 그리기
    ball_x += ball_dx
    ball_y += ball_dy
    if ball_x < 50 or ball_x > get_canvas_width() - 50:
        ball_dx = -ball_dx
    if ball_y < 50 or ball_y > get_canvas_height() - 50:
        ball_dy = -ball_dy
    ball_image.draw(ball_x, ball_y)

    # 패들 이동 및 그리기
    if hero_x < 50:
        hero_x = 50
    if hero_x > get_canvas_width() - 50:
        hero_x = get_canvas_width() - 50
    hero_image.draw(hero_x, hero_y)

    # 방향키 입력에 따른 패들 이동
    if left_key_down:
        hero_x -= hero_speed
    if right_key_down:
        hero_x += hero_speed

    # 충돌 검사
    if ball_y <= 50 and (hero_x - 50 < ball_x < hero_x + 50):
        ball_dy = -ball_dy
        score += 1

    # 스코어 표시
    score_text = "Score: %d" % score


    update_canvas()

    # 이벤트 처리
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

# 게임 종료
close_canvas()
print("게임 종료, 점수:", score)