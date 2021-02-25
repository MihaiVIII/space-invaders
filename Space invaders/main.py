import pygame
import sys
import random
 
WIDTH = 1200
HEIGHT = 630
 
FPS = 60
 
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)

def create_laser():
    
    new_laser = laser_surface.get_rect(midbottom = (ship_react.centerx,600))
    
    return new_laser


def move_laser(lasers):
    for laser in lasers:
        laser.centery -= 5
    return lasers

def draw_lasers(lasers):
    for laser in lasers:
        screen.blit(laser_surface,laser)
       
def build_barricades(barricades):
    x = 200
    w = x
    y = 500
    for i in range (0,4):
        for j in range (0,5):
            for k in range(0,25):
                new_b = barricade_block.get_rect(center = (w,y))
                barricades.append(new_b)
                w = w + 4
            y = y + 4
            w = x
        x = x + 250
        y = 500
     
def draw_barricades(barricades):
    for barricade in barricades:
        screen.blit(barricade_block, barricade)

def check_coolision_lassers(barricades,lasers,aliens,score):
    for b in barricades:
        for l in lasers:
            if l.colliderect(b):
                lasers.remove(l)
                barricades.remove(b)
    i = 0
    for a in alien_list:
        for l in lasers:
            if aliens[i] != 0: 
                if l.colliderect(a):
                    lasers.remove(l)
                    aliens[i] = 0
                    score = score + 10
        i += 1
    return score
    
def generate_aliens():
    generate_a1()
    generate_a2()
    generate_a3()

def generate_a1():
    x = 200

    for i in range (0,10):    

        new_a1 = alien1_frames[0].get_rect(center = (x,50))
        alien_list.append(new_a1)
        new_a1 = alien1_frames[0].get_rect(center = (x,100))
        alien_list.append(new_a1)
        x = x + 50 


def generate_a2():
    x = 200

    for i in range (0,10):
       
        new_a2 = alien2_frames[0].get_rect(center = (x,150))
        alien_list.append(new_a2)
        new_a2 = alien2_frames[0].get_rect(center = (x,200))
        alien_list.append(new_a2)

        x = x + 50 

def generate_a3():
    x = 200

    for i in range (0,10):
       
        new_a3 = alien3_frames[0].get_rect(center = (x,250))
        alien_list.append(new_a3)
        x = x + 50 

def draw_alien(aliens,index):
    for a in range (0,20):
        if aliens[a] != 0:
            screen.blit(alien1_frames[index], aliens[a])
    for a in range (20,40):
        if aliens[a]!=0 :
            screen.blit(alien2_frames[index], aliens[a])
    for a in range (40,50):
        if aliens[a]!=0 :
            screen.blit(alien3_frames[index], aliens[a])

def move_alien(alienx,i):
    
    if i < 17 and i > 0:
        for a in alienx :
            if a != 0:
                a.centerx += 25
        i = i + 1
    else:
        if i < 0:
            for a in alienx:
                if a != 0:
                    a.centerx -= 25
            i = i + 1  
        else: 
            if i == 0 or i == 17:
                for a in alienx :
                    if a != 0:
                        a.centery += 25
                if i == 17:
                    i = -16
                else:
                    i = 1
      
           
    return i

def fire_alien(aliens):
    i = random.randint(0,9)
    if aliens[i+40] != 0:
        if random.randint(0,1) :
            new_laser = elaser_surface.get_rect(midbottom = (aliens[i + 40].centerx,aliens[i + 40].centery))
            return new_laser
        

    for j in (i, i + 10 , i + 20, i + 30):
        if (aliens[j] != 0 and aliens[j + 10] == 0):
            if random.randint(0,1) :
                    new_laser = elaser_surface.get_rect(midbottom = (aliens[j].centerx,aliens[j].centery))
                    return new_laser
    return False   
                

def move_elaser(lasers):
    for laser in lasers:
        laser.centery += 5
    return lasers

def draw_elaser(lasers):
    for laser in lasers:
        screen.blit(elaser_surface,laser)

def check_coolision_elassers(barricades,lasers, lives):
    for b in barricades:
        for l in lasers:
            if l.colliderect(b):
                lasers.remove(l)
                barricades.remove(b)
                
    for l in lasers:
        if ship_react.colliderect(l):
            lasers.remove(l)
            return lives - 1

    return lives

def victory_check(aliens):
    for alien in aliens:
        if alien != 0:
            return 0
    return 1


# Initialize imported pygame modules
pygame.init()
 
# Set the window's caption
pygame.display.set_caption("Space invaders")
 
clock = pygame.time.Clock()
 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
 
#variables
game_state = 0
lsrcount = 0
index = 0
move = 0
mv = 1
lsrcount2 = 0
lives = 3
score = 0
h = open("highscore","r")
highscore = int(h.read())
h.close()

g = open("highscore","w")

# Update the screen
pygame.display.flip()
#assets
#background  
background =  pygame.image.load('assets/game_backround.png').convert()
#title screen
title_surface = pygame.image.load('assets/titlescreen.png').convert()
#spaceship
ship = pygame.image.load('assets/ship.png').convert()
ship_react = ship.get_rect(center = (600,600))
#laser
laser_surface = pygame.image.load('assets/laser.png').convert()
laser_list =[]
#barricade
barricade_block = pygame.image.load('assets/bariccade_block.png').convert()
baricade_list =[]
#aliens
alien1_1 = pygame.image.load('assets/alien1.1.png').convert_alpha()
alien1_2 = pygame.image.load('assets/alien1.2.png').convert_alpha()
alien1_frames = [ alien1_1,alien1_2]

