import pygame as pygame
import os
import random

#align screen to center, always.
os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

window_size_length = 350
window_size_width = 350
screen = pygame.display.set_mode((window_size_width,window_size_length))

done = False

participant_rect_length = window_size_length / 7.5
participant_rect_width = window_size_width / 7.5

player_score = 0
ai_score = 0

participant_to_territory_ratio = 1.5

territory_rect_length = participant_rect_length * participant_to_territory_ratio
territory_rect_width = participant_rect_width * participant_to_territory_ratio

def get_AI_Choice():

     intChoice = random.randint(0,2)

     if intChoice == 0: return "RIGHT"

     if intChoice == 1: return "LEFT"

     if intChoice == 2: return "UP"
     
     # if player_choice == "UP": return "RIGHT"

     # if player_choice == "RIGHT": return "LEFT"

     # if player_choice == "LEFT": return "UP"

def place_center(object_width): return((window_size_width/2) - (object_width/2))
def place_down(object_length): return(window_size_length - object_length)
def place_up(object_width): return(0)
def place_left(object_width): return(0)
def place_right(object_width): return(window_size_width - object_width)

##locations in screen
# center = (window_size_width/2) - (participant_rect_width/2)
# down = window_size_length - participant_rect_length
# up = 0
# left = 0
# right = window_size_width - participant_rect_width

clock = pygame.time.Clock()

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 20)

black_color = (0,0,0)
white_color = (255,255,255)
blue_color = (0, 128, 255)
grey_color = (100, 100, 100)
orange_color = (255, 100, 0)

player_choice = "UP"
player_choice_text = myfont.render("ROCK", False, (0, 0, 0))

ai_choice = "UP"
ai_choice_text = myfont.render("ROCK", False, (0, 0, 0))

winner = "__DRAW"

line_width = 10

