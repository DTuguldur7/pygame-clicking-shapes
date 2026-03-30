import pygame
import button
import random


pygame.init()

#create display window
window_height = 500
window_width = 800

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Click The Shapes')

#load button images
start_img = pygame.image.load('D:\\Python\\Game\\files\\Drawing_start.png').convert_alpha()
easy_img = pygame.image.load('D:\\Python\\Game\\files\\Drawing_easy.png').convert_alpha()
medium_img = pygame.image.load('D:\\Python\\Game\\files\\Drawing_medium.png').convert_alpha()
hard_img = pygame.image.load('D:\\Python\\Game\\files\\Drawing_hard.png').convert_alpha()

#create button instances
start_button = button.Button(300, 150, start_img, 0.8)
easy_button = button.Button(320, 50, easy_img, 0.6)
medium_button = button.Button(320, 200, medium_img, 0.6)
hard_button = button.Button(320, 350, hard_img, 0.6)

#Target...
target_radius = 30
target_x = random.randint(target_radius, window_width - target_radius)
target_y = random.randint(target_radius, window_height - target_radius)
#Second target...
target_radius1 = 15
target1_x = random.randint(target_radius1, window_width - target_radius1)
target1_y = random.randint(target_radius1, window_height - target_radius1)
#Third target...
target_radius2=10
target2_x = random.randint(target_radius2, window_width - target_radius2)
target2_y = random.randint(target_radius2, window_height - target_radius2)
#Fourth target...
target_radius3 = 5
target2_x = random.randint(target_radius3, window_width - target_radius3)
target2_y = random.randint(target_radius3, window_height - target_radius3)

#variables
font=pygame.font.Font(None,60)
got_pressed=False
target_spawn_time = pygame.time.get_ticks()
target_time_limit = 1200  # 1.2 seconds
current_circle=random.randint(1, 2)
score=0
dt=0
mouse_pressed=False
clock=pygame.time.Clock()
click_sound=pygame.mixer.Sound('D:\\Python\\Game\\files\\Clicksound.wav')
click_sound.set_volume(1.0)
winning_sound = pygame.mixer.Sound('D:\\Python\\Game\\files\\winning_sound.wav')
winning_sound.set_volume(0.8)
losing_sound = pygame.mixer.Sound('D:\\Python\\Game\\files\\losing_sound.wav')
losing_sound.set_volume(0.8)
game_time_limit_hard = 30000
game_time_limit_medium = 60000
game_time_limit_easy = 100000
game_start_time = pygame.time.get_ticks()

#game loop
run = True
def You_won():
    pygame.display.set_caption('You won!')
    while True:
        screen.fill('violet')
        win_text = font.render("Хожсонд баяр хүргэе! Бэлгээ аваарай!", True, "black")
        HappyBDay = font.render("Төрсөн өдрийн мэнд хүргэе!", True, "black")
        screen.blit(win_text, (0, 150))
        screen.blit(HappyBDay, (150, 250))
        winning_sound.play()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                return
            
        
        pygame.display.update()    
        
def You_lost():
    pygame.display.set_caption('Try again?')
    while True:
        screen.fill('violet')
        lose_text = font.render("Ахин оролдоорой!", True, "black")
        help = font.render("Та чаднаа!!", True, "black")
        screen.blit(lose_text, (150, 150))
        screen.blit(help, (150, 250))
        losing_sound.play()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                return
            
        
        pygame.display.update() 
        pygame.time.delay(10000)
        pygame.quit()

