import pygame.midi
import pygame
#import pygame module

#defining all notes, each note is a tuple (x,y) where x is the positional argument and y is the midi note value
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
Dsh4 = (-8.5, 75)
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

#initialize lists with the notes to be played. There is also a corresponding list of note lengths.
notes1 = [G3, G3, G3, Fsh3, E3, D3, C3,
          B3, G3, A3, Fsh3, G2, G3, Fsh3, G3, A4, B4, Csh4,
          D4, D4, D4, Csh4, B4, A4, D4, G3, D4,
          Fsh3, D4, Csh4, D4, E3, D4, Csh4, D4,
          D3, X, A4, Fsh3,
          D3, D3, D3, B4, G3, D3, D3, D3, C4, A4,
          D3, D3, D3, Fsh3, A4, C4, A4, C4, Fsh4, C4, Fsh4,
          G4, A5, Fsh4, G4,
          X, B4, A4, C4, B4, A4, G3,
          G4, A4, Fsh3, G3,
          F4, F4, F4, B4, E4, A5, Fsh4, G4,
          A4, B4, C4, D4, C4, B4, A4,
          G3, A4, B4, C4, D4, E4, Fsh4, G4, D4, B5, A5, G4, Fsh4,
          G4, B5, D4, F4, E4, D4, E4, C4, G4, F4, E4, D4,
          E4, G4, C4, B4, A4, G3, A4, Fsh3, C4, B4, A4, G3,
          A4, C4, Fsh3, A4, G3, Fsh3, G3, D3, G3, B4, D4, B4, G4,
          B4, A4, X,
          X, A4, D4, E4, Fsh4, D4, Fsh4, A5, C5, X,
          X, G3, B4, D4, G4, D4, G4, A5, B5, X,
          X, Csh4, D4, E4, Fsh4, G4, E4, Csh4, A4, G4,
          A5, Fsh4, D4, B4, Csh4, Fsh4, E4, D4, Csh4, B4,

          A4, Csh4, E4, Csh4, A5, E4, Csh4, E4, A4, Csh4, E4, Csh4, A5, E4, Csh4, E4,
          A4, D4, Fsh4, D4, A5, Fsh4, D4, Fsh4, A4, C4, Fsh4, C4, A5, Fsh4, C4, Fsh4,
          B4, D4, G4, D4, B5, G4, D4, G4, B4, D4, G4, D4, B5, G4, D4, G4,
          C4, E4, G4, E4, B5, G4, E4, G4, C4, E4, G4, E4, B5, G4, E4, G4,
          A4, C4, E4, C4, A5, E4, C4, E4, A4, C4, E4, C4, A5, E4, C4, E4,
          B4, Dsh4, Fsh4, Dsh4, A5, Fsh4, Dsh4, Fsh4, B4, Dsh4, Fsh4, Dsh4, A5, Fsh4, Dsh4, Fsh4,
          B4, Dsh4, E4, Dsh4, G4, E4, Dsh4, E4, B4, Dsh4, E4, Dsh4, G4, E4, Dsh4, E4,
          B4, Dsh4, E4, Dsh4, Fsh4, E4, Dsh4, E4, A4, Dsh4, E4, Dsh4, Fsh4, E4, Dsh4, E4,

          E3, E4, E4, D4, C4, B4, E4, A4, E4,
          G3, B4, E4, Fsh3, Dsh4, E3, Dsh3, E3, Fsh3, G3, A4, B4, C4,
          D4, E4, F4, E4, G4, F4, E4, D4, F4, E4, D4, C4, G4,
          Fsh4, E4, D4, C4, B4, A4, B4, G3, X, E4, Csh4,
          A4, A4, A4, Fsh4, D4, A4, A4, A4, G4, E4,
          A4, A4, A4, Csh4, E4, G4, E4, Csh4, A4, Csh4, E4,

          Fsh4, G4, E4, Fsh4, A4, A4, A4, Fsh4,
          G3, G4, E4, Fsh4, X, Fsh3, E3, G3, Fsh3, E3, D3,
          D4, G4, E4, Fsh4, Csh4, A4, D4,
          Fsh4, A5, Csh4, E4, G4, Fsh4, A5, G4, Fsh4, E4, D4, Csh4,

          D4, D4, D4, Csh4, B4, A4, G3, Fsh3, E3,
          Fsh3, A4, D4, E3, Csh4, D3, X, X,
          E4, E4, E4, D4, C4, B4, A4, G3, Fsh3,
          G3, B4, E4, Fsh3, Dsh4, E3, X, X,
          B5, B5, B5, A5, G4, Fsh4, G4, E4, Fsh4,
          Dsh4, E4, Fsh4, A5, G4, Fsh4, E4, Dsh4, E4, Dsh4, Csh4, B4, Csh4, Dsh4, E4, Fsh4,

          G4, B5, G4, E4, X, G4, E4, B4,
          X, E4, Csh4, A4, X, A5, E4, Csh4,
          X, A5, Fsh4, D4, X, Fsh4, D4, A4,
          X, D4, B4, G3, X, G4, D4, B4,]
