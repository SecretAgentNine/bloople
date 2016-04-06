import pygame
import player
import objects
import room

if __name__== '__main__':
  pygame.init()
  screen = pygame.display.set_mode((1024,512))
  pygame.display.set_caption('Witch')
  #pygame.display.toggle_fullscreen()
  screen.fill((255,255,255))
  mousepos = (0,0)
  room = room.room((14*64,8*64),('resources/grassmap','resources/fencemap'),(0,0), player.player((100,100),(32,128),(32,8),(0,120),3), []) #objects.obj((257,128),(64,64),'resources/fence.png',(64,20),(0,44)),])

  font = pygame.font.Font('resources/PressStart2P-Regular.ttf',14)

  debug = False
  
  running = True
  clock = pygame.time.Clock()

  while running:
    clock.tick(50)

    screen.fill((100,255,150))
    room.render(screen,debug)
    if debug:
      screen.blit(font.render('FPS: '+str(int(clock.get_fps())),0,(64,64,64)),(4,4))
      screen.blit(font.render('Mouse Position: '+str(mousepos),0,(64,64,64)),(4,20))
    screen.fill((255,0,255),(mousepos[0]-2,mousepos[1]-2,4,4))
    pygame.display.flip()

    room.update()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
        break
      elif event.type == pygame.MOUSEMOTION:
        mousepos = event.pos
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          running = False
          break
        elif event.key == pygame.K_F3:
          debug = not debug
        else:
          room.handle_keydown(event.key)
      elif event.type == pygame.KEYUP:
        room.handle_keyup(event.key)
        
