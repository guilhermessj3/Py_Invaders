import pygame
import random

from pygame import mixer


class PLAYER:
    def __init__(self):
        self.x = 400
        self.y = 480
        self.playerX_change = 0
        self.player_surf = pygame.image.load('player.png')
        self.player_rect = self.player_surf.get_rect(center=(self.x, self.y))

    def spawn(self):
        # Spawn player image
        screen.blit(self.player_surf, self.player_rect)


class ENEMY:
    def __init__(self):
        self.enemy_surf = []
        self.x = []
        self.y = []
        self.enemyX_change = []
        self.enemyY_change = []
        self.num_of_enemies = 6
        for i in range(self.num_of_enemies):
            self.enemy_surf.append(pygame.image.load('enemy.png'))
            self.x.append(random.randint(0, 736))
            self.y.append(random.randint(50, 150))
            self.enemyX_change.append(4)
            self.enemyY_change.append(40)

    def enemy_move(self):
        for i in range(self.num_of_enemies):

            # Game over
            if self.y[i] > 440:
                for j in range(self.num_of_enemies):
                    self.y[i] = 50

            self.x[i] += self.enemyX_change[i]
            if self.x[i] <= 0:
                self.enemyX_change[i] = 4
                self.y[i] += self.enemyY_change[i]
            elif self.x[i] > 736:
                self.enemyX_change[i] = -4
                self.y[i] += self.enemyY_change[i]

            screen.blit(self.enemy_surf[i], (self.x[i], self.y[i]))





# Start pygame module
pygame.init()

# Screen (Width and Height)
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

# Sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# Captions and Icon (Sets window icon and title)
pygame.display.set_caption('Py_Invader')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player instance
player = PLAYER()

# Enemy instance
enemy = ENEMY()

# Game loop
while True:
    for event in pygame.event.get():
        # Event Handler
        if event.type == pygame.QUIT:

            pygame.quit()
            quit()

    screen.blit(background, (0, 0))
    enemy.enemy_move()
    player.spawn()
    pygame.display.update()
