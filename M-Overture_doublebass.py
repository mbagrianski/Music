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
X = (1000,1000)

notes1 = [G3,
          X,
          C4, X, C4,
          X,
          Eb4, X, Eb4,
          X,
          Bb4, Ab3, G3,
          F3, F3, F3,
          F3, Ab3, C4, Ab3, F3, F3,
          G3, G3, G3,
          G3, Bb4, Db4, Bb4, G3, G3,
          Ab3, X, Ab3, G3, X, G3,
          F3, X, G3,
          Ab3, X, Ab3, Gb3, X, Gb3,
          F3, X, G3,
          Ab3, X, Ab3, A4, X, A4,
          Bb4, Bb4, Bb4,
          C4, C4, Gb4,
          F4, D4,








    Eb4, X, X,
          X,
          X,
          X,
          Bb4, Bb4, Bb4, Bb4, Bb4, Bb4, C4, Bb4, A4, Bb4,
          Eb4, Eb4, Eb4, Eb4, Eb4, Eb4, F4, Eb4, D4, Eb4,
          D4, D4, G4, G4, C4, C4, F4, F4,
          D4, D4, G4, G4, C4, C4, F4, F4,
          D4, X, Bb5, A5,
          X, Ab4, G4,
          F4, Eb4, D4, C4, Bb4, Ab3,

          G3, Bb4, Eb4,
          D4, C4, Bb4, Ab3, G3, F3,
          Eb3, X, Eb4, D4,
          X, Eb4, D4,
          Eb4, Eb4, C4, C4, F4, F4, D4, D4,
          G4, G4, D4, D4, C4, C4, C4, C4,

          Bb4, X, X, D4,
          C4, Bb4, A3,
          Bb4, X, D4, C4, D4, Eb4, Eb4, C4, C4,
          F4, F4, D4, C4, D4, Eb4, Eb4, C4, C4,
          D4, D4, G4, G4, C4, C4, F4, F4,
          Bb4, Bb4, Eb4, Eb4, Eb4, Eb4, D4, D4,
          Eb4, Eb4, Eb4, Eb4, Eb4, Eb4, F4, Eb4, D4, Eb4,
          Bb5, Bb5, Bb5, Bb5, Bb5, Bb5, C5, Bb5, A5, Bb5,
          G4, X, Eb5,
          D5, C5, Bb5, Ab4, G4, F4,

          G4, Eb4, G4, Eb4, C5, G4, C5, G4, A5, F4, A5, F4, Bb5, F4, Bb5, F4,
          Eb4, G3, Eb4, G3, Ab4, Eb4, Ab4, Eb4, Fsh4, D4, Fsh4, D4, G4, D4, G4, D4,
          C4, Eb3, C4, Eb3, F4, C4, F4, C4, D4, Bb4, D4, Bb4, Eb4, Bb4, Eb4, Bb4,
          Ab4, Ab4, Ab4, Ab4, Ab4, Ab4, Bb5, Ab4, G4, Ab4,

          G4, X, Eb5, D5, X,
          Bb5, C5, A5, Bb5, X,
          G4, Ab4,  G4, X,
          Eb4, F4, D4, F4,
          Eb5, Eb5, Eb5, Eb5, Eb5,
          Eb5, D5, C5, Bb5,

          A5, F4, F4, F4, F4, F4, G4, F4, E4, F4,
          Db5, Db5, Db5, Db5, Bb5,
          A5, F4, F4, F4, F4, F4, G4, F4, E4, F4,
          Db5, Db5, Db5, Db5, Bb5,
          A5, F4, F4, F4, F4, F4, G4, F4, E4, F4,
          G4,
          A5, Bb5, B5, C5, Db5, D5, Eb5,
          C5, C5, C5, C5, C5, C5, D5, C5, Bb5, C5,
          D5, X, X,
          Bb5, Bb5, Bb5, Bb5, Bb5, Bb5, C5, Bb5, A5, Bb5,
          C5, X, X,
          #cadence
          D4, Bb5, A5, G4, F4, E4, G4, F4,
          F4, Eb5, C5, A5, F4, Eb4, C5, Eb4,
          D4, Bb5, A5, G4, F4, E4, G4, F4,
          F4, Eb5, C5, A5, F4, Eb4, C5, Eb4,
          D5, D5, D5, D5, D5, D5, Eb5, D5, C5, D5,
          Eb5, X, Fsh4, G4, X,
          D5, X, E4, F4, X,
          C5, X, D4, Eb4, X,
          Eb3, G4, Bb3, F4,
          C3, Eb4, C3, C4,
X, Bb5, A5, G4, F4, E4, G4, F4,
          F4, Eb5, C5, A5, F4, Eb4, C5, Eb4,
          D4, Bb5, A5, G4, F4, E4, G4, F4,
          F4, Eb5, C5, A5, F4, Eb4, C5, Eb4,
          D5, D5, D5, D5, D5, D5, Eb5, D5, C5, D5,
          Eb5, X, Fsh4, G4, X,
          D5, X, E4, F4, X,
          C5, X, D4, Eb4, X,
          Eb3, G4, Bb3, F4,
          C3, Eb4, C3, C4,

          #finale
          Bb5, F4, Bb5, F4, B5, F4, B5, F4, C5, F4, C5, F4, A5, F4, A5, F4,
          Bb5, F4, Bb5, F4, B5, F4, B5, F4, C5, F4, C5, F4, A5, F4, A5, F4,
          Bb5, F4, Bb5, F4, B5, F4, B5, F4, C5, F4, C5, F4, A5, F4, A5, F4,
          Bb5, F4, Bb5, F4, B5, F4, B5, F4, C5, F4, C5, F4, A5, F4, A5, F4,
          Bb5, F4, Bb5, F4, B5, F4, B5, F4, C5, F4, C5, F4, A5, F4, A5, F4,
          Bb5, F4, Bb5, F4, B5, F4, B5, F4, C5, F4, C5, F4, A5, F4, A5, F4,
          F5, X, F5, X, F5, X, F5, X, Eb5, X, Eb5, X, Eb5, X, Eb5, X,
          D5, X, D5, X, D5, X, D5, X, C5, X, C5, X, C5, X, C5, X,
          Bb5, D5, X, Bb5,
          X, F4, X, D4,
          Bb4, Bb5, Bb4, Bb5, Bb4, F4, F3, F4, F3, D4, D3, D4, D3,
          Bb4, Bb5, Bb4, Bb4,
          Bb4, X,
Bb4, X, Bb4,
          X, Bb4, X,
Bb4, X, Bb4,
          X, Bb4, X,
Bb4, X, Bb4,
          X, Bb4, X,

          Bb4, Bb4, Bb4, Bb4, Bb4, Bb4, C4, Bb4, A4, Bb4,
          X, X,
          X, Gb4, F4, E4,
          F4,
          F4, Eb4, Eb4, Eb4, Eb4, Eb4, Eb4, Eb4,
          Eb4, D4, Ab4, G4, F4,
          Eb4, X, C4,




          ]




