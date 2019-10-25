# Pygame code, assignment for creating a game where user has to avoid coloured balls by moving his cursor on a window.
# Finished 2018-05-13, Misha Bagrianski
# Teacher: Mr. Radulovic, ICS201

import pygame
import random
import math

w = 800     # window width
l = 600     # window length
x = []      # x-vals list (positional)
y = []      # y-vals list (positional)
x_speed = []        # x speeds list (velocity)
y_speed = []        # y speeds list (velocity)
radius = []         # radius list
count = 0

black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
blue = [0, 0, 255]
green = [0, 255, 0]
cyan = [0, 255 ,255]
magenta = [255, 255, 0]
yellow = [255, 0, 255]

pygame.init() # initialize the graphics module


font = pygame.font.SysFont("Monospace", 25)
label_1 = font.render("Game Over", 1, white)



colour_selection = [red, blue, green, cyan, magenta, yellow]    # colour options to choose from, list
colour = []     # list that holds each circle's colour

state = True        # initial state, see comment @ lines 100-101
num = 2
pos = 0
seconds = 0

def lose():     # function for losing operations, when player loses the game
    for i in range(0, num):
        x_speed[i] = 0
        y_speed[i] = 0
        window.blit(label_1, (100, 100))
        window.blit(label_2, (100, 200))
        state = False
        return state

def setup(number):      # function that sets up balls, 'number' is a parameter that controls the number of balls spawned
    for i in range(0, number):
        radius.append(random.randint(5, 20))        #random radius for ball[i]
        x_speed.append(random.randint(-5, 5))
        y_speed.append(random.randint(-5, 5))
        while x_speed[i] == 0 and y_speed[i] == 0:    # get rid of possible situations where ball remains stationary
            x_speed[i] == random.randint(-5, 5)     # keep generating random integers until the ball is moving
            y_speed[i] == random.randint(-5, 5)
        x.append(random.randint(radius[i], w - radius[i]))   # generate starting positions
        y.append(random.randint(radius[i], l - radius[i]))
        colour.append(random.choice(colour_selection))      #random colour for ball[i]

def draw(num):      # function for drawing and adding 'speed' to the circles
    for i in range (0, num):
        pygame.draw.circle(window, colour[i], (x[i], y[i]), radius[i])

        if x[i] + radius[i] > w or x[i] < radius[i]:
            x_speed[i] = -x_speed[i]
        x[i] += x_speed[i]

        if y[i] + radius[i] > l or y[i] < radius[i]:
            y_speed[i] = -y_speed[i]
        y[i] += y_speed[i]

def ball_collision(num):       # function for collision detection and handling
    for i in range(0, num):
        for j in range(i + 1, num):     # for each element [i] in list, all following elements are checked for
                                        # collision with element [i]
            distance = math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
            if distance <= radius[i] + radius[i + 1]:       # collision detection
                prev_x_speed = x_speed[i]       # handling- balls get the velocity of the bal they collide with;
                prev_y_speed = y_speed[i]        # this is more realistic than just giving them an opposite velocity
                x_speed[i] = x_speed[j]
                y_speed[i] = y_speed[j]
                x_speed[j] = prev_x_speed
                y_speed[j] = prev_y_speed

window = pygame.display.set_mode((w, l)) # define window size
pygame.display.set_caption('PyGame Animation') # title of program that

clock = pygame.time.Clock() # used to track time within the game (FPS)
quit = False

setup(num)

while not quit: # main program loop
  for event in pygame.event.get(): # check if there were any events
      if event.type == pygame.QUIT: # check if user clicked the upper
          quit = True
      if event.type == pygame.MOUSEMOTION:
          pos = event.pos       # define tuple "pos", to use as the location of the white circle

  if state == True:     # variable 'state' is True while the cursor-controlled circle has not hit any other ball,
                        # the state is set to False when lose() is run
      window.fill(black)
      count += 1
      pygame.draw.circle(window, white, pos, 20)
      elapsed_time = count
      time = str(math.floor(elapsed_time / 60))
      label_2 = font.render("You survived for " + time + " seconds!", 1, white)     # Losing label initialization
      draw(num)

      seconds = math.floor(elapsed_time / 60)
      ball_collision(num)

      if elapsed_time % 300 == 0:      # since we have 60fps, 300runs of the code == 5 secs, and the speed increments
          for i in range(0, num):
              if x_speed[i] > 0:
                  x_speed[i] += 1
              elif x_speed[i] < 0:
                  x_speed[i] -= 1
              if y_speed[i] > 0:
                  y_speed[i] += 1
              elif y_speed[i] < 0:
                  y_speed[i] -= 1
      if elapsed_time % 600 == 0:       # (every 10 secs) add another ball to window by incrementing 'num'
          num += 1
          setup(num)
      for i in range(0, num):
          if count != 1:
             distance = math.sqrt((x[i] - pos[0]) ** 2 + (y[i] - pos[1]) ** 2)
             if distance <= radius[i] + 20:
                 state = lose()
  pygame.display.update()  # refresh  display
  clock.tick(60)  # wait an amount of time that ensures a frame rate of 60 fps


pygame.quit() # shutdown module
