import numpy as np
import pygame as py

py.init()
screen = py.display.set_mode((400,400))
screen.fill((0,0,0))

def draw_dice(screen, x, y, number, size=100):
  py.draw.rect(screen, (0, 0, 0), (x,y,size,size))
  py.draw.rect(screen,(255,255,255), (x, y, size, size))
  dot_radius = 8
  center_x = x + size // 2
  center_y = y + size // 2
  margin = size //5

  positions = {
    1: [(center_x, center_y)],
    2: [(x + margin, y + margin), (x + size - margin, y + size - margin)],
    3: [(x + margin, y + margin), (center_x, center_y), (x + size - margin, y + size - margin)],
    4: [(x + margin, y + margin), (x + size - margin, y + margin), (x + margin, y + size - margin), (x + size - margin, y + size - margin)],
    5: [(x + margin, y + margin), (x + size - margin, y + margin), (center_x, center_y), (x + margin, y + size - margin), (x + size - margin, y + size - margin)],
    6: [(x + margin, y + margin), (x + margin, center_y), (x + margin, y + size - margin), (x + size - margin, y + margin), (x + size - margin, center_y), (x + size - margin, y + size - margin)]
  }

  for pos in positions.get(number, []):
    py.draw.circle(screen, (0, 0, 0), pos, dot_radius)

def roll_dice():
  rolls = np.random.randint(low=1, high=6, size=2)
  return rolls

running = True
rolls = roll_dice()
while running:
  for event in py.event.get():
    if event.type == py.QUIT:
      running = False
  screen.fill((0, 0, 0))
  draw_dice(screen, 50, 130, rolls[0])
  draw_dice(screen, 250, 130, rolls[1])
  py.display.flip()
py.quit()


