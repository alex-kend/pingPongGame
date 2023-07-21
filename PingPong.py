import pygame


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ПингПонг")
clock = pygame.time.Clock()
bg = pygame.image.load("img/maxresdefault.jpg")
player_a = pygame.image.load("img/png-transparent-gray-graphic-design-metal-silver-skin-metal-texture-plate-signs-label-rectangle-plate-thumbnail.png").convert_alpha()
player_b = pygame.image.load("img/png-transparent-gray-graphic-design-metal-silver-skin-metal-texture-plate-signs-label-rectangle-plate-thumbnail.png").convert_alpha()
ball = pygame.Rect(400, 300, 30, 30)
label = pygame.font.Font(None, 48)

ball_sound = pygame.mixer.Sound("sounds/877427.mp3")
lose_sound = pygame.mixer.Sound("sounds/gameshow_02.mp3")
new_game_sound = pygame.mixer.Sound("sounds/countdown_loop_64s_minimal_01.mp3")

text_new_game = label.render(f"НОВАЯ ИГРА", True, (142, 212, 189))
text_new_game_rect = text_new_game.get_rect(topleft=(250, 230))

text_exit = label.render(f"ВЫХОД", True, (142, 212, 189))
text_exit_rect = text_exit.get_rect(topleft=(250, 300))

text_author = label.render(f"Автор - Кендюхов Александр", True, (158, 68, 68))

player_a_y = 300
player_a_x = 30
player_b_y = 300
player_b_x = 715


ball_x = 400
ball_y = 300


player_speed_x = 5
player_speed_y = 3
ball_speed_X = 7
ball_speed_Y = 9

score_1 = 0
score_2 = 0

game_run = True
running = True

while running:
    if game_run:
        keys = pygame.key.get_pressed()
        text = label.render(f"Игрок 1: {score_1}     Игрок 2: {score_2}", True, (44, 176, 172))

        screen.blit(bg, (0, 0))
        screen.blit(player_a, (player_a_x, player_a_y))
        screen.blit(player_b, (player_b_x, player_b_y))
        screen.blit(text, (230, 50))

        player_a_rect = player_a.get_rect(center=(player_a_x, player_a_y))
        player_b_rect = player_b.get_rect(center=(player_b_x, player_b_y))
        pygame.draw.rect(screen, (255, 255, 255), ball)
        ball.x -= ball_speed_X
        ball.y -= ball_speed_Y

        if ball.top <= 0 or ball.bottom >= 600:
            ball_speed_Y *= -1
        if ball.left <= 0:
            ball_speed_X *= -1
            lose_sound.play()
            score_2 += 1

        if ball.right >= 800:
            ball_speed_X *= -1
            lose_sound.play()
            score_1 += 1

        if score_2 == 5:
            winner = "Игрок 2"
            game_run = False

        if score_1 == 5:
            winner = "Игрок 1"
            game_run = False

        if ball.colliderect(player_a_rect):
            ball_speed_X *= -1
            ball_sound.play()

        if ball.colliderect(player_b_rect):
            ball_speed_X *= -1
            ball_sound.play()

        if keys[pygame.K_w]:
            player_a_y -= player_speed_x
        elif keys[pygame.K_s]:
            player_a_y += player_speed_x

        if keys[pygame.K_i]:
            player_b_y -= player_speed_x
        elif keys[pygame.K_k]:
            player_b_y += player_speed_x

        if player_a_y <= 0:
            player_a_y = 0
        elif player_a_y >= 500:
            player_a_y = 500

        if player_b_y <= 0:
            player_b_y = 0
        elif player_b_y >= 500:
            player_b_y = 500

    else:
        screen.blit(bg, (0, 0))
        lose_sound.stop()
        new_game_sound.play()
        text = label.render(f"{winner} выиграл!!!", True, (44, 176, 172))
        screen.blit(text, (230, 100))
        screen.blit(text_new_game, text_new_game_rect)
        screen.blit(text_exit, text_exit_rect)
        screen.blit(text_author, (300, 550))

        mouse = pygame.mouse.get_pos()
        if text_new_game_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            game_run = True
            score_1 = 0
            score_2 = 0
            ball = pygame.Rect(400, 300, 30, 30)
            new_game_sound.stop()
        elif text_exit_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            running = False
            pygame.quit()
            break

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(60)