def dif_easy():
    global game_start_time, score
    game_start_time = pygame.time.get_ticks()
    global score, target_x, target_y, target1_x, target1_y
    global current_circle, target_spawn_time, distance, distance1
    pygame.display.set_caption('Play')

    while True:

        screen.fill('pink')

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                return

            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()

                if event.button == 1 and current_circle == 1:
                    distance = ((mouse_pos[0] - target_x) ** 2 +
                        (mouse_pos[1] - target_y) ** 2) ** 0.5

                    if distance <= target_radius:
                        score += 1
                        click_sound.play()
                        target_x = random.randint(target_radius, window_width - target_radius)
                        target_y = random.randint(target_radius, window_height - target_radius)

                    current_circle = random.randint(1, 2)
                    target_spawn_time = pygame.time.get_ticks()
        
        # RIGHT CLICK (blue circle)
                if event.button == 3 and current_circle == 2:
                        distance1 = ((mouse_pos[0] - target1_x) ** 2 +
                            (mouse_pos[1] - target1_y) ** 2) ** 0.5

                        if distance1 <= target_radius1:
                            score += 2
                            click_sound.play()
                            target1_x = random.randint(target_radius1, window_width - target_radius1)
                            target1_y = random.randint(target_radius1, window_height - target_radius1)
                            current_circle = random.randint(1, 2)
                            target_spawn_time = pygame.time.get_ticks()

        current_time=pygame.time.get_ticks()
        if current_circle==2:
            if current_time - target_spawn_time>target_time_limit:
                score-=2
                target1_x = random.randint(target_radius1, window_width - target_radius)
                target1_y = random.randint(target_radius1, window_height - target_radius)
                target_spawn_time=pygame.time.get_ticks()

        if current_circle==1:
            if current_time - target_spawn_time>target_time_limit:
                score-=1
                target_x = random.randint(target_radius, window_width - target_radius)
                target_y = random.randint(target_radius, window_height - target_radius)
                target_spawn_time=pygame.time.get_ticks()

        if current_circle==1:
            pygame.draw.circle(screen, "red", (target_x, target_y), target_radius)
        else:
            pygame.draw.circle(screen, "blue", (target1_x, target1_y), target_radius1)

        score_text = font.render(f"Score: {score}", True, "black")
        screen.blit(score_text, (10, 10))
        time_left = (game_time_limit_easy - (current_time - game_start_time)) // 1000
        timer_text = font.render(f"Time: {time_left}", True, "black")
        screen.blit(timer_text, (550, 10))
        
        if score==50:
            You_won()
        elif score == -50:
            You_lost()
        elif time_left<=0 and score>=50:
            You_won()
        elif time_left<=0 and score<=50:
            You_lost()
        pygame.display.flip()

        dt = clock.tick(60) / 1000

