import pygame.midi
import time

pygame.midi.init()
player = pygame.midi.Output(0)
player.set_instrument(21)
player.note_on(60, 100)
player.note_on(66, 100)
time.sleep(2)
player.note_off(60, 100)
player.note_off(66, 100)

del player
pygame.midi.quit()