alien2_1 = pygame.image.load('assets/alien2.1.png').convert_alpha()
alien2_2 = pygame.image.load('assets/alien2.2.png').convert_alpha()
alien2_frames = [ alien2_1,alien2_2]

alien3_1 = pygame.image.load('assets/alien3.1.png').convert_alpha()
alien3_2 = pygame.image.load('assets/alien3.2.png').convert_alpha()
alien3_frames = [ alien3_1,alien3_2]
alien_list = []
#enemy laser
elaser_surface = pygame.image.load('assets/enemy_laser.png').convert()
elaser_list =[]

#Game over screen
gover_surface = pygame.image.load('assets/gameoverman.png').convert()
#Victory screen
victory_surface = pygame.image.load('assets/BATTLECRUISER OPERATIONAL.png').convert()
#font
game_font = pygame.font.Font('SF Distant Galaxy Alternate.ttf',20)
score_surface = game_font.render(f'Score: {int(score)}',True,(255,255,255))
score_rect = score_surface.get_rect(midleft = (15,450))
hscore_surface = game_font.render(f'Highscore: {int(highscore)}',True,(255,255,255))
hscore_rect = score_surface.get_rect(midleft = (15,500))
lives_surface = game_font.render(f'Lives: {int(lives)}',True,(255,255,255))
lives_rect = score_surface.get_rect(midleft = (15,550))

# Main loop
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # Check for Quit event
            g.write(str(highscore))
            g.close()
            pygame.quit()
            sys.exit()
            
    #title screen
    if game_state == 0:
        screen.blit(title_surface,(0,0))

    # Check for key presses and update paddles accordingly
    keys_pressed = pygame.key.get_pressed()
    if (keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]) and game_state == 1 and ship_react.centerx >= 0: 
        ship_react.centerx -= 2
       
    if (keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]) and game_state == 1 and ship_react.centerx <= 1200 : 
        ship_react.centerx += 2
    
    if keys_pressed[pygame.K_SPACE] and game_state == 1 and lsrcount >= 100:
        laser_list.append(create_laser())  
        lsrcount = 0
       
    if keys_pressed[pygame.K_SPACE] and game_state == 0:
        game_state = 1
        build_barricades(baricade_list)
        generate_aliens()
    
    #reset
    if keys_pressed[pygame.K_SPACE] and game_state == 3:
        game_state = 1
        baricade_list.clear()
        alien_list.clear()
        laser_list.clear()
        elaser_list.clear()
        build_barricades(baricade_list)
        generate_aliens()
        lsrcount = 0
        index = 0
        move = 0
        mv = 1
        lsrcount2 = 0
        lives = 3
        score = 0

    if keys_pressed[pygame.K_SPACE] and game_state == 4:
        game_state = 1
        baricade_list.clear()
        alien_list.clear()
        laser_list.clear()
        elaser_list.clear()
        build_barricades(baricade_list)
        generate_aliens()
        lsrcount = 0
        index = 0
        move = 0
        mv = 1
        lsrcount2 = 0
        lives = 3

    #When the game is running
    if game_state == 1:
        screen.blit(background, (0, 0))
        screen.blit(score_surface,score_rect)
        screen.blit(hscore_surface,hscore_rect)
        screen.blit(lives_surface,lives_rect)
        screen.blit(ship,ship_react)
        move_laser(laser_list)
        draw_lasers(laser_list)
        
        draw_barricades(baricade_list)
        score = check_coolision_lassers(baricade_list,laser_list,alien_list,score)
        score_surface = game_font.render(f'Score: {int(score)}',True,(255,255,255))
        lives_surface = game_font.render(f'Lives: {int(lives)}',True,(255,255,255))
        
        draw_alien(alien_list,index)
        ls = fire_alien(alien_list)
        lives = check_coolision_elassers(baricade_list,elaser_list, lives)

        if ls and lsrcount2 >= 80 : 
            elaser_list.append(ls)
            lsrcount2 = 0
        move_elaser(elaser_list)
        draw_elaser(elaser_list)

        move += 1
        if move == 100:
            index = (index + 1 )%2
            mv = move_alien(alien_list,mv)
            move = 0
        
        if lives == 0:
            game_state = 3
            if score > highscore:
                highscore = score
                hscore_surface = game_font.render(f'Highscore: {int(highscore)}',True,(255,255,255))

            
           
        lsrcount += 1
        lsrcount2 += 1

        victory = victory_check(alien_list)
        if victory == 1:
            game_state = 4
            if score > highscore:
                highscore = score
                hscore_surface = game_font.render(f'Highscore: {int(highscore)}',True,(255,255,255))

    
    #gameover_screen 
    if game_state == 3:
        screen.blit(gover_surface, (0, 0))
        screen.blit(score_surface,score_rect)
        screen.blit(hscore_surface,hscore_rect)
    #victory_screen
    if game_state == 4:
        screen.blit(victory_surface, (0, 0))
        screen.blit(score_surface,score_rect)
        screen.blit(hscore_surface,hscore_rect)

  
    pygame.display.update()
    clock.tick(120)