len_1 = [16,
         24,
         4, 4, 16,
         24,
         4, 4, 16,
         24,
         2, 2, 2,
         8, 16, 8,
         10, 2, 2, 2, 8, 8,
         8, 16, 8,
         10, 2, 2, 2, 8, 8,

         8, 6, 2, 8, 6, 2,
         16, 8, 8,
8, 6, 2, 8, 6, 2,
         16, 8, 8,
8, 6, 2, 8, 6, 2,
         16, 8, 8,
         16, 8, 8,
         16, 16,



    4, 4, 8,
         16,
         16,
         16,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 8, 4,
         4, 8, 4,
         6, 2, 2, 2, 2, 2,

         4, 4, 12,
         2, 2, 2, 2, 2, 2,
         2, 2, 8, 4,
         4, 8, 4,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,

         4, 4, 4, 4,
         6, 2, 8,
         2, 2, 2, 1, 1, 2, 2, 2, 2,
         2, 2, 2, 1, 1, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         4, 4, 12, 2, 2, 2, 2, 2, 2,

         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,

         2, 2, 8, 2, 2,
         4, 4, 4, 2, 2,
         4, 8, 2, 2,
7, 1, 7, 1,
         2, 4, 4, 4, 2,
         4, 4, 4, 4,

         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 4, 4, 4, 2,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 4, 4, 4, 2,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         18,
         2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         4, 4, 8,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         4, 4, 8,
#cadence
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 8, 2, 2,
         2, 2, 8, 2, 2,
         2, 2, 8, 2, 2,
         4, 4, 4, 4,
         4, 4, 4, 4,
2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 8, 2, 2,
         2, 2, 8, 2, 2,
         2, 2, 8, 2, 2,
         4, 4, 4, 4,
         4, 4, 4, 4,
         #finale
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         4, 4, 4, 4,
         4, 4, 4, 4,
         4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         4, 4, 6, 6,
         20, 24,
4, 4, 16,
         4, 24, 24,
4, 4, 16,
         4, 24, 24,
4, 4, 16,
         4, 24, 24,

         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         4, 16,
         4, 4, 4, 4,
         12,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 4, 4, 4, 2,
         4, 4, 8,
         ]