len_1 = [4, 4, 2, 1, 1, 2, 2,
         2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1,
         4, 4, 2, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1,
         4, 2, 1, 1,
         2, 2, 2, 1, 1, 2, 2, 2, 1, 1,
         2, 2, 2, 1, 1, 2, 1, 1, 2, 1, 1,
         2, 2, 2, 2,
         2, 1, 1, 1, 1, 1, 1,
         2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 1, 1, 2, 2, 4, 4,
         2, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1,
         1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1,
         1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1,
         1, 1, 3, 1, 1, 1,1, 1, 1, 1, 1, 1, 2, 2, 2,
         2, 2, 4,
         2, 2, 2, 2, 1, 1, 1, 1, 2, 2,
         2, 2, 2, 2, 1, 1, 1, 1, 2, 2,
         2, 1, 1, 1, 1, 4, 1, 1, 2, 4,
         2, 2, 1, 1, 1, 1, 1, 1, 1, 1,

         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,

         2, 4, 4, 1, 1, 1, 1, 1, 1,
         1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6,
         1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1,
         2, 2, 2, 1, 1, 2, 2, 2, 1, 1,
         2, 2, 2, 1, 1, 2, 1, 1, 2, 1, 1,

         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 5,
         1, 2, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1,
         4, 4, 2, 1, 1, 1, 1 ,1, 1,
         1, 1, 2, 2, 2, 2, 2, 4,
         4, 4, 2, 1, 1, 1, 1, 1, 1,
         1, 1, 2, 2, 2, 2, 2, 4,
         4, 4, 2, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,]

