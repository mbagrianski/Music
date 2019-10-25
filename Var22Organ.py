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
Db4 = (-7.5, 73)
D4 = (-8,74)
Dsh4 = (-8.5, 75)
Eb4 = (-8.5, 75)
E4 = (-9,76)
F4 = (-10,77)
Fsh4 = (-10.5, 78)
Gb4 = (-10.5, 78)
G4 = (-11,79)
Ab4 = (-11.5, 80)
A5 = (-12,81)
Bb5 = (-12.5, 82)
B5 = (-13,83)
C5 = (-14,84)
Db5 = (-14.5, 85)
D5 = (-15,86)
Eb5 = (-15.5, 87)
F5 = (-16, 89)
G5 = (-17, 91)
X = (1000,1000)

notes1 = [X,
          X,
          X,
          X,

          X, D4,
          C4, B4, C4, E4,
          A4, D4, C4,
          B4, A4, B4,

          B4, A4, B4,
          A4, D4,
          E4,
          E4,

          E4, D4, Csh4, D4, Fsh4,
          B4, E4, D4,
          E4, D4, Csh4,
          D4, A4, G3, A4,

X,
          X,
          X,
          X,

          X, D4,
          C4, B4, C4, E4,
          A4, D4, C4,
          B4, A4, B4,

          B4, A4, B4,
          A4, D4,
          E4,
          E4,

          E4, D4, Csh4, D4, Fsh4,
          B4, E4, D4,
          E4, D4, Csh4,
          D4, A4, G3, A4,
          ]
len_1 = [8,
         8,
         8,
         8,

         4, 6,
         1, 1, 2, 2,
         2, 4, 4,
         1, 1, 6,

         1, 1, 4,
         4, 4,
         8,
         8,

         2, 1, 1, 2, 2,
         6, 1, 1,
         2, 4, 2,
         2, 1, 1, 4,

8,
         8,
         8,
         8,

         4, 6,
         1, 1, 2, 2,
         2, 4, 4,
         1, 1, 6,

         1, 1, 4,
         4, 4,
         8,
         8,

         2, 1, 1, 2, 2,
         6, 1, 1,
         2, 4, 2,
         2, 1, 1, 4,
         ]

notes2 = [X,
          X,
          X, G3,
          Fsh3, E3, Fsh3, A4,

          D3, F3,
          E3, G3,
          Fsh3, E3, Fsh3, A4,
          G3, Fsh3, G3, B4,

          E3, B4,
          Csh4, A5, G4, Fsh4,
          G4, A5, G4, A5, G4, A5, G4, A5, G4, A5,
          G4, A5, G4, A5, G4, A5, G4, A5, G4, A5,
          G4, A5, G4, A5, G4, A5, G4, A5, G4, A5,
          G4, A5, G4, A5, G4, A5, G4, A5, G4, A5,

          G4, Fsh4, E4, Fsh4, A5,
          D4, G4,
          Fsh4, E4,
          D4,

X,
          X,
          X, G3,
          Fsh3, E3, Fsh3, A4,

          D3, F3,
          E3, G3,
          Fsh3, E3, Fsh3, A4,
          G3, Fsh3, G3, B4,

          E3, B4,
          Csh4, A5, G4, Fsh4,
          G4, A5, G4, A5, G4, A5, G4, A5, G4, A5,
          G4, A5, G4, A5, G4, A5, G4, A5, G4, A5,
          G4, A5, G4, A5, G4, A5, G4, A5, G4, A5,
          G4, A5, G4, A5, G4, A5, G4, A5, G4, A5,

          G4, Fsh4, E4, Fsh4, A5,
          D4, G4,
          Fsh4, E4,
          D4,

          ]
len_2 = [8,
         8,
         4, 6,
         1, 1, 2, 2,

         6, 2,
         6, 4,
         1, 1, 2, 4,
         1, 1, 2, 2,

         4, 4,
         2, 4, 1, 1,
         0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4,
         0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4,
         0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4,
         0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4,

         2, 1, 1, 2, 2,
         4, 6,
         2, 4,
         8,

8,
         8,
         4, 6,
         1, 1, 2, 2,

         6, 2,
         6, 4,
         1, 1, 2, 4,
         1, 1, 2, 2,

         4, 4,
         2, 4, 1, 1,
         0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4,
         0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4,
         0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4,
         0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4,

         2, 1, 1, 2, 2,
         4, 6,
         2, 4,
         8,
         ]
