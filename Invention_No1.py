import pygame.midi
import pygame

A0 = (23,21)
Ash0 = (22.5,22)
Bb0 = (22.5,22)
B0 = (22,23)
C0 = (21,24)
Csh0 = (20.5,25)
Db0 = (20.5,25)
D0 = (20,26)
Dsh0 = (19.5,27)
Eb0 = (19.5,27)
E0 = (19,28)
F0 = (18,29)
Fsh0 = (17.5,30)
Gb0 = (17.5,30)
G0 = (17,31)
Gsh0 = (16.5,32)
Ab0 = (16.5,32)

A1 = (16,33)
Ash1 = (15.5,34)
Bb1 = (15.5,34)
B1 = (15,35)
C1 = (14,36)
Csh1 = (13.5,37)
Db1 = (13.5,37)
D1 = (13,38)
Dsh1 = (12.5,39)
Eb1 = (12.5,39)
E1 = (12,40)
F1 = (11,41)
Fsh1 = (10.5,42)
Gb1 = (10.5,42)
G1 = (10,43)
Gsh1 = (9.5,44)
Ab1 = (9.5,44)

A2 = (9,45)
Ash2 = (8.5,46)
Bb2 = (8.5,46)
B2 = (8,47)
C2 = (7,48)
Csh2 = (6.5,49)
Db2 = (6.5,49)
D2 = (6,50)
Dsh2 = (5.5,51)
Eb2 = (5.5,51)
E2 = (5,52)
F2 = (4,53)
Fsh2 = (3.5,54)
Gb2 = (3.5,54)
G2 = (3,55)
Gsh2 = (2.5,56)
Ab2 = (2.5,56)

A3 = (2,57)
Ash3 = (1.5,58)
Bb3 = (1.5,58)
B3 = (1,59)
C3 = (0,60)
Csh3 = (-0.5,61)
Db3 = (-0.5,61)
D3 = (-1,62)
Dsh3 = (-1.5,63)
Eb3 = (-1.5,63)
E3 = (-2,64)
F3 = (-3,65)
Fsh3 = (-3.5,66)
Gb3 = (-3.5,66)
G3 = (-4,67)
Gsh3 = (-4.5,68)
Ab3 = (-4.5,68)
A4 = (-5,69)
Bb4 = (-5.5, 70)
B4 = (-6,71)
C4 = (-7,72)
Csh4 = (-7.5, 73)
D4 = (-8,74)
Eb4 = (-8.5, 75)
E4 = (-9,76)
F4 = (-10,77)
Fsh4 = (-10.5, 78)
G4 = (-11,79)
Ab4 = (-11.5, 80)
A5 = (-12,81)
B5 = (-13,83)
C5 = (-14,84)
D5 = (-15,86)
X = (1000,1000)

w = 800
l = 600
play_pos_x = w / 2
voice_col_1 = [0, 100, 100]
voice_col_2 = [100, 0, 100]
voice_col_3 = [50, 50, 100]

red = [255, 0, 0]
black = [0, 0, 0]
white = [255, 255, 255]


default = 800
x = default

pygame.init()
pygame.midi.init()
player = pygame.midi.Output(0)
player.set_instrument(2)
window = pygame.display.set_mode((w, l)) # define window size
pygame.display.set_caption('Intro to PyGame') # title of program that
clock = pygame.time.Clock() # used to track time within the game (FPS)
quit = False

notes1 = [X, C3, D3, E3, F3, D3, E3, C3, G3, C4, B4, C4,
          D4, G3, A4, B4, C4, A4, B4, G3, D4, G4, F4, G4,
          E4, A5, G4, F4, E4, G4, F4, A5, G4, F4, E4, D4, C4, E4, D4, F4,
          E4, D4, C4, B4, A4, C4, B4, D4, C4, B4, A4, G3, Fsh3, A4, G3, B4,
          A4, D3, C4, D4, B4, A4, G3, Fsh3, E3, G3, Fsh3, A4,
          G3, B4, A4, C4, B4, D4, C4, E4, D4, B4, C4, D4, G4, B4, C4, B4,  A4, G3,
          G3, X, X, X, G3, A4, B4, C4, A4, B4, G3,
          Fsh4, X, X, X, A5, B5, C5, D5, B4, C4, A4,
          ]