notes2 = [Eb4,
          X,
          Eb4, X, Eb4,
          X,
          Bb5, X,  Bb5,
          X, X, #rest 6 for second
          X, Eb3, Eb3,
          Eb3, Eb3, Eb3,
Eb3, Eb3,
Eb3, Eb3, Eb3,
Eb3, Eb3, Eb3,
Eb3, Eb3, Eb3, Eb3,
Eb3, Eb3,
Eb3, Eb3, Eb3, Eb3,
Eb3, Eb3,
          D3, F3, F3,
          Gb3, Gb3, Eb4,
          X, D3,

          Eb3, Eb3, Eb3, Eb3, Eb3, Eb3, Eb3, F3, Eb3, D3, Eb3,
          Bb4, Bb4, Bb4, Bb4, Bb4, Bb4, C4, Bb4, A4, Bb4,
          G3, G3, C4, C4, F3, F3, Bb4, Bb4,
          G3, G3, C4, C4, F3, F3, Bb4, Bb4,
          G3, Ab3, G3, F3, Eb3, F3, Eb3, D3,
          C3, D3, Eb3, F3, Fsh3, G3, Ab3, A4,
          Bb4, X, Bb4, A4,
          X, Bb4, A4,
          Bb4, Bb4, G4, G4, C4, C4, F4, F4,
          D4, D4, F4, F4, Bb4, Bb4, Eb4, Eb4,
          Eb4, D4, C4, Bb4, Ab3, G3, F3,

          Eb3, G3, G3,
          F3, Eb3, D3,
          Eb3, X, G3, F3, G3, Ab3, Ab3, F3, F3,
          Bb4, Bb4, G3, F3, G3, Ab3, Ab3, F3, F3,
          G3, G3, A4, A4,A4, A4, Bb4, Bb4,
          Bb4, Bb4, F3, F3, Eb3, Eb3, F3, Eb3,

          D3, F3, Bb4,
          A4, G3, F3, Eb3, D3, C3,
          Bb3, X, Bb4, A4,
          X, Bb4, A4,
          Bb4, Bb4, Db4, Db4, A4, A4, B4, B4,
          G3, G3, C4, C4, Bb4, Bb4, Bb4, Bb4,
          G3, G2, G3, G2, G3, G2, G3, G2,
          Bb3, F3, Bb3, F3, Bb3, F3, Bb3, F3,
          Eb4, X, G4,
          F4, Eb4, D4, F4, Eb4, D4,
          X, C4, C4, C4, C4, Bb4, Bb4,
          X, Ab3, Ab3, A4, A4, G3, G3,
          X, F3, F3, F3, F3, G3, G3,
          C4, Eb4, C4, Eb4, C4, Eb4, C4, Eb4, D4, F4, D4, F4, Bb5, Ab4, G4, Ab4,

          Eb4, X, G4, F4, Bb5,
          G4, Eb4, D4, G4,
          Eb4, F4, Bb4, Eb4,

          C4, Bb4,
          A5, A5, A5, A5, A5,
          A5, Bb5, G4, D4,
          F4, X, X,
          G4, G4, G4, G4, E4,
          F4, X, X,
          G4, G4, G4, G4, E4,
          C5, X, X, X,
          D5, D5, D5, D5, D5, D5, Eb5, D5, C5, D5,
          Eb5,
          F4,
          G4, Ab4, A5, Bb5, C5, Db5, D5,
          Eb4,
          F4, G4, A5, Bb5, B5, C5, Eb4,
          #cadence
          X,
          F4, F4, F4, F4, F4, F4, F4, X,
          Fsh4, X, Eb4, Bb4, X,
          Bb5, X, Db4, A4, X,
          Ab4, X, F3, G4, X,
          G2, Eb4, F2, D4,
          G2, C4, A3, A4,
          X,
          F4, F4, F4, F4, F4, F4, F4, X,
          Fsh4, X, Eb4, Bb4, X,
          Bb5, X, Db4, A4, X,
          Ab4, X, F3, G4, X,
          G2, Eb4, F2, D4,
          G2, C4, A3, A4,
          #finale
          D3, F3, D3, F3, Eb3, F3, Eb3, F3,
D3, F3, D3, F3, Eb3, F3, Eb3, F3,
D3, F3, D3, F3, Eb3, F3, Eb3, F3,
D3, F3, D3, F3, Eb3, F3, Eb3, F3,
D2, F2, D2, F2, Eb2, F2, Eb2, F2,
D2, F2, D2, F2, Eb2, F2, Eb2, F2,
          Bb5, F4, Bb5, F4, Bb5, F4, Bb5, F4, C5, G4, C5, G4, C5, G4, C5, G4,
          Bb5, F4, Bb5, F4, Bb5, F4, Bb5, F4, A5, F4, A5, F4, A5, F4, A5, F4,
          Bb4, Bb4, X, F4,
          X, D4, X, Bb4,
          F4, X,
          Bb3, D4, Bb3, Bb3,
          Bb3, X,
          D3, X, D3,
          X, D3, X,
D4, X, D4,
          X, D4, X,
D4, X, D4,
          X, D4, X,

          X, X,
          F4, F4, F4, F4, F4, F4, Gb4, F4, E4, F4,
          Db4, X, X, Db4,
          C4, Eb4, Db4, C4,
          B4, C4, C4, C4, C4, C4, C4, C4,
          C4, B4, B4, C4, B4,
          C4, X, Eb3,
          ]