def dif_medium():
    global game_start_time, score
    game_start_time = pygame.time.get_ticks()
    global score, target_x, target_y, target1_x, target1_y, target2_x, target2_y
    global current_circle, target_spawn_time, distance, distance1, distance2
    pygame.display.set_caption('Play')

    while True:

        screen.fill('pink')

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                return

            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()

                if event.button == 1 and current_circle == 1:
                    distance = ((mouse_pos[0] - target_x) ** 2 +
                        (mouse_pos[1] - target_y) ** 2) ** 0.5

                    if distance <= target_radius:
                        score += 1
                        click_sound.play()
                        target_x = random.randint(target_radius, window_width - target_radius)
                        target_y = random.randint(target_radius, window_height - target_radius)

                    current_circle = random.randint(1, 3)
                    target_spawn_time = pygame.time.get_ticks()
        
        # RIGHT CLICK (green circle)
                if event.button == 3 and current_circle == 3:
                    distance2 = ((mouse_pos[0] - target2_x) ** 2 +
                         (mouse_pos[1] - target2_y) ** 2) ** 0.5

                    if distance2 <= target_radius2:
                        score += 3
                        click_sound.play()
                        target2_x = random.randint(target_radius2, window_width - target_radius2)
                        target2_y = random.randint(target_radius2, window_height - target_radius2)

                    current_circle = random.randint(1, 3)
                    target_spawn_time = pygame.time.get_ticks()
        
        # RIGHT CLICK (blue circle)
                if event.button == 3 and current_circle == 2:
                        distance1 = ((mouse_pos[0] - target1_x) ** 2 +
                            (mouse_pos[1] - target1_y) ** 2) ** 0.5

                        if distance1 <= target_radius1:
                            score += 2
                            click_sound.play()
                            target1_x = random.randint(target_radius1, window_width - target_radius1)
                            target1_y = random.randint(target_radius1, window_height - target_radius1)
                            current_circle = random.randint(1, 3)
                            target_spawn_time = pygame.time.get_ticks()

        current_time=pygame.time.get_ticks()
        if current_circle==2:
            if current_time - target_spawn_time>target_time_limit:
                score-=2
                target1_x = random.randint(target_radius1, window_width - target_radius)
                target1_y = random.randint(target_radius1, window_height - target_radius)
                target_spawn_time=pygame.time.get_ticks()

        if current_circle==1:
            if current_time - target_spawn_time>target_time_limit:
                score-=1
                target_x = random.randint(target_radius, window_width - target_radius)
                target_y = random.randint(target_radius, window_height - target_radius)
                target_spawn_time=pygame.time.get_ticks()

        if current_circle==3:
            if current_time - target_spawn_time>target_time_limit:
                score-=3
                target2_x = random.randint(target_radius2, window_width - target_radius2)
                target2_y = random.randint(target_radius2, window_height - target_radius2)
                target_spawn_time=pygame.time.get_ticks()

        if current_circle==1:
            pygame.draw.circle(screen, "red", (target_x, target_y), target_radius)
        elif current_circle==3:
            pygame.draw.circle(screen, "green", (target2_x, target2_y), target_radius2)
        else:
            pygame.draw.circle(screen, "blue", (target1_x, target1_y), target_radius1)

        score_text = font.render(f"Score: {score}", True, "black")
        screen.blit(score_text, (10, 10))

        time_left = (game_time_limit_medium - (current_time - game_start_time)) // 1000

        timer_text = font.render(f"Time: {time_left}", True, "black")
        screen.blit(timer_text, (550, 10))
            
        if score==50:
            You_won()
        elif score == -50:
            You_lost()
        elif time_left<=0 and score>=50:
            You_won()
        elif time_left<=0 and score<=50:
            You_lost()
        pygame.display.flip()

        dt = clock.tick(60) / 1000