notes2 = [G2, G2, G2, Fsh2, E2, D2, C2,
          B2, G2, A2, Fsh2, G1, X,
          D3, D3, D3, Csh3, B3, A3, D3, G2, D3,
          Fsh2, D3, Csh3, D3, E2, D3, Csh3, D3,
          D2, E2, Fsh2, G2, A3, B3, C3, A3,
          Fsh2, A3, Fsh2, D2, D2, D2, B3, G2, D2, D2,
          D2, C3, A3, D2, D2, D2, Fsh2, A3, C3, Fsh2, A3,
          B3, C3, A3, B3,
          D2, D2, D2, B3,
          C2, C3, A3, B3,
          X, B3, A3, C3, B3, A3, G2,
          G2, C3, A3, B3, Fsh2, D2, G2,
          B3, D3, Fsh2, A3, C3, B3, X,
          X, D2, G2, A3, B3, G2, B3, D3, F3, X,
          X, C2, E2, G2, C3, G2, C3, D3, E3, X,
          X, Fsh2, G2, A3, B3, C3, A3, Fsh2, D2, C3,
          D3, B3, G2, Fsh2, E2, Fsh2, G2, A3, B3, Csh3, #4th
          D3, A3, Fsh3, E3, D3, Csh3, D3, Fsh3, A3, C3, B3, A3,
          B3, G2, D3, C3, B3, A3, B3, D3, G2, Fsh2, E2, D2,
          E2, Csh2, G2, Fsh2, E2, D2, E2, G2, Csh2, E2, D2, Csh2,
          D2, A2, D2, Fsh2, A3, Fsh2, D3, Fsh2, E2, X,
          X, Csh2, E2, A3, X, Csh2, E2, A3,
          X, D2, Fsh2, A3, X, D2, Fsh2, A3,
          X, D2, G2, B3, X, D2, G2, B3,
          X, C2, G2, B3, X, E2, G2, B3,
          X, C2, E2, A3, X, C2, E2, A3,
          X, B2, Fsh2, A3, X, B2, Fsh2, A3,
          X, B2, E2, G2, X, B2, E2, G2,
          X, Fsh2, A3, C3, X, B3, A3, Fsh3,

          G2, A3, B3, A3, C3, B3, A3, Gsh2, A3, G2, Fsh2, E2, E3,
          D3, C3, B3, A3, G2, Fsh2, G2, E2, X,
          X, G2, G2, Fsh2, E2, D2, G2, C2, G2,
          B2, D2, G2, A2, Fsh2, G1, B2, C2, D2, E2, Fsh2, G2,
          E2, Csh2, A2, A2, A2, Fsh2, D2, A2, A2, A2,
          G2, E2, A2, A2, A2, Csh2, E2, G2, E2, Csh2,

          A2, E2, Csh2, D2, X, Fsh1, E1, G1, Fsh1, E1, D1,
          D2, E1, Csh1, D1, C2, C2, C2, Fsh1,
          B2, E2, Csh2, D2, E1, Fsh1, G1, A2, G1,
          Fsh1, E1, D1, X,
          X, X,
          A3, A3, A3, G2, Fsh2, E2, D2, C2, B2,
          C2, E2, A3, B2, Gsh2, A2, X, X,
          B3, B3, B3, A3, G2, Fsh2, G2, E2, Fsh2,
          Csh2, E2, Fsh2, Dsh2, E2, Dsh2, Csh2, B2, E2, Fsh2, G2, A3, B3, G2, A3,
          Fsh2, G2, A3, C3, B3, A3, G2, Fsh2, G2, Fsh2, E2, Dsh2, E2, Fsh2, G2, A3,

          B3, G2, E2, G2, B2, E2, G2, E2, B3, G2, E2, G2, B2, E2, G2, E2,
          A3, E2, Csh2, E2, A2, Csh2, E2, Csh2, A3, E2, Csh2, E2, A2, Csh2, E2, Csh2,
          A3, Fsh2, D2, Fsh2, A2, D2, Fsh2, D2, A3, Fsh2, D2, Fsh2, A2, D2, Fsh2, D2,
          G2, D2, B2, D2, G1, B2, D2, B2, G2, D2, B2, D2, G1, B2, D2, B2,
          G2, E2, B2, E2, G1, B2, E2, B2, G2, E2, B2, E2, G1, B2, E2, B2,]
len_2 = [4, 4, 2, 1, 1, 2, 2,
         2, 2, 2, 2, 2, 6,
         4, 4, 2, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1,
         2, 1, 1, 2, 2, 2, 1, 1, 2, 2,
         2, 1, 1, 2, 2, 2, 1, 1, 2, 1, 1,
         2, 2, 2, 2,
         2, 2, 2, 2,
         2, 2, 2, 2,
         2, 1, 1, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 5,
         1, 2, 1, 1, 2, 4, 4,
         2, 2, 2, 2, 1, 1, 1, 1, 2, 2,
         2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2,
         1, 1, 1, 1, 4, 1, 1, 2, 4,
         2, 2, 3, 1, 1, 1, 1, 1, 1, 1, #4th
         1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1,
         1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1,
         1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 2, 2, 2, 4,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,

         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6,
         1, 1, 1, 1, 1, 1, 2, 2, 4,
         2, 4, 4, 1, 1, 1, 1, 1, 1,
         1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 4,
         1, 1, 2, 2, 2, 1, 1, 2, 2,
         2, 1, 1, 2, 2, 2, 1, 1, 2, 1, 1,

         2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 1, 1, 2, 2,
         4, 4, 4, 4,
         8, 8,
         4, 4, 2, 1, 1, 1, 1, 1, 1,
         1, 1, 2, 2, 2, 2, 2, 4,
         4, 4, 2, 1, 1, 1, 1, 1, 1 ,
         1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,

         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,]