len_2 = [16,
         24,
         4, 4, 16,
         24,
         4, 4, 16,
         24, 6,
         8, 16, 8,
         8, 16, 16,
         16, 8,
         8, 16, 8,
         8, 16, 12,
         8, 8, 8, 12,
         16, 12,
         8, 8, 8, 12,
         16, 8,
         8, 16, 8,
         8, 8, 16,
         16, 8, 8,



    2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 8, 4,
         4, 8, 4,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         4, 2, 2, 2, 2, 2, 2,

         4, 8, 4,
         6, 2, 8,
         2, 2, 2, 1, 1, 2, 2, 2, 2,
         2, 2, 2, 1, 1, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,

         4, 4, 12,
         2, 2, 2, 2, 2, 2,
         2, 2, 8, 4,
         4, 8, 4,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         4, 4, 8, 6, 2, 2, 2, 2, 2,
         4, 2, 2, 2, 2, 2, 2,
         4, 2, 2, 2, 2, 2, 2,
         4, 2, 2, 2, 2, 2, 2,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,

         2, 2, 4, 4, 4,
         4, 4, 4, 4,
         4, 4, 4, 4,
         8, 8,
         2, 4, 4, 4, 2,
         4, 4, 4, 4,
         2, 6, 8,
         2, 4, 4, 4, 2,
         2, 6, 8,
         2, 4, 4, 4, 2,
         2, 2, 4, 8,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         16,
         18,
         2, 2, 2, 2, 2, 2, 2,
         18,
         2, 2, 2, 2, 2, 2, 2,
         #cadence
         64,
         2, 2, 2, 2, 2, 2, 1, 3,
         2, 2, 8, 2, 2,
         2, 2, 8, 2, 2,
         2, 2, 8, 2, 2,

         4, 4, 4, 4,
         4, 4, 4, 4,
64,
         2, 2, 2, 2, 2, 2, 1, 3,
         2, 2, 8, 2, 2,
         2, 2, 8, 2, 2,
         2, 2, 8, 2, 2,

         4, 4, 4, 4,
         4, 4, 4, 4,
         #finale
2, 2, 2, 2, 2, 2, 2, 2,
2, 2, 2, 2, 2, 2, 2, 2,
2, 2, 2, 2, 2, 2, 2, 2,
2, 2, 2, 2, 2, 2, 2, 2,
2, 2, 2, 2, 2, 2, 2, 2,
2, 2, 2, 2, 2, 2, 2, 2,
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         4, 4, 4, 4,
         4, 4, 4, 4,
         4, 12,
         4, 4, 6, 6,
         20, 24,
4, 4, 16,
         4, 24, 24,
4, 4, 16,
         4, 24, 24,
4, 4, 16,
         4, 24, 24,

         16,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 4, 4, 4,
         4, 4, 4, 4,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 4, 4, 4, 2,
         4, 4, 8,

         ]