len_1 = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2,
         1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         2, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0.5, 1, 1, 0.3, 0.3, 1.4, 1, 1, 1,
         2, 2, 4, 1, 1, 1, 1, 1, 1, 1, 1,
         2, 2, 4, 1, 1, 1, 1, 1, 1, 1, 1,]

notes2 = [X, X, C2, D2, E2, F2, D2, E2, C2,
          G2, G1, X, X, G2, A3, B3, C3, A3, B3, G2,
          C3, B3, C3, D3, E3, G2, A3, B3,
          C3, E2, Fsh2, G2, A3, B3, C3,
          D2, E2, Fsh2, G2, E2, Fsh2, D2, G2, B2, C2, D2,
          E2, Fsh2, G2, E2, B2, C2, D2, D1,
          X, G1, A2, B2, C2, A2, B2, G1, D2, G2, Fsh2, G2,
          A3, D2, E2, Fsh2, G2, E2, Fsh2, D2, A3, D3, C3, D3,]
len_2 = [8, 1, 1, 1, 1, 1, 1, 1, 1,
         2, 2, 4, 1, 1, 1, 1, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 5,
         1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2,
         2, 2, 2, 2, 3, 1, 2, 2,
         1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2,
         1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2,]

notes3 = []
len_3 = []

count = 0
state = False
state1 = False
state_list_1 = []
state_list_2 = []
state_list_3 = []


def setup():
    for i in range(0, len(len_1)):
        state_list_1.append(False)
    for i in range(0, len(len_2)):
        state_list_2.append(False)
    for i in range(0, len(len_3)):
        state_list_3.append(False)
scale_x = 15
scale_y = 10
y_stretch = 12
setup()

while not quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True

    window.fill(black)
    #pygame.draw.line(window, red, (0, 300), (w, 300))
    #pygame.draw.line(window, white, (play_pos_x, 0), (play_pos_x, l))

    for i in range(0, len(notes1)):
        y_pos = notes1[i][0] * scale_y + 300
        play_time = len_1[i] * scale_x
        if play_pos_x - play_time < x < play_pos_x and notes1[i] != X:
            voice_col_1 = [0, 255, 255]
            if state_list_1[i] != True:
                player.note_on(notes1[i][1], 100)
                state_list_1[i] = True
        else:
            voice_col_1 = [0, 100, 100]
            if state_list_1[i] != False:
                player.note_off(notes1[i][1], 100)
                state_list_1[i] = False

        pygame.draw.rect(window, voice_col_1, (x, y_pos, play_time, y_stretch))
        x += len_1[i] * scale_x
    x = default

    for i in range(0, len(notes2)):
        y_pos = notes2[i][0] * scale_y + 300
        play_time = len_2[i] * scale_x
        if play_pos_x - play_time < x < play_pos_x and notes2[i] != X:
            voice_col_2 = [255, 0, 255]
            if state_list_2[i] != True:
                player.note_on(notes2[i][1], 100)
                state_list_2[i] = True
        else:
            voice_col_2 = [100, 0, 100]
            if state_list_2[i] != False:
                player.note_off(notes2[i][1], 100)
                state_list_2[i] = False

        pygame.draw.rect(window, voice_col_2, (x, y_pos, play_time, y_stretch))
        x += len_2[i] * scale_x
    x = default

    for i in range(0, len(notes3)):
        y_pos = notes3[i][0] * scale_y + 300
        play_time = len_3[i] * scale_x
        if play_pos_x - play_time < x < play_pos_x and notes3[i] != X:
            voice_col_3 = [125, 125, 255]
            if state_list_3[i] != True:
                player.note_on(notes3[i][1], 100)
                state_list_3[i] = True
        else:
            voice_col_3 = [50, 50, 100]
            if state_list_3[i] != False:
                player.note_off(notes3[i][1], 100)
                state_list_3[i] = False

        pygame.draw.rect(window, voice_col_3, (x, y_pos, play_time, y_stretch))
        x += len_3[i] * scale_x

    x = default - 1
    default = x



    pygame.display.update() # refresh your display
    clock.tick(60) # wait a certain amount of time that
# ensures a frame rate of 60 fps

pygame.quit() # shutdown module