def dif_hard():
    global game_start_time, score
    game_start_time = pygame.time.get_ticks()
    global score, target_x, target_y, target1_x, target1_y, target2_x, target2_y, target3_x, target3_y
    global current_circle, target_spawn_time, distance, distance1, distance2, distance3
    pygame.display.set_caption('Play')

    while True:

        screen.fill('pink')

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                return

            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()

                if event.button == 1 and current_circle == 1:
                    distance = ((mouse_pos[0] - target_x) ** 2 +
                        (mouse_pos[1] - target_y) ** 2) ** 0.5

                    if distance <= target_radius:
                        score += 1
                        click_sound.play()
                        target_x = random.randint(target_radius, window_width - target_radius)
                        target_y = random.randint(target_radius, window_height - target_radius)

                    current_circle = random.randint(1, 4)
                    target_spawn_time = pygame.time.get_ticks()
        
        # RIGHT CLICK (green circle)
                if event.button == 3 and current_circle == 3:
                    distance2 = ((mouse_pos[0] - target2_x) ** 2 +
                         (mouse_pos[1] - target2_y) ** 2) ** 0.5

                    if distance2 <= target_radius2:
                        score += 3
                        click_sound.play()
                        target2_x = random.randint(target_radius2, window_width - target_radius2)
                        target2_y = random.randint(target_radius2, window_height - target_radius2)

                    current_circle = random.randint(1, 4)
                    target_spawn_time = pygame.time.get_ticks()
        
        # RIGHT CLICK (blue circle)
                if event.button == 3 and current_circle == 2:
                        distance1 = ((mouse_pos[0] - target1_x) ** 2 +
                            (mouse_pos[1] - target1_y) ** 2) ** 0.5

                        if distance1 <= target_radius1:
                            score += 2
                            click_sound.play()
                            target1_x = random.randint(target_radius1, window_width - target_radius1)
                            target1_y = random.randint(target_radius1, window_height - target_radius1)
                            current_circle = random.randint(1, 4)
                            target_spawn_time = pygame.time.get_ticks()

        #LEFT CLICK (Violet circle)
                if event.button == 1 and current_circle == 4:
                        distance3 = ((mouse_pos[0] - target_x) ** 2 +
                            (mouse_pos[1] - target_y) ** 2) ** 0.5

                        if distance3 <= target_radius3:
                            score += 4
                            click_sound.play()
                            target3_x = random.randint(target_radius3, window_width - target_radius3)
                            target3_y = random.randint(target_radius3, window_height - target_radius3)
                            current_circle = random.randint(1, 4)
                            target_spawn_time = pygame.time.get_ticks()

        current_time=pygame.time.get_ticks()
        if current_circle==2:
            if current_time - target_spawn_time>target_time_limit:
                score-=2
                target1_x = random.randint(target_radius1, window_width - target_radius)
                target1_y = random.randint(target_radius1, window_height - target_radius)
                target_spawn_time=pygame.time.get_ticks()

        if current_circle==1:
            if current_time - target_spawn_time>target_time_limit:
                score-=1
                target_x = random.randint(target_radius, window_width - target_radius)
                target_y = random.randint(target_radius, window_height - target_radius)
                target_spawn_time=pygame.time.get_ticks()

        if current_circle==3:
            if current_time - target_spawn_time>target_time_limit:
                score-=3
                target2_x = random.randint(target_radius2, window_width - target_radius2)
                target2_y = random.randint(target_radius2, window_height - target_radius2)
                target_spawn_time=pygame.time.get_ticks()
        
        if current_circle==4:
            if current_time - target_spawn_time>target_time_limit:
                score-=4
                target3_x = random.randint(target_radius3, window_width - target_radius3)
                target3_y = random.randint(target_radius3, window_height - target_radius3)
                target_spawn_time=pygame.time.get_ticks()

        if current_circle==1:
            pygame.draw.circle(screen, "red", (target_x, target_y), target_radius)
        elif current_circle==3:
            pygame.draw.circle(screen, "green", (target2_x, target2_y), target_radius2)
        elif current_circle==4:
            pygame.draw.circle(screen, "violet", (target_x, target_y), target_radius3)
        else:
            pygame.draw.circle(screen, "blue", (target1_x, target1_y), target_radius1)

        score_text = font.render(f"Score: {score}", True, "black")
        screen.blit(score_text, (10, 10))
        time_left = (game_time_limit_hard - (current_time - game_start_time)) // 1000
        timer_text = font.render(f"Time: {time_left}", True, "black")
        screen.blit(timer_text, (550, 10))

        if score==50:
            You_won()
        elif score == -50:
            You_lost()
        elif time_left<=0 and score>=50:
            You_won()
        elif time_left<=0 and score<=50:
            You_lost()
        pygame.display.flip()

        dt = clock.tick(60) / 1000

def start():
    pygame.display.set_caption('Choose difficulty')

    running = True
    while running:
        screen.fill('white')

        # Draw buttons
        easy_button.draw(screen)
        medium_button.draw(screen)
        hard_button.draw(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if easy_button.rect.collidepoint(mouse_pos):
                    dif_easy()
                elif medium_button.rect.collidepoint(mouse_pos):
                    dif_medium()
                elif hard_button.rect.collidepoint(mouse_pos):
                    dif_hard()

        pygame.display.update()
        clock.tick(60)

def menu():
     
     pygame.display.set_caption('Click the shapes')

     while True:

        screen.fill('white')
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
        
        if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if start_button.rect.collidepoint(mouse_pos):
                start()

        start_button.draw(screen)
        
                
        pygame.display.update()

menu()
pygame.quit()