notes3 = [Eb2,
          X,
          G2, X, G2,
          X,
          G1, X,  G1,
          X, X, #6 rest
          X, C3, C3,
          C3, C3, C3,
          Db3, Db3, Db3,
          Db3, Db3, Db3,
          X,
          X, Db3,
          X,
          X, D3, D3,
          Eb3, Eb3, X, C3,
          Eb3, X, Bb3, X,




          G2, X, X,
          X,

          Eb2, Eb2, Eb2, Eb2, Eb2, Eb2, F2, Eb2, D2, Eb2,
          Bb3, Bb3, Bb3, Bb3, Bb3, Bb3, C3, Bb3, A3, Bb3,
          G2, G2, C3, C3, F2, F2, Bb3, Bb3,
          G2, G2, C3, C3, F2, F2, Bb3, Bb3,
          Eb2, Eb2, F2, F2, D2, D2, G2, G2,
          Eb2, X, Bb3, A3,

          X,
          Bb3, Bb4, Bb3, Bb4, E3, Bb4, E3, Bb4, F3, A4, F3, A4, D3, Ab3, D3, Ab3,
          Eb3, G3, Eb3, G3, A3, Gb3, A3, Gb3, Bb3, F3, Bb3, F3, Bb3, Ab3, Bb3, Ab3,
          Bb3, X, Eb3,
          D3, C3, Bb3, Ab2, G2, F2,
          Eb2, Eb2, Eb2, Eb2, Eb2, Eb2,  F2, Eb2, D2, Eb2,
          Bb3, Bb3, Bb3, Bb3, Bb3, Bb3, C3, Bb3, A3, Bb3,
          Eb3, X, Eb3, D3, X,
          X, C3, Bb3, X,
          X, Ab3, G2, X,
          F2, F2, F2, F2, Bb2, Bb2, Bb2, Bb2,

          Eb2, Eb2, C3, C3, A3, A3, Bb3, Bb3,
          Eb2, Eb2, Ab2, Ab2, Fsh2, Fsh2, G2, G2,
          C2, C2, F2, F2, D2, D2, Eb2, Eb2,
          A2, Bb2,
          C2, C2, C2, C2, C2, C2, C2, C2,
          C2, D2, Eb2, E2,
          C3, X, X,
          E4, E4, E4, E4, Db4,
          C3, X, X,
          E4, E4, E4, E4, Db4,
          F3, X, X,
          F4, X, F4, X,
          Eb4, X, X,
          Eb4, X, Eb4, X,
          D4, X, X,
          D4, X, D4, X,
          C4, X, A3, X,

          #cadence
          D3, D3, D3, D3, D3, D3, Eb3, D3, C3, D3,
          Eb3, C4, C4, C4, C4, C4,  D4, C4, Bb4, C4,
          D3, D3, D3, D3, D3, D3, Eb3, D3, C3, D3,
          Eb3, C4, C4, C4, C4, C4,  D4, C4, Bb4, C4,
          D4, Bb3, Bb3, Bb3, Bb3, Bb3,  X,
          A3, X, C3, Bb3, X,
          G2, X, Bb3, A3, X,
          F2, X, Ab2, G2, X,
          Eb2, Bb4, D2, Bb4,
          Eb2, G3, F2, F3,
D3, D3, D3, D3, D3, D3, Eb3, D3, C3, D3,
          Eb3, C4, C4, C4, C4, C4,  D4, C4, Bb4, C4,
          D3, D3, D3, D3, D3, D3, Eb3, D3, C3, D3,
          Eb3, C4, C4, C4, C4, C4,  D4, C4, Bb4, C4,
          D4, Bb3, Bb3, Bb3, Bb3, Bb3,  X,
          A3, X, C3, Bb3, X,
          G2, X, Bb3, A3, X,
          F2, X, Ab2, G2, X,
          Eb2, Bb4, D2, Bb4,
          Eb2, G3, F2, F3,
          #finale
          X,
          Bb4, B4, C4, A4,
Bb4, B4, C4, A4,
          D3, D3, Eb3, Eb3,
D3, D3, Eb3, Eb3,
          D3, D3, D3, D3, Eb3, Eb3, Eb3, Eb3,
          F3, F3, F3, F3, F2, F2, F2, F2,
          Bb3, F4, Bb3, D4,
          Bb3, Bb4, Bb3, F3,
          D3, Bb3, F2, D2,
          Bb2, Bb3, Bb2, Bb2,
          Bb2, X,
Bb1, X, Bb1,
          X, Bb1, X,
Bb1, X, Bb1,
          X, Bb1, X,
Bb1, X, Bb1,
          X, Bb2, X,


          ]