notes3 = [G1, Fsh1, G1, A2, B2, A2, B2, C2,
          D2, D1, G0, B2, A2, G1, Fsh1, E1, D1, E1,
          Fsh1, E1, Fsh1, G1, A2, A1,
          B1, B2, Fsh1, A2,
          C2, X, D1, B2, X, D1,
          A2, G1, Fsh1, E1, D1, C1, B1, A1,
          G0, X, Fsh0, X,
          E0, X, D0, X,
          C0, C1, B1, C1, D2, D1,
          G0, C2, B2, A2, G1, X,
          X, G1, G1, G1, G0, X,
          X, G1, G1, G1, G0, X,
          X, G1, G1, G1, G0, B1, G0, B1,
          D1, G0, Fsh0, E0, D0, X,
          X, D1, D1, D1, D0, X,
          X, D1, D1, D1, D0, X,
          X, D1, D1, D1, D0, Fsh1, D1, Fsh1,
          A2, A1, Csh1, E1,
          A2, G1, Fsh1, D1,
          G1, Fsh1, E1, C1,
          Fsh1, E1, Dsh1, B1,
          E1, G1, B2, B1,
          E1, D1, C1, G0,
          A1, B1, E0, E1, D1, C1,
          B1, D1, B1, G0, C1, A1, B1, E1,
          D1, C1, D1, D0, G0, Fsh0, G0, E0,
          Csh1, X, A1, Fsh1, X, A1,
          E1, D1, Csh2, B1, A1, G1, Fsh1, E1,

          D1, X, Csh1, X,
          B1, X, A1, X,
          G0, G1, Fsh1, G1,
          A2, A1, D1, Csh1, D1, E1,
          Fsh1, G1, E1, Fsh1, D1, E1, Csh1, D1, B1, G1, Csh1, A2,
          D1, Fsh1, D1, A2, Fsh1, G1, E1, Fsh1, D1, Gsh1, E1,
          A2, A1, C1, A1, E1, C1, D1, B1, C1, A1, Dsh1, B1,
          E1, G1, E1, B2, G1, A2, Fsh1, G1, E1, A2,
          Fsh1, G1, E1, C2, C1, C2,
          Dsh1, E1, Ash1, B1, A2, G1, Fsh1,

          E1, D1,
          Csh1, A1,
          D1, Csh1,
          B1, G0,
          Csh1, B1,
          Ash1, Fsh0,]
len_3 = [2, 2, 2, 2, 2, 2, 2, 2,
         4, 4, 2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 4, 4,
         2, 2, 2, 2,
         4, 2, 2, 4, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         4, 4, 4, 4,
         4, 4, 4, 4,
         4, 8, 2, 2, 4, 4,
         2, 2, 2, 2, 4, 4,
         2, 2, 2, 2, 4, 4,
         2, 2, 2, 2, 4, 4,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 4, 4,
         2, 2, 2, 2, 4, 4,
         2, 2, 2, 2, 4, 4,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2,
         8, 8, 8, 8,
         8, 8, 8, 8,
         8, 8, 8, 8,
         8, 8, 8, 8,
         4, 4, 4, 4,
         4, 4, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         4, 2, 2, 4, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,

         4, 4, 4, 4,
         4, 4, 4, 4,
         4, 8, 2, 2,
         4, 4, 2, 2, 2, 2,
         1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2,
         2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2,
         1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2,
         2, 1, 1, 1, 1, 1 ,1 ,2, 2, 6,
         2, 2, 2, 2, 2, 6,
         2, 2, 2, 2, 2, 2, 2,

         8, 8,
         8, 8,
         8, 8,
         8, 8,
         8, 8,
         8, 8,
         ]

