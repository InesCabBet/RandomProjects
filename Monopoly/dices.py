import numpy as np
import pygame as py

py.init()
screen = py.display.set_mode((800,600))
screen.fill((0,0,0))

def draw_dice(screen, x, y, number, size=100):
  py.draw.rect(screen, (0, 0, 0), (x,y,size,size))
  py.draw.rect(screen,(255,255,255), (x, y, size, size))
  do_radius = 8

def roll_dice():
  rolls = np.random.randint(low=1, high=6, size=2)
  return rolls

running = True
while running:
  for event in py.event.get():
    if event.type == py.QUIT:
      running = False
  screen.fill((0, 0, 0))
  py.display.flip()
py.quit()