len_3 = [16,
         24,
         4, 4, 16,
         24,
         4, 4, 16,
         24, 6,
         8, 16, 8,
         8, 16, 8,
         8, 16, 8,
8, 16, 8,
         96,
         24, 8,
         32,
         8, 16, 8,
         8, 8, 8, 8,
         8, 8, 8, 8,



    4, 4, 8,
         160,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 8, 4,

         64,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         4, 4, 12,
         2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 8, 2, 2,
         4, 8, 2, 2,
         4, 8, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,

         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         8, 8,
         2, 2, 2, 2, 2, 2, 2, 2,
         4, 4, 4, 4,
         2, 6, 8,
         2, 4, 4, 4, 2,
         2, 6, 8,
         2, 4, 4, 4, 2,
         4, 4, 8,
         4, 4, 4, 4,
         4, 4, 8,
         4, 4, 4, 4,
         4, 4, 8,
         4, 4, 4, 4,
         4, 4, 4, 4,
         #cadence
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
2, 2, 2, 2, 2, 2, 4,
         2, 2, 8, 2, 2,
         2, 2, 8, 2, 2,
         2, 2, 8, 2, 2,
         4, 4, 4, 4,
         4, 4, 4, 4,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 4,
         2, 2, 8, 2, 2,
         2, 2, 8, 2, 2,
         2, 2, 8, 2, 2,
         4, 4, 4, 4,
         4, 4, 4, 4,
         #Finale
         32,
         4, 4, 4, 4,
4, 4, 4, 4,
4, 4, 4, 4,
4, 4, 4, 4,
         2, 2, 2, 2, 2, 2, 2, 2,
2, 2, 2, 2, 2, 2, 2, 2,
4, 4, 4, 4,
         4, 4, 4, 4,
         4, 4, 4, 4,
         4, 4, 6, 6,
         20, 24,
4, 4, 16,
         4, 24, 24,
4, 4, 16,
         4, 24, 24,
4, 4, 16,
         4, 24, 24,
         ]

