import pygame
import random
import math
from pygame.constants import K_LEFT, K_RIGHT
#
pygame.init()
# create the screen
screen = pygame.display.set_mode((800, 600))
# 800 is weight and 600 is height
# background
background = pygame.image.load("background.png")
# Title  and Icon
pygame.display.set_caption("arcade_space")
icon = pygame.image.load("penguin.png")
pygame.display.set_icon(icon)

# player:
player_image = pygame.image.load('rc-plane.png')
playerX = 370
playerY = 480
player_changeX = 0
player_changeY = 0


def player(x, y):
    screen.blit(player_image, (x, y))


# enemy:
enemy_image = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemy = 6
for i in range(number_of_enemy):
    enemy_image.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(30)


def enemy(x, y, i):
    screen.blit(enemy_image[i], (x+16, y+10))


# bullet
bullet_image = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"


def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (x, y))

# Collision :va cham


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX-bulletX)**2+(enemyY-bulletY)**2)
    if distance < 40:
        return True
    else:
        return False


# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)


textX = 10
textY = 10


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


# over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def chech_over(playerX, playerY, enemyX, enemyY):
    distance_over = math.sqrt((playerX-enemyX)**2+(playerY-enemyY)**2)
    if(distance_over < 20):
        return True
    else:
        return False


def show_over():
    over = over_font.render("Game Over", True, (255, 255, 255))
    screen.blit(over, (200, 250))


def over():
    for j in range(number_of_enemy):
        enemyY[j] = 2000
        show_over()


# cotrol game
running = True
while running:
    # background
    screen.blit(background, (0, 0))
    # screen.fill((0,0,0))
    for event in pygame.event.get():
        # when using close button
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_changeX = -5
            if event.key == pygame.K_RIGHT:
                player_changeX = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    bulletY = playerY
                    bullet(bulletX, bulletY)
            if event.key == pygame.K_DOWN:
                player_changeY = 5
            if event.key == pygame.K_UP:
                player_changeY = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_changeX = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player_changeY = 0

    # rgb :red,green, blue(max=255)
    # checking for boundlaries of spaceship so it does not go out the bound
    playerX += player_changeX
    playerY += player_changeY
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    if playerY <= 0:
        playerY = 480
    if playerY >= 480:
        playerY = 480
    # enemy moving
    for i in range(number_of_enemy):
        if chech_over(playerX, playerY, enemyX[i], enemyY[i]):
            over()
            playerY = 2000
            break

        elif enemyY[i] > 400:
            over()
            break
        enemyX[i] = enemyX[i] + enemyX_change[i]
        # enemyY_change=random .randint(10,40)
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        enemy(enemyX[i], enemyY[i], i)
        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)

#    bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    show_score(textX, textY)
    player(playerX, playerY)
    pygame.display.update()