notes3 = [X, E3,
          D3, Csh3, D3,
          Csh3, B3, Csh3, E3,
          A3,

          G2, Fsh2, G2,
          E2, A3,
          A3, G2, A3, Fsh2,
          X,

          E3, E3,
          D3, Csh3, D3,
          Csh3, B3, Csh3, E3,
          A3,

          X, A3,
          G2, Fsh2, G2, B2,
          Csh2, D2, E2, Fsh2, G2,
          Fsh2, E2, Fsh2,

X, E3,
          D3, Csh3, D3,
          Csh3, B3, Csh3, E3,
          A3,

          G2, Fsh2, G2,
          E2, A3,
          A3, G2, A3, Fsh2,
          X,

          E3, E3,
          D3, Csh3, D3,
          Csh3, B3, Csh3, E3,
          A3,

          X, A3,
          G2, Fsh2, G2, B2,
          Csh2, D2, E2, Fsh2, G2,
          Fsh2, E2, Fsh2,
          ]
len_3 = [4, 6,
         1, 1, 6,
         1, 1, 2, 2,
         10,

         1, 1, 6,
         2, 6,
         1, 1, 2, 2,
         8,

         4, 6,
         1, 1, 6,
         1, 1, 2, 2,
         8,

         4, 6,
         1, 1, 2, 2,
         2, 2, 1, 1, 4,
         1, 1, 4,

         4, 6,
         1, 1, 6,
         1, 1, 2, 2,
         10,

         1, 1, 6,
         2, 6,
         1, 1, 2, 2,
         8,

         4, 6,
         1, 1, 6,
         1, 1, 2, 2,
         8,

         4, 6,
         1, 1, 2, 2,
         2, 2, 1, 1, 4,
         1, 1, 4,
         ]

notes4 = [G2,
          Fsh2,
          E2,
          D2, C2,

          B2,
          C2,
          D2,
          G1,

          G2, Fsh2, G2,
          Fsh2, E2, Fsh2, B3,
          E2, D2,
          Csh2, B2, Csh2, E2,

          Fsh1, Fsh2,
          G1, E2,
          A2,
          D1,
          G2,
          Fsh2,
          E2,
          D2, C2,

          B2,
          C2,
          D2,
          G1,

          G2, Fsh2, G2,
          Fsh2, E2, Fsh2, B3,
          E2, D2,
          Csh2, B2, Csh2, E2,

          Fsh1, Fsh2,
          G1, E2,
          A2,
          D1,
          ]
len_4 = [8,
         8,
         8,
         6, 2,

         8,
         8,
         8,
         10,

         1, 1, 6,
         1, 1, 2, 2,
         6, 4,
         1, 1, 2, 2,

         4, 4,
         4, 4,
         8,
         8,

         8,
         8,
         8,
         6, 2,

         8,
         8,
         8,
         10,

         1, 1, 6,
         1, 1, 2, 2,
         6, 4,
         1, 1, 2, 2,

         4, 4,
         4, 4,
         8,
         8,
         ]

notes5 = [
          ]
len_5 = [8,
         8,
         8,
         6, 2,

         8,
         8,
         8,
         10,

         1, 1, 6,
         1, 1, 2, 2,
         6, 4,
         1, 1, 2, 2,

         32,

         8,
         8,
         8,
         6, 2,

         8,
         8,
         8,
         10,

         1, 1, 6,
         1, 1, 2, 2,
         6, 4,
         1, 1, 2, 2,

         32,
         ]



w = 800
l = 600

red = [255, 0, 0]
black = [0, 0, 0]
white = [255, 255, 255]

play_pos_x = w / 2
y_0 = l / 2

dark_voice_col_1 = [100, 0, 0]
dark_voice_col_2 = [100, 50, 0]
dark_voice_col_3 = [100,100,0]
dark_voice_col_4 = [100,150,0]
dark_voice_col_5 = [100,150,0]

lit_voice_col_1 = [255, 0, 0]
lit_voice_col_2 = [255, 100, 0]
lit_voice_col_3 = [255,150,0]
lit_voice_col_4 = [255,225,0]
lit_voice_col_5 = [255,225,0]

background_col = black