while not done:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
                done = True

     toPaint = False

     pressed = pygame.key.get_pressed()
        
     if pressed[pygame.K_UP]: 
          ai_choice = get_AI_Choice()
          player_choice = "UP"
          toPaint = True
             
        
     if pressed[pygame.K_LEFT]:
          ai_choice = get_AI_Choice()
          player_choice = "LEFT"
          toPaint = True 
             

     if pressed[pygame.K_RIGHT]:
          ai_choice = get_AI_Choice()
          player_choice = "RIGHT"
          toPaint = True 

     #reset screen
     screen.fill(white_color)

     #draw player
     pygame.draw.rect(screen, blue_color, pygame.Rect(place_center(participant_rect_length), place_down(participant_rect_width), participant_rect_length, participant_rect_width))
     pygame.draw.circle(screen,black_color,[int(window_size_width/2),int(window_size_length) - int(participant_rect_length/2)],int(window_size_width / 50),0)

     #draw ai
     pygame.draw.rect(screen, orange_color, pygame.Rect(place_center(participant_rect_length), place_up(participant_rect_width),  participant_rect_length, participant_rect_width))
     pygame.draw.circle(screen,black_color,[int(window_size_width/2),int(participant_rect_length/2)],int(window_size_width / 50),0)

     #draw player zone
     pygame.draw.rect(screen, blue_color, pygame.Rect(place_left(territory_rect_length), place_up(territory_rect_width),  territory_rect_length, territory_rect_width))
     pygame.draw.rect(screen, blue_color, pygame.Rect(place_right(territory_rect_length), place_down(territory_rect_width),  territory_rect_length, territory_rect_width))

     #draw ai zone
     pygame.draw.rect(screen, orange_color, pygame.Rect(place_right(territory_rect_length), place_up(territory_rect_width),  territory_rect_length, territory_rect_width))
     pygame.draw.rect(screen, orange_color, pygame.Rect(place_left(territory_rect_length), place_down(territory_rect_width),  territory_rect_length, territory_rect_width))     
     
     if toPaint :
          
          ##drawing ai choice
          if ai_choice == "UP": 
               ai_choice_text = myfont.render("ROCK", False, (0, 0, 0))
               pygame.draw.line(screen,black_color,[int(window_size_width/2) ,int(participant_rect_length/2)],[int(window_size_width/2),(window_size_length) - int(participant_rect_length/2)],line_width)
          
          if ai_choice == "LEFT":
               ai_choice_text = myfont.render("PAPER", False, (0, 0, 0))
               pygame.draw.line(screen,black_color,[0,int(participant_rect_length/2)],[int(window_size_width/2), int(participant_rect_length/2)],line_width)

          if ai_choice == "RIGHT":
               ai_choice_text = myfont.render("SCISSORS", False, (0, 0, 0))
               pygame.draw.line(screen,black_color,[int(window_size_width/2), int(participant_rect_length/2)],[window_size_width, int(participant_rect_length/2)],line_width)

               
               
          ##drawing player choice
          if player_choice == "UP": 
               player_choice_text = myfont.render("ROCK", False, (0, 0, 0))
               pygame.draw.line(screen,black_color,[int(window_size_width/2) ,int(participant_rect_length/2)],[int(window_size_width/2),(window_size_length) - int(participant_rect_length/2)],line_width)
          
          if player_choice == "LEFT":
               player_choice_text = myfont.render("PAPER", False, (0, 0, 0))
               pygame.draw.line(screen,black_color,[0,window_size_length - int(participant_rect_length/2)],[int(window_size_width/2),window_size_length - int(participant_rect_length/2)],line_width)

          if player_choice == "RIGHT":
               player_choice_text = myfont.render("SCISSORS", False, (0, 0, 0))
               pygame.draw.line(screen,black_color,[int(window_size_width/2),window_size_length - int(participant_rect_length/2)],[window_size_width,window_size_length - int(participant_rect_length/2)],line_width)


          ##Drawing winner initial in text
          if player_choice == "LEFT" and ai_choice == "LEFT":
               player_score = player_score + 1
               ai_score = ai_score + 1
               winner = "__DRAW"
          elif player_choice == "LEFT" and ai_choice == "RIGHT":
               player_score = player_score + 1
               ai_score = ai_score + 0
               winner = "__AI"
          elif player_choice == "LEFT" and ai_choice == "UP":
               player_score = player_score + 1
               ai_score = ai_score + 0
               winner = "__AI"
          elif player_choice == "RIGHT" and ai_choice == "LEFT":
               player_score = player_score + 0
               ai_score = ai_score + 1
               winner = "__PLAYER"
          elif player_choice == "RIGHT" and ai_choice == "RIGHT":
               player_score = player_score + 0
               ai_score = ai_score + 0
               winner = "__DRAW"
          elif player_choice == "RIGHT" and ai_choice == "UP":
               player_score = player_score + 0
               ai_score = ai_score + 1
               winner = "__PLAYER"
          elif player_choice == "UP" and ai_choice == "LEFT":
               player_score = player_score + 0
               ai_score = ai_score + 1
               winner = "__PLAYER"
          elif player_choice == "UP" and ai_choice == "RIGHT":
               player_score = player_score + 1
               ai_score = ai_score + 0
               winner = "__AI"
          elif player_choice == "UP" and ai_choice == "UP":
               player_score = player_score + 0
               ai_score = ai_score + 0
               winner = "__DRAW"
          else:
               player_score = player_score + 0
               ai_score = ai_score + 0
               winner = "__DRAW"
          
     ##drawing ai choice
     if ai_choice == "UP": 
          ai_choice_text = myfont.render("ROCK", False, (0, 0, 0))
          pygame.draw.line(screen,black_color,[int(window_size_width/2) ,int(participant_rect_length/2)],[int(window_size_width/2),(window_size_length) - int(participant_rect_length/2)],line_width)
          
     if ai_choice == "LEFT":
          ai_choice_text = myfont.render("PAPER", False, (0, 0, 0))
          pygame.draw.line(screen,black_color,[0,int(participant_rect_length/2)],[int(window_size_width/2), int(participant_rect_length/2)],line_width)

     if ai_choice == "RIGHT":
          ai_choice_text = myfont.render("SCISSORS", False, (0, 0, 0))
          pygame.draw.line(screen,black_color,[int(window_size_width/2), int(participant_rect_length/2)],[window_size_width, int(participant_rect_length/2)],line_width)

               
               
     ##drawing player choice
     if player_choice == "UP": 
          player_choice_text = myfont.render("ROCK", False, (0, 0, 0))
          pygame.draw.line(screen,black_color,[int(window_size_width/2) ,int(participant_rect_length/2)],[int(window_size_width/2),(window_size_length) - int(participant_rect_length/2)],line_width)
          
     if player_choice == "LEFT":
          player_choice_text = myfont.render("PAPER", False, (0, 0, 0))
          pygame.draw.line(screen,black_color,[0,window_size_length - int(participant_rect_length/2)],[int(window_size_width/2),window_size_length - int(participant_rect_length/2)],line_width)

     if player_choice == "RIGHT":
          player_choice_text = myfont.render("SCISSORS", False, (0, 0, 0))
          pygame.draw.line(screen,black_color,[int(window_size_width/2),window_size_length - int(participant_rect_length/2)],[window_size_width,window_size_length - int(participant_rect_length/2)],line_width)
               
     
     player_score_text = myfont.render(str(player_score), False, (0, 0, 0))
     ai_score_text = myfont.render(str(ai_score), False, (0, 0, 0))

     winner_text = myfont.render("WINNER", False, (0, 0, 0))
     draw_text = myfont.render("DRAW", False, (0, 0, 0))

     # screen.blit(ai_score_text,(window_size_width - 50,territory_rect_length))
     # screen.blit(player_score_text,(window_size_width - 50,window_size_length - territory_rect_length - 30))

     if winner == "__PLAYER":
          screen.blit(winner_text,(window_size_width - 100,territory_rect_length))
     elif winner == "__DRAW":
          screen.blit(draw_text,(window_size_width - 100,int(window_size_length/2)))
     else:
          screen.blit(winner_text,(window_size_width - 100,window_size_length - territory_rect_length - 30))

     screen.blit(ai_choice_text,(1,territory_rect_length))
     screen.blit(player_choice_text,(1,window_size_length - territory_rect_length - 30))
          
     pygame.display.flip()

     clock.tick(30)



# center = (window_size_width/2) - (participant_rect_width/2)
# down = window_size_length - participant_rect_length
# up = 0
# left = 0
# right = window_size_width - participant_rect_width