w = 800 #define window size
l = 600

red = [255, 0, 0]
black = [0, 0, 0]
white = [255, 255, 255]

play_pos_x = w / 2 #define the location where notes will be played on the screen (right now it is set for the middle)
y_0 = l / 2 #set the location of the middle C (C3) note on the screen

dark_voice_col_1 = [100, 0, 0] #define the colours that are shown when the note is not played
dark_voice_col_2 = [75, 100, 0]
dark_voice_col_3 = [139,69,19]

lit_voice_col_1 = [255, 0, 0] #define the colours that are shown when the note is played
lit_voice_col_2 = [150, 255, 0]
lit_voice_col_3 = [210,180,140]

#define outlines for the notes (outline_x can change, so original_outline_x is used to reset it if need be)
original_outline_1 = 1
original_outline_2 = 1
original_outline_3 = 1
outline_1 = original_outline_1
outline_2 = original_outline_2
outline_3 = original_outline_3

#define instruments. A full list of midi instruments is found at https://en.wikipedia.org/wiki/General_MIDI#Program_change_events
instrument_1 = 3
instrument_2 = 3
instrument_3 = 3

appear_1 = True #define if the notes appear once they are played, or are visible the whole time
appear_2 = True
appear_3 = True

#define if the notes are filled in completely WHEN PLAYED (to keep them filled after, the outline has to be changed to 0
fill_1 = True
fill_2 = True
fill_3 = True

default = w / 2 + 100 #define the location that the notes start scrolling from
x = default

pygame.init()
pygame.midi.init()
player = pygame.midi.Output(0)


window = pygame.display.set_mode((w, l)) # define window size
pygame.display.set_caption('Graphical Score Studio') # title of program
clock = pygame.time.Clock() # used to track time within the game (FPS)
quit = False

state_list_1 = [] #initialize the state lists (see function definitions in document)
state_list_2 = []
state_list_3 = []

scale_x = 14 #scale of the x-axis, this will change the speed at which the notes play but not their scrolling
scale_y = 10#scale of y-axis, i.e. vertical positioning of the notes
y_stretch = 10#thickness of the bars
original_speed = 2#initial speed, this changes the speed at which the notes scroll
speed = original_speed

shape_1 = 0#define shape of notes (0 = rectangular, 1 = circular)
shape_2 = 0
shape_3 = 0



font1 = pygame.font.SysFont('times new roman', 20,)
font2 = pygame.font.SysFont('times new roman', 20, False, True)
font3 = pygame.font.SysFont('times new roman', 40, False, False)

label1 = font1.render("J. S. Bach", 1, white)
label2 = font2.render("Organ Sonata No.6 in G major BWV 530", 1, white)
label3 = font3.render("Graphic Score Studio", 1, white)
label4 = font1.render("Play built-in example: Bach Triosonata in G BWV 530", 1, white)
label5 = font1.render("Go to Music Studio", 1, white)

x_label = font1.render(" X ", 1, white)

labelC1 = font2.render("C1", 1, white)
labelC2 = font2.render("C2", 1, white)
labelC3 = font2.render("C3", 1, red)
labelC4 = font2.render("C4", 1, white)
labelC5 = font2.render("C5", 1, white)

cover_image = pygame.image.load('main screen image.png')


state = 0

def setup():
    for i in range(0, len(len_1)):
        state_list_1.append(False)
    for i in range(0, len(len_2)):
        state_list_2.append(False)
    for i in range(0, len(len_3)):
        state_list_3.append(False)

