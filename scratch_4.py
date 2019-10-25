import pygame.midi
import time


w = 800
l = 600
voice_col_1 = [0, 150, 150]
voice_col_2 = [150, 0, 150]
red = [255, 0, 0]
black = [0, 0, 0]
white = [255, 255, 255]
C5 = 3
B5 = 2
A5 = 1
G4 = 0

default = 800
x = default



init_time = time.time()
pygame.midi.init()
player = pygame.midi.Output(0, 1)
player.set_instrument(0)


A0 = 26
Ash0 = 26
Bb0 = 27
B0 = 28
C0 = 29
Csh0 = 30
Db0 = 30
D0 = 31
Dsh0 = 32
Eb0 = 32
E0 = 33
F0 = 34
Fsh0 = 35
Gb0 = 35
G0 = 36
Gsh0 = 37
Ab0 = 37

A1 = 38
Ash1 = 39
Bb1 = 39
B1 = 40
C1 = 41
Csh1 = 42
Db1 = 42
D1 = 43
Dsh1 = 44
Eb1 = 44
E1 = 45
F1 = 46
Fsh1 = 47
Gb1 = 47
G1 = 48
Gsh1 = 49
Ab1 = 49

A2 = 50
Ash2 = 51
Bb2 = 51
B2 = 52
C2 = 53
Csh2 = 54
Db2 = 54
D2 = 55
Dsh2 = 56
Eb2 = 56
E2 = 57
F2 = 58
Fsh2 = 59
Gb2 = 59
G2 = 60
Gsh2 = 61
Ab2 = 61

A3 = 61
Ash3 = 62
Bb3 = 62
B3 = 63
C3 = 64
Csh3 = 65
Db3 = 65
D3 = 66
Dsh3 = 67
Eb3 = 67
E3 = 68
F3 = 69
Fsh3 = 70
Gb3 = 70
G3 = 71
Gsh3 = 72
Ab3 = 72
A4 = 73
B4 = 75
C4 = 76
D4 = 78
E4 = 80
F4 = 81
G4 = 83

X = 0


notes1 = [ E3, A4, C4, B4, E3, B4, D4, C4, E4, Gsh3, E4,
          A4, E3, A4, C4, B4, E3, B4, D4, C4, A4, X, X, X, X,
          X, E4, C4, E4, A4, C4, E3, G3, F3, A4, D4, F4,
          D4, B4, D4, G3, B4, D3, F3, E3, G3, C4, E4]
len_1 = [ 1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 15,
         1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3,
         1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3]
notes2 = [A2, A3, Gsh2, A3, E2, A3, C3, B3, E2, B3, D3,
          C3, A3, Gsh2, E2, A3, E2, A3, C3, B3, E2, B3, D3,
          C3, A3, C3, A3,]
len_2 = [2, 4, 2, 1, 1, 1, 1, 1, 1, 1, 1,
         2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1,
         2, 2, 2, 2,]

for i in range(0, len(notes1)):
    note1 = notes1[i]
    cur_time = time.time()
    while int(cur_time - init_time) == len_1[i]:
        player.note_off(notes1[i], 100)
        player.note_on(notes1[i + 1], 100)
        time.sleep(1)


del player
pygame.midi.quit()
