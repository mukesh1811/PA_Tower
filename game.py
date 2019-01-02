import pygame,os

#align screen to center, always.
os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
screen = pygame.display.set_mode((800, 800))
done = False
is_blue = True
x = 30
y = 30

alter_x = 800 - 30
alter_y = 800 - 30

clock = pygame.time.Clock()

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: 
            y -= 3

        if pressed[pygame.K_w]:
            alter_y -=3
        
        if pressed[pygame.K_DOWN]:
            y += 3

        if pressed[pygame.K_s]:
            alter_y +=3

        if pressed[pygame.K_LEFT]:
            x -= 3

        if pressed[pygame.K_a]:
            alter_x -=3

        if pressed[pygame.K_RIGHT]: 
            x += 3

        if pressed[pygame.K_d]:
            alter_x +=3

        textsurface = myfont.render('x = ' + str(x) + ' y = ' + str(y) + '\nalter_x = ' + str(alter_x) + ' alter_y = ' + str(alter_y), False, (255, 255, 255))
        
        screen.fill((0, 0, 0))
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)

        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

        pygame.draw.rect(screen, color, pygame.Rect(alter_x,alter_y, 60, 60))
        screen.blit(textsurface,(1,0))

        pygame.display.flip()
        clock.tick(120)