notes4 = [Eb1,
          X,
          C2, X, C2,
          X,
          Eb2, X,  Eb2,
          X, X,
          Ab1, C2, Eb2, C2,
          Ab1,
          Bb2, Db2, G2, Db2,
          Bb2, Bb3,
          C3, X, C3, Bb3, X, Bb3,
          Ab2, X, Bb3,
          C3, X, C3, Bb3, X, Bb3,
          A3, X, Bb3,
          C3, X, C3, B3, X, B3,
          Bb3, Bb2, Bb3,
          A3, Eb2, Gb3,
          F3, F3, Bb2, Ab2,



    Eb2, X, X,
          X,

          Bb2, Bb2, Bb2, Bb2, Bb2, Bb2, C2, Bb2, A2, Bb2,
          F2, F2, F2, F2, F2, F2, G2, F2, E2, F2,
          D2, D2, G2, G2, C2, C2, F2, F2,
          D2, D2, G2, G2, C2, C2, F2, F2,
          Bb2,
          Bb3, X, Bb2,
          Eb2, X, Eb2,
          D2, C2, Bb2, Ab1, G1, F1,
          Eb1,
          Bb2,
          Eb2, X, Eb2, D2, X,
          X, C2, Bb2, X,
          X, Ab2, G1, X,
          F1, Bb1,

          Eb1, Eb1, C2, C2, A2, A2, Bb2, Bb2,
          Eb1, Eb1, Ab1, Ab1, Fsh1, Fsh1, G1, G1,
          C1, C1, F1, F1, D1, D1, Eb1, Eb1,
          A1, Bb1,
          C1, C1, C1, C1, C1, C1, C1, C1,
          C1, D1, Eb1, E1,
          F1, X, X,
          F1, F1, F1, F1, F1, F1, F1, F1,
          F1, X, X,
          F1, F1, F1, F1, F1, F1, F1, F1,
          F1, X, X,
          B4, B4, B4, B4, B4, B4, C4, B4, A4, B4,
          C4, X, X,
          A4, A4, A4, A4, A4, A4, Bb4, A4, G3, A4,
          Bb4, X, X,
          G3, G3, G3, G3, G3, G3, A4, G3, F4, G3,
          A4, X, C3, X,
          #cadence
          Bb3, Bb3, Bb3, Bb3, Bb3, Bb3, C3, Bb3, A3, Bb3,
          C3, A4, A4, A4, A4, A4, Bb4, A4, G3, A4,
          Bb3, Bb3, Bb3, Bb3, Bb3, Bb3, C3, Bb3, A3, Bb3,
          C3, A4, A4, A4, A4, A4, Bb4, A4, G3, A4,
          Bb4, Bb2, Bb2, Bb2, Bb2, Bb2,  C2, Bb2, A2, Bb2,
          A2, X, C2, Bb2, X,
          G1, X, Bb2, A2, X,
          F1, X, Ab1, G1, X,
          Eb1, G3, Bb2, F3,
          Eb1, G2, F1, F2,
Bb3, Bb3, Bb3, Bb3, Bb3, Bb3, C3, Bb3, A3, Bb3,
          C3, A4, A4, A4, A4, A4, Bb4, A4, G3, A4,
          Bb3, Bb3, Bb3, Bb3, Bb3, Bb3, C3, Bb3, A3, Bb3,
          C3, A4, A4, A4, A4, A4, Bb4, A4, G3, A4,
          Bb4, Bb2, Bb2, Bb2, Bb2, Bb2,  C2, Bb2, A2, Bb2,
          A2, X, C2, Bb2, X,
          G1, X, Bb2, A2, X,
          F1, X, Ab1, G1, X,
          Eb1, G3, Bb2, F3,
          Eb1, G2, F1, F2,
          #finale
          X,
          F5, F5, F5, F5, F5, F5, F5, F5,
F5, F5, F5, F5, F5, F5, F5, F5,
          D2, D2, D2, D2, Eb2, Eb2, Eb2, Eb2,
          F2, F2, F2, F2, F1, F1, F1, F1,
          Bb2, D4, Bb2, Bb4,
          Bb2, F3, Bb2, D3,
          Bb3, Bb2, F1, D1,
          Bb1, Bb2, Bb1, Bb1,
          Bb1, X,
          Bb2, X, Bb2,
          X, Bb2, X,
Bb2, X, Bb2,
          X, Bb2, X,
Bb2, X, Bb2,
          X, Bb2, X,

          ]
