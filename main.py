import pygame
import player
import objects
import room
import menu

if __name__== '__main__':
  pygame.init()
  screen = pygame.display.set_mode((1024,512))
  pygame.display.set_caption('Witch')
  #pygame.display.toggle_fullscreen()
  screen.fill((255,255,255))
  mousepos = (0,0)
  mousebutton = 0
  room = room.room((14*64,8*64),('resources/tilemaps/grassmap','resources/tilemaps/fencemap'),(0,0), player.player((100,100),(32,128),(32,8),(0,120),3), {'up':pygame.K_UP, 'down':pygame.K_DOWN, 'left':pygame.K_LEFT, 'right':pygame.K_RIGHT}, [
	objects.obj((20,20),(20,64*5),None,(22,64*8),(0,0)),
	objects.obj((20+64*13,20),(0,0),None,(22,64*8),(0,0)),
	objects.obj((20,40),(64*14,20),None,(64*14,22),(0,0)),
	objects.tile_object((0,64*7),(64*14,64),'resources/tilemaps/fences_v',(64*14,22),(0,40))])

  font = pygame.font.Font('resources/PressStart2P-Regular.ttf',14)

  menu = menu.menu('resources/PressStart2P-Regular.ttf',14,'god is real',[menu.menu_item(),menu.menu_item()])

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
      menu.update(mousepos,mousebutton)
      menu.render(screen)
    screen.fill((255,0,255),(mousepos[0]-2,mousepos[1]-2,4,4))
    pygame.display.flip()

    room.update()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
        break
      elif event.type == pygame.MOUSEMOTION:
        mousepos = event.pos
      elif event.type == pygame.MOUSEBUTTONDOWN:
        mousebutton = event.button
      elif event.type == pygame.MOUSEBUTTONUP:
        if event.button == mousebutton:
          mousebutton = None
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
        
