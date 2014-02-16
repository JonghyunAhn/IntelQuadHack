import Image
import numpy as np
import pygame
import pygame.surfarray
import facial

import pygame.transform
from libardrone import libardrone

def main():

  #Constants
  SCREEN_HEIGHT, SCREEN_WIDTH = 360,720
  FPS = .1

  #Setting up Drone
  pygame.init()
  drone = libardrone.ARDrone(True)  #CHANGE THIS TO IMAGE_PROCCESSING
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  drone.reset()
  clock = pygame.time.Clock()
  running = True

  #Pygame Event Listener
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      elif event.type == pygame.KEYUP:
        drone.hover()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          drone.reset()
          running = False
        elif event.key == pygame.K_RETURN:
          print "takeoff"
          drone.takeoff()
        elif event.key == pygame.K_SPACE:
          print "land"
          drone.land()
        # emergency reset
        elif event.key == pygame.K_BACKSPACE:
          drone.reset()
        elif event.key == pygame.K_w:
          drone.move_forward()
        elif event.key == pygame.K_s:
          drone.move_backward()
        elif event.key == pygame.K_a:
          drone.move_left()
        elif event.key == pygame.K_d:
          drone.move_right()
        elif event.key == pygame.K_UP:
          drone.move_up()
        elif event.key == pygame.K_DOWN:
          drone.move_down()
        elif event.key == pygame.K_LEFT:
          drone.turn_left()
        elif event.key == pygame.K_RIGHT:
          drone.turn_right()

    try:
      pixelarray = drone.get_image()  #The image in pixels (RGB)
      #Image Piping If Found Person in Picture
      #result = findFaces(pixelarray)
      img = Image.fromarray(pixelarray,'RGB')
      #img2 = Image.fromarray(result,'RGB')
      img.save('./tmp/img.png')
      #img2.save('./tmp/img2.png')
      
      if pixelarray != None:
        #Pygame Gui Design
        surface = pygame.surfarray.make_surface(pixelarray)
        rotsurface = pygame.transform.rotate(surface, 270)
        screen.blit(rotsurface, (0, 0))
        hud_color = (255, 0, 0) if drone.navdata.get('drone_state', dict()).get('emergency_mask', 1) else (10, 10, 255)
        bat = drone.navdata.get(0, dict()).get('battery', 0)
        f = pygame.font.Font(None, 20)
        hud = f.render('Battery: %i%%' % bat, True, hud_color)
        screen.blit(hud, (10, 10))
    except:
      pass

    pygame.display.flip()
    clock.tick(FPS) 
    pygame.display.set_caption("FPS: %.2f" % clock.get_fps())

  print "Shutting down...",
  drone.halt()

if __name__=='__main__':
    main()