original_outline_1 = 1
original_outline_2 = 1
original_outline_3 = 1
original_outline_4 = 1
original_outline_5 = 1

outline_1 = original_outline_1
outline_2 = original_outline_2
outline_3 = original_outline_3
outline_4 = original_outline_4
outline_5 = original_outline_4


instrument_1 = 60
instrument_2 = 60
instrument_3 = 60
instrument_4 = 60
instrument_5 = 60


appear_1 = True
appear_2 = True
appear_3 = True
appear_4 = True
appear_5 = True


fill_1 = True
fill_2 = True
fill_3 = True
fill_4 = True
fill_5 = True


default = w / 2 + 100
x = default

pygame.init()
pygame.midi.init()
player = pygame.midi.Output(0)


window = pygame.display.set_mode((w, l)) # define window size
pygame.display.set_caption('Graphical Score Studio') # title of program that
clock = pygame.time.Clock() # used to track time within the game (FPS)
quit = False

count = 0
state = False
state_list_1 = []
state_list_2 = []
state_list_3 = []
state_list_4 = []
state_list_5 = []


def setup():
    for i in range(0, len(len_1)):
        state_list_1.append(False)
    for i in range(0, len(len_2)):
        state_list_2.append(False)
    for i in range(0, len(len_3)):
        state_list_3.append(False)
    for i in range(0, len(len_4)):
        state_list_4.append(False)
    for i in range(0, len(len_5)):
        state_list_5.append(False)

original_scale_x = 14
scale_x = original_scale_x
scale_y = 10
y_stretch = 10
original_speed = 1.1
speed = original_speed

count = 0

setup()

shape_1 = 0
shape_2 = 0
shape_3 = 0
shape_4 = 0
shape_5 = 0



font1 = pygame.font.SysFont('times new roman', 20,)
font2 = pygame.font.SysFont('times new roman', 20, False, True)

label1 = font1.render("Смуглянка Молдаванка", 1, white)
label2 = font2.render("", 1, white)



