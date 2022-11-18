import pygame
import random
pygame.init()
# COLORS
white = (255,255,255)
red = (255,0,0)
bleck = (0,255,0)
blue = (0,0,255)
screen_width = 900
screen_hight = 600
# Create Window
gameWindow = pygame.display.set_mode((screen_width,screen_hight))
# Game title
pygame.display.set_caption('Snakes Game')
pygame.display.update()
# Game Variable
font = pygame.font.SysFont(None,55)
clock = pygame.time.Clock()
# score in display

def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        text_screen("Welcome To Snakes Game",blue,200,230)
        text_screen(' Press Space Bar To Play',blue,200,300)
        text_screen('Developed By Shantonu Acharjee',red,160,500)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(30)

# Game Loop
def gameloop():
    e=[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300]
    f=0
    with open('hiscore.txt', "r") as f:
        hiscore = f.read()
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    valocity_x = 0
    valocity_y = 0
    snk_list = []
    snk_length = 1
    food_x = random.randint(40, screen_width - 40)
    food_y = random.randint(40, screen_hight - 40)
    score = 0
    init_valocity = 5
    snake_size = 10
    fps = 30
    game_level = 0

    while not exit_game:
        if score in e and f==0:
            f=1
            init_valocity +=2
        if game_over:
            with open('hiscore.txt', "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen('Game Over! Press Enter To Continue.',red,100,screen_hight/2.5)
            text_screen('Your Score is : '+str(score),blue,280,300)
            text_screen("Hiscore is : " + str(hiscore), bleck, 280, 350)
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        valocity_x = init_valocity
                        valocity_y = 0

                    if event.key == pygame.K_LEFT:
                        valocity_x = -init_valocity
                        valocity_y = 0

                    if event.key == pygame.K_UP:
                        valocity_y = -init_valocity
                        valocity_x = 0

                    if event.key == pygame.K_DOWN:
                        valocity_y = init_valocity
                        valocity_x = 0

            snake_x = snake_x + valocity_x
            snake_y = snake_y + valocity_y

            if abs(snake_x - food_x) < 7 and abs(snake_y - food_y) < 7:
                score += 1
                f=0
                #print("Score : ",score)
                a = score/10
                game_level=int(a)
                food_x = random.randint(40, screen_width - 40)
                food_y = random.randint(40, screen_hight - 40)
                snk_length +=3
                if score > int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            text_screen("Score : " + str(score), blue, 5, 5)
            text_screen("Level : " + str(game_level) , red, screen_width/2.5 , 5)
            text_screen("Hiscore : " + str(hiscore),blue,650,5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over=True
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_hight:
                game_over=True

            pygame.draw.rect(gameWindow,blue,[snake_x,snake_y,snake_size, snake_size])
            plot_snake(gameWindow,bleck,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()
gameloop()
