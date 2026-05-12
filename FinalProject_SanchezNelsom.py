# Nelson Sanchez
# CTI-110-0001
# 5/11/2026
# Final Project 
# Tank Duel a game of tanks were the user controls the tanks cannon up or down to kill the enemy.

 
"""
Tank Duel Game
---------------
A simple 2-player artillery game using Pygame.

Features:
- Player name input
- Red vs Blue tanks
- Adjustable cannon elevation
- Projectile physics
- Explosion effects
- Hit sound effects
- Game ends when a tank is destroyed

Controls
--------
Player 1 (Red):
    A / D = Aim cannon down/up
    SPACE = Fire

Player 2 (Blue):
    LEFT / RIGHT = Aim cannon down/up
    ENTER = Fire

Install:
    pip install pygame

Optional:
    Add a file named "hit.wav" in the same folder for hit sounds.
"""

import math
import os
import pygame
import sys

# ---------------------------
# INITIALIZE
# ---------------------------
pygame.init()
pygame.mixer.init()

WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tank Duel")

clock = pygame.time.Clock()

# ---------------------------
# COLORS
# ---------------------------
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
GREEN = (50, 180, 50)
RED = (220, 50, 50)
BLUE = (50, 100, 255)
YELLOW = (255, 220, 0)
ORANGE = (255, 140, 0)
GRAY = (90, 90, 90)

GROUND_Y = HEIGHT - 100

# ---------------------------
# SOUND
# ---------------------------
hit_sound = None
if os.path.exists("hit.wav"):
    try:
        hit_sound = pygame.mixer.Sound("hit.wav")
    except:
        hit_sound = None

# ---------------------------
# FONTS
# ---------------------------
font = pygame.font.SysFont("arial", 24)
big_font = pygame.font.SysFont("arial", 42)

