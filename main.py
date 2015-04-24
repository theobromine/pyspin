import sys
import pygame
from pygame.locals import *
import time
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BRIGHT    = ( 85, 255, 64)
a, b, c = 85
#def grad(background):
#    background = (a, b, c)
#    if a >= 85:
#        a +=
def play(angle, sound):
    if angle % 36 == 0:
        pygame.mixer.Sound.play(sound)
        print angle
    else:
        pass
     #print "sound is played"
def main():
    pygame.init()
    size = [1300, 850]
    flags =  DOUBLEBUF
    screen = pygame.display.set_mode(size, flags)
    screen.set_alpha(None)
    #screen = pygame.display.set_mode(size)
    pygame.mixer.init(frequency=22050, size=-8, channels=2, buffer=2048)
    tick = pygame.mixer.Sound("n.mp3")
    screen_rect = screen.get_rect()
    pygame.display.set_caption("Spinner!")
    clock = pygame.time.Clock()
    image_orig = pygame.image.load('Wheel.png')
    image = image_orig.copy()
    image_rect = image_orig.get_rect(center=screen_rect.center)
    pointer_orig = pygame.image.load('Pointer.png').convert_alpha()
    #pointer = pointer_orig.copy()
    pointer_rect = pointer_orig.get_rect(centerx=screen_rect.centerx, centery=-270)
    angle = 0
    change = 36
    done = False
    stopping = False
    while not done:
        clock.tick(120)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print('Forward')
                    change += 1
                elif event.key == pygame.K_SPACE:
                    print('Stopping')
                    stopping = not stopping
                elif event.key == pygame.K_d:
                    print change
                elif (event.type is KEYDOWN and event.key == K_f):
                    if screen.get_flags() & FULLSCREEN:
                        pygame.display.set_mode(size)
                    else:
                        pygame.display.set_mode(size, FULLSCREEN)
                elif event.key == pygame.K_ESCAPE:
                    print('escape!')
                    done = True
        if stopping == True and change > 0:
            change -= .5
            if change <=2:
                change == 0
        image = pygame.transform.rotate(image_orig, angle)
        image_rect = image.get_rect(center=image_rect.center)
        #screen.fill(BLACK)
        grad(BRIGHT)
        screen.fill(BRIGHT)
        play(angle, tick)
        screen.blit(image, image_rect)
        screen.blit(pointer_orig, pointer_rect)
        pygame.display.update(image_rect)
        angle += change


    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