len_4 = [16,
         24,
         4, 4, 16,
         24,
         4, 4, 16,
         24, 6,
         14, 2, 14, 2,
         32,
         14, 2, 14, 2,
         24, 8,
         8, 6, 2, 8, 6, 2,
         16, 8, 8,
8, 6, 2, 8, 6, 2,
         16, 8, 8,
8, 6, 2, 8, 6, 2,
         8, 16, 8,
         8, 16, 8,
         8, 8, 8, 8,



    4, 4, 8,
         256,

         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         16,
         4, 4, 8,
         4, 4, 12, 2, 2, 2, 2, 2, 2,
         16,
         16,
         2, 2, 8, 2, 2,
         4, 8, 2, 2,
         4, 8, 2, 2,
         8, 8,

         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         8, 8,
         2, 2, 2, 2, 2, 2, 2, 2,
         4, 4, 4, 4,
         4, 4, 8,
         2, 2, 2, 2, 2, 2, 2, 2,
         4, 4, 8,
         2, 2, 2, 2, 2, 2, 2, 2,
         4, 4, 8,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         4, 4, 8,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         4, 4, 8,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         4, 4, 4, 4,
         #cadence
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 8, 2, 2,
         2, 2, 8, 2, 2,
         2, 2, 8, 2, 2,
         4, 4, 4, 4,
         4, 4, 4, 4,
2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
2, 2, 2, 2, 2, 2, 1, 1, 1, 1,
         2, 2, 8, 2, 2,
         2, 2, 8, 2, 2,
         2, 2, 8, 2, 2,
         4, 4, 4, 4,
         4, 4, 4, 4,
         #finale
         64,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 2, 2, 2,
4, 4, 4, 4,
4, 4, 4, 4,
         4, 4, 4, 4,
         4, 4, 6, 6,
         20, 24,
         4, 4, 16,
         4, 24, 24,
4, 4, 16,
         4, 24, 24,
4, 4, 16,
         4, 24, 24,
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

lit_voice_col_1 = [255, 0, 0]
lit_voice_col_2 = [255, 100, 0]
lit_voice_col_3 = [255,150,0]
lit_voice_col_4 = [255,225,0]

background_col = black

original_outline_1 = 1
original_outline_2 = 1
original_outline_3 = 1
original_outline_4 = 1

outline_1 = original_outline_1
outline_2 = original_outline_2
outline_3 = original_outline_3
outline_4 = original_outline_4


instrument_1 = 3
instrument_2 = 2
instrument_3 = 1
instrument_4 = 1


appear_1 = False
appear_2 = False
appear_3 = False
appear_4 = False


fill_1 = True
fill_2 = True
fill_3 = True
fill_4 = True


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


def setup():
    for i in range(0, len(len_1)):
        state_list_1.append(False)
    for i in range(0, len(len_2)):
        state_list_2.append(False)
    for i in range(0, len(len_3)):
        state_list_3.append(False)
    for i in range(0, len(len_4)):
        state_list_4.append(False)

scale_x = 10
scale_y = 10
y_stretch = 10
speed = 2

setup()

shape_1 = 0
shape_2 = 0
shape_3 = 0
shape_4 = 0


font1 = pygame.font.SysFont('times new roman', 20,)
font2 = pygame.font.SysFont('times new roman', 20, False, True)

label1 = font1.render("Wolfgang Amadeus Mozart", 1, white)
label2 = font2.render("Overture to the opera'The magic Flute', Die Zauberflöte, K.620", 1, white)



while not quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True

    window.fill(background_col)
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
                player.note_on(notes3[i][1], 120)
                player.note_on(notes3[i][1] - 12, 120)

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
                player.note_off(notes3[i][1] - 12, 100)

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
                player.note_on(notes4[i][1], 120)
                player.note_on(notes4[i][1] - 12, 120)

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
                player.note_off(notes4[i][1] - 12, 100)

                state_list_4[i] = False

        if shape_4 == 0:
            pygame.draw.rect(window, voice_col_4, (x, y_pos, play_time, y_stretch), outline_4)
        elif shape_4 == 1:
            pygame.draw.circle(window, voice_col_4, (int(x) + int(play_time / 2), int(y_pos)), int(play_time / 2),
                               outline_4)

        x += len_4[i] * scale_x

    x = default - speed
    default = x
    #pygame.draw.line(window, red, (0, y_0), (w, y_0))
    #pygame.draw.line(window, white, (play_pos_x, 50), (play_pos_x, l - 50),)



    pygame.display.update() # refresh your display
    clock.tick(60) # wait a certain amount of time that
# ensures a frame rate of 60 fps

pygame.quit() # shutdown module