# ---------------------------
# PLAYER NAME INPUT
# ---------------------------
def get_player_name():
    name = ""
    active = True

    while active:
        screen.fill(BLACK)

        title = big_font.render("Enter Your Name:", True, WHITE)
        txt = big_font.render(name, True, YELLOW)

        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 200))
        screen.blit(txt, (WIDTH // 2 - txt.get_width() // 2, 300))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and len(name) > 0:
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    if len(name) < 15:
                        name += event.unicode

    return name

player1_name = get_player_name()
player2_name = "Computer"

# ---------------------------
# TANK CLASS
# ---------------------------
class Tank:
    def __init__(self, x, y, color, angle):
        self.x = x
        self.y = y
        self.color = color
        self.angle = angle
        self.health = 100
        self.width = 60
        self.height = 30
        self.alive = True

    def draw(self):
        # body
        pygame.draw.rect(
            screen,
            self.color,
            (self.x, self.y, self.width, self.height)
        )

        # wheels
        for i in range(4):
            pygame.draw.circle(
                screen,
                BLACK,
                (self.x + 10 + i * 15, self.y + self.height),
                7
            )

        # turret
        end_x = self.x + self.width // 2 + math.cos(math.radians(self.angle)) * 45
        end_y = self.y + 10 - math.sin(math.radians(self.angle)) * 45

        pygame.draw.line(
            screen,
            GRAY,
            (self.x + self.width // 2, self.y + 10),
            (end_x, end_y),
            6
        )

    def get_barrel_end(self):
        end_x = self.x + self.width // 2 + math.cos(math.radians(self.angle)) * 45
        end_y = self.y + 10 - math.sin(math.radians(self.angle)) * 45
        return end_x, end_y

# ---------------------------
# PROJECTILE CLASS
# ---------------------------
class Projectile:
    def __init__(self, x, y, angle, power, color):
        self.x = x
        self.y = y
        self.radius = 6
        self.color = color

        self.vel_x = math.cos(math.radians(angle)) * power
        self.vel_y = -math.sin(math.radians(angle)) * power

        self.active = True

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y

        self.vel_y += 0.25  # gravity

        if self.y > GROUND_Y or self.x < 0 or self.x > WIDTH:
            self.active = False

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# ---------------------------
# EXPLOSION
# ---------------------------
def explosion(x, y):
    for radius in range(10, 50, 5):
        pygame.draw.circle(screen, ORANGE, (x, y), radius)
        pygame.display.update()
        pygame.time.delay(20)

# ---------------------------
# DRAW UI
# ---------------------------
def draw_ui(current_player):
    p1_text = font.render(
        f"{player1_name} Angle: {int(red_tank.angle)}",
        True,
        WHITE
    )

    p2_text = font.render(
        f"{player2_name} Angle: {int(blue_tank.angle)}",
        True,
        WHITE
    )

    turn_text = font.render(
        f"Turn: {current_player}",
        True,
        YELLOW
    )

    screen.blit(p1_text, (20, 20))
    screen.blit(p2_text, (20, 55))
    screen.blit(turn_text, (WIDTH // 2 - 60, 20))

# ---------------------------
# GAME OBJECTS
# ---------------------------
red_tank = Tank(120, GROUND_Y - 30, RED, 45)
blue_tank = Tank(WIDTH - 180, GROUND_Y - 30, BLUE, 135)

projectiles = []

current_turn = 1
running = True
winner = None

def move_tanks_closer():
    move_amount = 20

    # move red tank right
    red_tank.x += move_amount

    # move blue tank left
    blue_tank.x -= move_amount

    # prevent overlap
    min_distance = 140

    if blue_tank.x - red_tank.x < min_distance:
        blue_tank.x = red_tank.x + min_distance

# ---------------------------
# MAIN LOOP
# ---------------------------
while running:
    clock.tick(60)

    screen.fill((120, 200, 255))

    # ground
    pygame.draw.rect(screen, GREEN, (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y))

    # draw tanks
    if red_tank.alive:
        red_tank.draw()

    if blue_tank.alive:
        blue_tank.draw()

    # UI
    current_name = player1_name if current_turn == 1 else player2_name
    draw_ui(current_name)

    # ---------------------------
    # EVENTS
    # ---------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # PLAYER 1 CONTROLS
            if current_turn == 1:
                if event.key == pygame.K_a:
                    red_tank.angle -= 2

                if event.key == pygame.K_d:
                    red_tank.angle += 2

                if event.key == pygame.K_SPACE:
                    x, y = red_tank.get_barrel_end()

                    projectiles.append(
                        Projectile(x, y, red_tank.angle, 10, RED)
                    )

                    move_tanks_closer()
                    
                    current_turn = 2

            # PLAYER 2 CONTROLS
            else:
                if event.key == pygame.K_LEFT:
                    blue_tank.angle += 2

                if event.key == pygame.K_RIGHT:
                    blue_tank.angle -= 2

                if event.key == pygame.K_RETURN:
                    x, y = blue_tank.get_barrel_end()

                    projectiles.append(
                        Projectile(x, y, blue_tank.angle, 10, BLUE)

                    )

                    move_tanks_closer()

                    current_turn = 1

    # limit angles
    red_tank.angle = max(0, min(90, red_tank.angle))
    blue_tank.angle = max(90, min(180, blue_tank.angle))

    # ---------------------------
    # UPDATE PROJECTILES
    # ---------------------------
    for projectile in projectiles[:]:
        projectile.update()
        projectile.draw()

        # collision with red tank
        red_rect = pygame.Rect(
            red_tank.x,
            red_tank.y,
            red_tank.width,
            red_tank.height
        )

        # collision with blue tank
        blue_rect = pygame.Rect(
            blue_tank.x,
            blue_tank.y,
            blue_tank.width,
            blue_tank.height
        )

        if blue_rect.collidepoint(projectile.x, projectile.y):
            explosion(int(projectile.x), int(projectile.y))

            if hit_sound:
                hit_sound.play()

            blue_tank.alive = False
            winner = player1_name
            projectiles.remove(projectile)

        elif red_rect.collidepoint(projectile.x, projectile.y):
            explosion(int(projectile.x), int(projectile.y))

            if hit_sound:
                hit_sound.play()

            red_tank.alive = False
            winner = player2_name
            projectiles.remove(projectile)

        elif not projectile.active:
            projectiles.remove(projectile)

    # ---------------------------
    # GAME OVER
    # ---------------------------
    if winner:
        screen.fill(BLACK)

        text = big_font.render(f"{winner} Wins!", True, YELLOW)
        screen.blit(
            text,
            (WIDTH // 2 - text.get_width() // 2,
             HEIGHT // 2 - text.get_height() // 2)
        )

        pygame.display.flip()
        pygame.time.delay(5000)

        running = False

    pygame.display.flip()

pygame.quit()
sys.exit()