while not quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True

    window.fill(background_col)
    window.blit(label1, (10, 10))
    window.blit(label2, (10, 30))


    label3 = font1.render("int(i) == " + str(count), 1, white)
    window.blit(label3, (100, 100))

    if count >= 60:
        if count % 2 == 0 and speed > 0.5:
            speed -= 0.003
    else:
        speed = original_speed


    player.set_instrument(instrument_1)

    for i in range(0, len(notes1)):

        y_pos = notes1[i][0] * scale_y + y_0
        play_time = len_1[i] * scale_x
        if play_pos_x - play_time < x < play_pos_x and notes1[i] != X:
            voice_col_1 = lit_voice_col_1
            count = i

            if state_list_1[i] != True:
                player.note_on(notes1[i][1], 100)
                state_list_1[i] = True

            if fill_1 == True:
                outline_1 = 0



        else:
            if x > play_pos_x and appear_1 == True:
                voice_col_1 = background_col

            else:
                voice_col_1 = dark_voice_col_1
            if fill_1 == True:
                outline_1 = original_outline_1
            if state_list_1[i] != False:
                player.note_off(notes1[i][1], 100)
                state_list_1[i] = False

        if shape_1 == 0:
            pygame.draw.rect(window, voice_col_1, (x, y_pos, play_time, y_stretch), outline_1)
        elif shape_1 == 1:
            pygame.draw.circle(window, voice_col_1, (int(x) + int(play_time / 2), int(y_pos)), int(play_time / 2), outline_1)

        x += len_1[i] * scale_x
    x = default

    player.set_instrument(instrument_2)

    for i in range(0, len(notes2)):

        y_pos = notes2[i][0] * scale_y + y_0
        play_time = len_2[i] * scale_x
        if play_pos_x - play_time < x < play_pos_x and notes2[i] != X:
            voice_col_2 = lit_voice_col_2
            if state_list_2[i] != True:
                player.note_on(notes2[i][1], 100)
                state_list_2[i] = True
            if x < play_pos_x and fill_2 == True:
                outline_2 = 0

        else:

            if x > play_pos_x and appear_2 == True:
                voice_col_2 = background_col
            else:
                voice_col_2 = dark_voice_col_2
            if fill_2 == True:
                outline_2 = original_outline_2
            if state_list_2[i] != False:
                player.note_off(notes2[i][1], 100)
                state_list_2[i] = False

        if shape_2 == 0:
            pygame.draw.rect(window, voice_col_2, (x, y_pos, play_time, y_stretch), outline_2)
        elif shape_2 == 1:
            pygame.draw.circle(window, voice_col_2, (int(x) + int(play_time / 2), int(y_pos)), int(play_time / 2), outline_2)

        x += len_2[i] * scale_x
    x = default

    player.set_instrument(instrument_3)

    for i in range(0, len(notes3)):
        y_pos = notes3[i][0] * scale_y + y_0
        play_time = len_3[i] * scale_x
        if play_pos_x - play_time < x < play_pos_x and notes3[i] != X:
            voice_col_3 = lit_voice_col_3
            if state_list_3[i] != True:
                player.note_on(notes3[i][1], 100)
                state_list_3[i] = True
            if fill_3 == True:
                outline_3 = 0
        else:

            if x > play_pos_x and appear_3 == True:
                voice_col_3 = background_col
            else:
                voice_col_3 = dark_voice_col_3
            if fill_3 == True:
                outline_3 = original_outline_1

            if state_list_3[i] != False:
                player.note_off(notes3[i][1], 100)
                state_list_3[i] = False

        if shape_3 == 0:
            pygame.draw.rect(window, voice_col_3, (x, y_pos, play_time, y_stretch), outline_3)
        elif shape_3 == 1:
            pygame.draw.circle(window, voice_col_3, (int(x) + int(play_time / 2), int(y_pos)), int(play_time / 2), outline_3)

        x += len_3[i] * scale_x

    x = default

    player.set_instrument(instrument_4)

    for i in range(0, len(notes4)):
        y_pos = notes4[i][0] * scale_y + y_0
        play_time = len_4[i] * scale_x
        if play_pos_x - play_time < x < play_pos_x and notes4[i] != X:
            voice_col_4 = lit_voice_col_4
            if state_list_4[i] != True:
                player.note_on(notes4[i][1], 100)
                state_list_4[i] = True
            if fill_4 == True:
                outline_4 = 0
        else:

            if x > play_pos_x and appear_4 == True:
                voice_col_4 = background_col
            else:
                voice_col_4 = dark_voice_col_4
            if fill_4 == True:
                outline_4 = original_outline_4

            if state_list_4[i] != False:
                player.note_off(notes4[i][1], 100)
                state_list_4[i] = False

        if shape_4 == 0:
            pygame.draw.rect(window, voice_col_4, (x, y_pos, play_time, y_stretch), outline_4)
        elif shape_4 == 1:
            pygame.draw.circle(window, voice_col_4, (int(x) + int(play_time / 2), int(y_pos)), int(play_time / 2),
                               outline_4)

        x += len_4[i] * scale_x

    x = default

    player.set_instrument(instrument_5)

    for i in range(0, len(notes5)):
        y_pos = notes5[i][0] * scale_y + y_0
        play_time = len_5[i] * scale_x
        if play_pos_x - play_time < x < play_pos_x and notes5[i] != X:
            voice_col_5 = lit_voice_col_5
            if state_list_5[i] != True:
                player.note_on(notes5[i][1], 100)
                state_list_5[i] = True
            if fill_5 == True:
                outline_5 = 0
        else:

            if x > play_pos_x and appear_5 == True:
                voice_col_5 = background_col
            else:
                voice_col_5 = dark_voice_col_5
            if fill_5 == True:
                outline_5 = original_outline_5

            if state_list_5[i] != False:
                player.note_off(notes5[i][1], 100)
                state_list_5[i] = False

        if shape_5 == 0:
            pygame.draw.rect(window, voice_col_5, (x, y_pos, play_time, y_stretch), outline_5)
        elif shape_5 == 1:
            pygame.draw.circle(window, voice_col_5, (int(x) + int(play_time / 2), int(y_pos)), int(play_time / 2),
                               outline_4)

        x += len_5[i] * scale_x

    x = default - speed
    default = x
    #pygame.draw.line(window, red, (0, y_0), (w, y_0))
    #pygame.draw.line(window, white, (play_pos_x, 50), (play_pos_x, l - 50),)



    pygame.display.update() # refresh your display
    clock.tick(60) # wait a certain amount of time that
# ensures a frame rate of 60 fps

pygame.quit() # shutdown module