def prepare_studio():
    window.fill(black)
    pygame.draw.line(window, red, (0, l / 2), (w, l / 2), 1)
    window.blit(labelC3, (0, l / 2))
    pygame.draw.line(window, white, (0, l / 2 + 7 * scale_y), (w, l / 2 + 7 * scale_y), 1)
    window.blit(labelC2, (0, l / 2 + 7 * scale_y))
    pygame.draw.line(window, white, (0, l / 2 + 14 * scale_y), (w, l / 2 + 14 * scale_y), 1)
    window.blit(labelC1, (0, l / 2 + 14 * scale_y))
    pygame.draw.line(window, white, (0, l / 2 - 7 * scale_y), (w, l / 2 - 7 * scale_y), 1)
    window.blit(labelC4, (0, l / 2 - 7 * scale_y))
    pygame.draw.line(window, white, (0, l / 2 - 14 * scale_y), (w, l / 2 - 14 * scale_y), 1)
    window.blit(labelC5, (0, l / 2 - 14 * scale_y))
    pygame.draw.rect(window, white, (w - 50, 10, 40, 20,), thickness)
    window.blit(x_label, (w - 40, 10))
def axis(x, y):
    if x == True:
        pygame.draw.line(window, red, (0, y_0), (w, y_0))
    if y == True:
        pygame.draw.line(window, white, (play_pos_x, 50), (play_pos_x, l - 50), )

setup()

count_keys = 0
thickness = 2 #thickness of outlines of the boxes that the user clicks on

while not quit:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True

        if event.type == pygame.MOUSEBUTTONUP:
            pos = event.pos
            if 175 < pos[0] < 685 and 170 < pos[1] < 200:
                state = 1
            elif w - 50 < pos[0] < w - 10 and 20 < pos[1] < 30:
                state = 0
            elif 175 < pos[0] < 685 and 205 < pos[1] < 235:
                state = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and count_keys % 2 != 0:
                speed = 0
                count_keys += 1
            elif event.key == pygame.K_SPACE and count_keys % 2 == 0:
                speed = original_speed
                count_keys += 1
            if event.key == pygame.K_LEFT:
                speed -= 0.1
            if event.key == pygame.K_RIGHT:
                speed += 0.1
            if event.key == pygame.K_UP:
                instrument_1 += 1
                instrument_2 += 1
                instrument_3 += 1
            if event.key == pygame.K_DOWN:
                instrument_1 -=1
                instrument_2 -=1
                instrument_3 -=1


    if state == 0: #Home screen

        window.fill(black)
        window.blit(label3, (200, 100))
        window.blit(label4, (200, 175))
        window.blit(label5, (200, 210))
        pygame.draw.rect(window, white, (175, 170, 490, 30,), thickness)
        pygame.draw.rect(window, white, (175, 205, 490, 30,), thickness)
        window.blit(cover_image, (0, l - 270))



    if state == 1: #Example code screen

        window.fill(black)
        pygame.draw.rect(window, white, (w - 50, 10, 40, 20,), thickness)
        window.blit(x_label, (w - 40, 10))
        window.blit(label1, (10, 10))
        window.blit(label2, (10, 30))


        player.set_instrument(instrument_1)

        for i in range(0, len(notes1)):
            y_pos = notes1[i][0] * scale_y + y_0
            play_time = len_1[i] * scale_x
            if play_pos_x - play_time < x < play_pos_x and notes1[i] != X:
                voice_col_1 = lit_voice_col_1
                if state_list_1[i] != True:
                    player.note_on(notes1[i][1], 100)
                    state_list_1[i] = True
                if fill_1 == True:
                    outline_1 = 0


            else:
                if x > play_pos_x and appear_1 == True:
                    voice_col_1 = black

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
                pygame.draw.circle(window, voice_col_1, (int(x) + int(play_time / 2), int(y_pos)), int(play_time / 2),
                                   outline_1)

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
                    voice_col_2 = black
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
                pygame.draw.circle(window, voice_col_2, (int(x) + int(play_time / 2), int(y_pos)), int(play_time / 2),
                                   outline_2)

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
                    voice_col_3 = black
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
                pygame.draw.circle(window, voice_col_3, (int(x) + int(play_time / 2), int(y_pos)), int(play_time / 2),
                                   outline_3)

            x += len_3[i] * scale_x
        x = default - speed
        default = x
        axis(False, False)

    if state == 2:
        prepare_studio()

    pygame.display.update() # refresh your display
    clock.tick(60) # wait a certain amount of time that
# ensures a frame rate of 60 fps

pygame.quit() # shutdown module
