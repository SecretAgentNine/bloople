import pygame
import player
import objects

if __name__== '__main__':
  pygame.init()
  screen = pygame.display.set_mode((1024,512))
  pygame.display.set_caption('Witch')
  #pygame.display.toggle_fullscreen()
  screen.fill((255,255,255))
  mousepos = (0,0)
  
  player = player.player((100,100),(32,128),(32,8),(0,120),3)
  obj = objects.obj((257,128),(20,80),(20,20),(0,60))
  renderlist = [player, obj]
  collidelist = [obj,]

  font = pygame.font.Font('resources/PressStart2P-Regular.ttf',14)

  debug = False
  
  running = True
  clock = pygame.time.Clock()

  while running:
    clock.tick(50)

    screen.fill((255,255,255))
    renderlist = sorted(renderlist, key = lambda i: i.pos[1]+i.size[1])
    for i in renderlist:
      i.render(screen, debug)
    if debug:
      screen.blit(font.render('FPS: '+str(int(clock.get_fps())),0,(0,0,0)),(4,4))
      screen.blit(font.render('Mouse Position: '+str(mousepos),0,(0,0,0)),(4,20))
    screen.fill((255,0,255),(mousepos[0]-2,mousepos[1]-2,4,4))
    pygame.display.flip()

    player.update(collidelist)

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
          player.move(event.key)
      elif event.type == pygame.KEYUP:
        player.stop(event.key)
        
