import pygame
import random

pygame.init()
screenWidth = 1300
screenHeight = 640
clock = pygame.time.Clock()
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("The Exploring DINO")
background = pygame.image.load('background.jpg')
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)

# SOUNDS
eat_sound = pygame.mixer.Sound("eat_sound.wav")
et_sound = pygame.mixer.Sound("ET_sound.wav")
hit_sound = pygame.mixer.Sound("hit_sound.wav")
died_sound = pygame.mixer.Sound("died_sound.wav")
bone_sound = pygame.mixer.Sound("bone_sound.wav")
coin_sound = pygame.mixer.Sound("coin_sound.wav")
egg_sound = pygame.mixer.Sound("egg_sound.wav")

# DINO SPRITES

walk_right = [pygame.image.load('walk (1).png'), pygame.image.load('walk (2).png'),
              pygame.image.load('walk (3).png'), pygame.image.load('walk (4).png'),
              pygame.image.load('walk (5).png'), pygame.image.load('walk (6).png'),
              pygame.image.load('walk (7).png'), pygame.image.load('walk (8).png'),
              pygame.image.load('walk (9).png'), pygame.image.load('walk (10).png')]

walk_left = [pygame.image.load('walk (1)L.png'), pygame.image.load('walk (2)L.png'),
             pygame.image.load('walk (3)L.png'), pygame.image.load('walk (4)L.png'),
             pygame.image.load('walk (5)L.png'), pygame.image.load('walk (6)L.png'),
             pygame.image.load('walk (7)L.png'), pygame.image.load('walk (8)L.png'),
             pygame.image.load('walk (9)L.png'), pygame.image.load('walk (10)L.png')]

dead_right = [pygame.image.load('Dead (1).png'), pygame.image.load('Dead (2).png'), pygame.image.load('Dead (3).png'),
              pygame.image.load('Dead (4).png'), pygame.image.load('Dead (5).png'), pygame.image.load('Dead (6).png'),
              pygame.image.load('Dead (7).png'), pygame.image.load('Dead (8).png')]

dead_left = [pygame.image.load('Dead (1)L.png'), pygame.image.load('Dead (2)L.png'), pygame.image.load('Dead (3)L.png'),
             pygame.image.load('Dead (4)L.png'), pygame.image.load('Dead (5)L.png'), pygame.image.load('Dead (6)L.png'),
             pygame.image.load('Dead (7)L.png'), pygame.image.load('Dead (8)L.png')]


# EASY TROLL SPRITES

ETR_walk = [pygame.image.load('ETR_walk0.png'), pygame.image.load('ETR_walk1.png'), pygame.image.load('ETR_walk2.png'),
            pygame.image.load('ETR_walk3.png'), pygame.image.load('ETR_walk4.png'), pygame.image.load('ETR_walk5.png'),
            pygame.image.load('ETR_walk6.png'), pygame.image.load('ETR_walk7.png'), pygame.image.load('ETR_walk8.png'),
            pygame.image.load('ETR_walk9.png')]

ETL_walk = []
for i in ETR_walk:
    j = pygame.transform.flip(i, True, False)
    ETL_walk.append(j)

ETR_attack = [pygame.image.load('ETR_attack0.png'), pygame.image.load('ETR_attack1.png'),
              pygame.image.load('ETR_attack2.png'), pygame.image.load('ETR_attack3.png'),
              pygame.image.load('ETR_attack4.png'), pygame.image.load('ETR_attack5.png'),
              pygame.image.load('ETR_attack6.png'), pygame.image.load('ETR_attack7.png'),
              pygame.image.load('ETR_attack8.png'), pygame.image.load('ETR_attack9.png')]

ETL_attack = []
for i in ETR_attack:
    j = pygame.transform.flip(i, True, False)
    ETL_attack.append(j)

steak_r = pygame.image.load('steak.png')
steak_l = pygame.transform.flip(steak_r, True, False)
pterosaurs_r = pygame.image.load('pterosaurs.png')
pterosaurs_l = pygame.transform.flip(pterosaurs_r, True, False)
bone_r = pygame.image.load('bone.png')
bone_l = pygame.transform.flip(bone_r, True, False)
steak_scale = pygame.transform.scale(steak_r, (30, 18))
bone_scale = pygame.transform.scale(bone_r, (30, 19))
egg = pygame.image.load('egg.png')
egg_scale = pygame.transform.scale(egg, (35, 30))
coin = pygame.image.load('coin.png')
coin_scale = pygame.transform.scale(coin, (25, 25))


def display_items_on_stats():
    win.blit(steak_scale, (960, 10))
    win.blit(bone_scale, (660, 10))
    win.blit(egg_scale, (330, 5))
    win.blit(coin_scale, (100, 8))


class Player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 80
        self.height = 85
        self.walkLeft = False
        self.walkRight = False
        self.idle = True
        self.walkCount = 0
        self.steps = 8
        self.heading = 'R'
        self.jump = False
        self.smallJump = False
        self.jumpCount = 10
        self.smallJumpCount = 5
        self.boulderPath = [-35, 100]
        self.jumpBoulder = False
        self.itemEaten = False
        self.hitBox = (self.x, self.y, self.width, self.height)
        self.health = 100
        self.weapon = 0
        self.leapEgg = 0
        self.level = 0
        self.xp = 0
        self.kills = 0
        self.blinkCount = 0
        self.deadCount = 0
        self.died = False
        self.attackJump = False

    def move(self):
        if not self.died:
            if self.heading == 'R':
                self.hitBox = (self.x, self.y + 7, self.width, self.height)
                if self.jump and self.walkRight:
                    self.hitBox = (self.x + 5, self.y + 7, self.width, self.height)
            else:
                self.hitBox = (self.x + 30, self.y + 5, self.width, self.height)
                if self.jump and self.walkLeft:
                    self.hitBox = (self.x + 20, self.y + 7, self.width, self.height)

            if self.walkRight and self.hitBox[0] < screenWidth - self.hitBox[2] - 10:
                if self.jump:
                    self.x += self.steps + 6
                    self.idle = True
                    self.walkRight = False
                    self.walkLeft = False
                    self.heading = 'R'
                if self.walkCount < 10 and not self.jump:
                    win.blit(walk_right[self.walkCount], (self.x, self.y))
                    self.walkCount += 3
                    self.x += self.steps
                    self.idle = False
                    self.walkLeft = False
                    self.heading = 'R'
                else:
                    self.walkCount = 0
                    self.idle = True
                    self.walkRight = False
            elif self.walkRight and self.hitBox[0] >= screenWidth - self.hitBox[2] - 10:
                self.walkCount = 0
                win.blit(walk_right[self.walkCount], (self.x, self.y))

            if self.walkRight and self.jumpBoulder:
                if not (self.boulderPath[0] < self.hitBox[0] < self.boulderPath[1] - 35):
                    self.jumpCount = -7
                    self.jump = True
                    self.walkCount = 0
                    win.blit(walk_right[self.walkCount], (self.x, self.y))

            if self.walkLeft and self.hitBox[0] > 10:
                if self.jump:
                    self.x -= self.steps
                    self.idle = True
                    self.walkRight = False
                    self.walkLeft = False
                    self.heading = 'L'
                if self.walkCount < 10 and not self.jump:
                    win.blit(walk_left[self.walkCount], (self.x - 35, self.y))
                    self.walkCount += 1
                    self.x -= self.steps
                    self.idle = False
                    self.walkRight = False
                    self.heading = 'L'
                else:
                    self.walkCount = 0
                    self.idle = True
            elif self.walkLeft and self.hitBox[0] <= 10:
                self.walkCount = 0
                win.blit(walk_left[self.walkCount], (self.x - 35, self.y))

            if self.idle:
                if self.heading == 'R':
                    win.blit(walk_right[0], (self.x, self.y))
                    self.walkRight = False
                    self.walkLeft = False
                else:
                    win.blit(walk_left[0], (self.x - 35, self.y))
                    self.walkRight = False
                    self.walkLeft = False

            if self.jump:
                if self.jumpCount >= -10:
                    neg = 1
                    if self.jumpCount < 0:
                        neg = -1
                    self.y -= ((self.jumpCount ** 2) * 0.5) * neg
                    self.jumpCount -= 1
                else:
                    self.jump = False
                    self.jumpCount = 10

            if self.smallJump:
                if self.smallJumpCount >= -5:
                    neg = 1
                    if self.smallJumpCount < 0:
                        neg = -1
                    self.y -= ((self.smallJumpCount ** 2) * 0.5) * neg
                    self.smallJumpCount -= 1
                else:
                    self.smallJump = False
                    self.smallJumpCount = 5
            # pygame.draw.rect(win, (255, 0, 0), self.hitBox, 2)

    def attack_jump(self, troll):
        if self.attackJump:
            if self.x > 200:
                if troll.attackRight:
                    self.smallJump = True
                    self.x += 4
                elif troll.attackLeft:
                    self.smallJump = True
                    self.x -= 4

    def climb_boulder(self):
        if (self.y <= 350 or self.y == 390) and (self.boulderPath[0] < self.x < self.boulderPath[1]):
            self.y = 390
            self.jump = False
            self.jumpBoulder = True
        else:
            self.jumpBoulder = False

    def dead(self):
        if not self.died:
            died_sound.play()
            if self.heading == 'R':
                win.blit(dead_right[self.deadCount], (self.x, self.y))
                self.deadCount += 1
                if self.deadCount > 7:
                    self.idle = False
                    self.died = True
                    self.walkRight = False
                    self.walkLeft = False
                    self.jump = False
            else:
                win.blit(dead_left[self.deadCount], (self.x, self.y))
                self.deadCount += 1
                if self.deadCount > 7:
                    self.idle = False
                    self.died = True
                    self.walkRight = False
                    self.walkLeft = False
                    self.jump = False
        else:
            self.health = 0
            self.idle = False
            self.died = True
            self.walkRight = False
            self.walkLeft = False
            self.jump = False
            if self.heading == 'L':
                win.blit(dead_left[7], (self.x, 530))
            else:
                win.blit(dead_right[7], (self.x, 530))

    def level_up(self):
        pass

    def eat_item(self):
        if not self.died:
            if self.hitBox[1] <= item.hitBox[1] + item.hitBox[3] <= self.hitBox[1] + self.height:
                if (item.hitBox[0] <= self.hitBox[0] + self.width <= item.hitBox[0] + item.hitBox[2]) or \
                        (item.hitBox[0] <= self.hitBox[0] <= item.hitBox[0] + item.hitBox[2]) or \
                        (item.hitBox[0] <= self.hitBox[0] + (self.width // 2) <= item.hitBox[0] + item.hitBox[2]):
                    self.itemEaten = True
                    if item.item == 'steak':
                        eat_sound.play()
                        self.health += 4
                        if self.health >= 100:
                            self.health = 100
                    if item.item == 'bone':
                        bone_sound.play()
                        self.weapon += 1
                        if self.weapon >= 100:
                            self.weapon = 100
                    if item.item == 'egg':
                        egg_sound.play()
                        self.leapEgg += 1
                        if self.leapEgg >= 100:
                            self.leapEgg = 100
                    if item.item == 'coin':
                        coin_sound.play()
                        self.xp += 1
                        self.level_up()

    def health_bar(self):
        pygame.draw.rect(win, (0, 0, 0), (1120, 10, 102, 15), 2)
        if self.health == 100:
            pygame.draw.rect(win, (0, 255, 0), (1122, 12, 100, 13))
        elif 80 <= self.health < 100:
            pygame.draw.rect(win, (255, 255, 0), (1122, 12, 80, 13))
        elif 60 <= self.health < 80:
            pygame.draw.rect(win, (255, 128, 0), (1122, 12, 60, 13))
        elif 40 <= self.health < 60:
            pygame.draw.rect(win, (255, 102, 102), (1122, 12, 40, 13))
        elif 20 <= self.health < 40:
            pygame.draw.rect(win, (255, 0, 0), (1122, 12, 20, 13))
        elif 0 < self.health < 20:
            if self.blinkCount % 2 == 0:
                pygame.draw.rect(win, (255, 0, 0), (1122, 12, 10, 13))
        self.blinkCount += 1
        if self.blinkCount > 10:
            self.blinkCount = 0

    def weapon_bar(self):
        pygame.draw.rect(win, (0, 0, 0), (820, 10, 102, 15), 2)
        if self.weapon == 100:
            pygame.draw.rect(win, (0, 255, 0), (822, 12, 100, 13))
        elif 80 <= self.weapon < 100:
            pygame.draw.rect(win, (255, 255, 0), (822, 12, 80, 13))
        elif 60 <= self.weapon < 80:
            pygame.draw.rect(win, (255, 128, 0), (822, 12, 60, 13))
        elif 40 <= self.weapon < 60:
            pygame.draw.rect(win, (255, 102, 102), (822, 12, 40, 13))
        elif 20 <= self.weapon < 40:
            pygame.draw.rect(win, (255, 0, 0), (822, 12, 20, 13))
        elif 0 < self.weapon < 20:
            pygame.draw.rect(win, (255, 0, 0), (822, 12, 10, 13))

    def leap_egg_bar(self):
        pygame.draw.rect(win, (0, 0, 0), (510, 10, 102, 15), 2)
        if self.leapEgg == 100:
            pygame.draw.rect(win, (0, 255, 0), (512, 12, 100, 13))
        elif 80 <= self.leapEgg < 100:
            pygame.draw.rect(win, (255, 255, 0), (512, 12, 80, 13))
        elif 60 <= self.leapEgg < 80:
            pygame.draw.rect(win, (255, 128, 0), (512, 12, 60, 13))
        elif 40 <= self.leapEgg < 60:
            pygame.draw.rect(win, (255, 102, 102), (512, 12, 40, 13))
        elif 20 <= self.leapEgg < 40:
            pygame.draw.rect(win, (255, 0, 0), (512, 12, 20, 13))
        elif 0 < self.leapEgg < 20:
            pygame.draw.rect(win, (255, 0, 0), (512, 12, 10, 13))

    def xp_bar(self):
        pygame.draw.rect(win, (0, 0, 0), (200, 10, 102, 15), 2)
        if self.leapEgg == 100:
            pygame.draw.rect(win, (212, 175, 55), (202, 12, 100, 13))
        elif 80 <= self.xp < 100:
            pygame.draw.rect(win, (212, 175, 55), (202, 12, 80, 13))
        elif 60 <= self.xp < 80:
            pygame.draw.rect(win, (212, 175, 55), (202, 12, 60, 13))
        elif 40 <= self.xp < 60:
            pygame.draw.rect(win, (212, 175, 55), (202, 12, 40, 13))
        elif 20 <= self.xp < 40:
            pygame.draw.rect(win, (212, 175, 55), (202, 12, 20, 13))
        elif 0 < self.xp < 20:
            pygame.draw.rect(win, (212, 175, 55), (202, 12, 10, 13))

    def show_stats(self):
        font = pygame.font.Font('freesansbold.ttf', 20)
        health = font.render("Health " + str(self.health), True, (255, 255, 255))
        win.blit(health, (1000, 10))
        self.health_bar()
        weapon = font.render("Weapon " + str(self.weapon), True, (255, 255, 255))
        win.blit(weapon, (700, 10))
        self.weapon_bar()
        leap_egg = font.render("Leap-Eggs " + str(self.leapEgg), True, (255, 255, 255))
        win.blit(leap_egg, (365, 10))
        self.leap_egg_bar()
        xp_coin = font.render("XP " + str(self.xp), True, (255, 255, 255))
        win.blit(xp_coin, (135, 10))
        self.xp_bar()
        level = font.render("LVL: " +str(self.level), True, (255, 255, 255))
        win.blit(level, (10, 10))
        enemy = font.render("E: " +str(self.kills), True, (255, 255, 255))
        win.blit(enemy, (10, 30))
        dino = font.render("DINO", True, (0, 0, 0))
        win.blit(dino, (1235, 10))


class Pterosaurs(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.stationary = False
        self.pace = 5
        self.width = 200
        self.height = 200
        self.flyRight = False
        self.flyLeft = False
        self.moveRight = False
        self.moveLeft = False
        self.roundComplete = False
        self.roundWaitCount = 0
        self.playerFly = False
        self.hitBox = (self.x, self.y, self.width, self.height)

    def draw(self, surf, right):
        if right:
            surf.blit(pterosaurs_r, (self.x, self.y))
        elif not right:
            surf.blit(pterosaurs_l, (self.x, self.y))

    def move(self):
        self.hitBox = (self.x + 10, self.y + 38, self.width - 20, self.height - 98)
        if not self.playerFly:
            if self.flyRight and (1100 > self.x):
                self.draw(win, True)
                self.x += self.pace
            else:
                self.flyRight = False
            if self.flyLeft and (self.x > 0):
                self.draw(win, False)
                self.x -= self.pace
            else:
                self.flyLeft = False
        pygame.draw.rect(win, (0, 0, 255), self.hitBox, 1)

    def make_rounds(self):
        self.hitBox = (self.x + 10, self.y + 38, self.width - 20, self.height - 98)
        if self.pace > 0:
            self.moveRight = True
            self.draw(win, True)
            self.moveLeft = False
        else:
            self.moveLeft = True
            self.draw(win, False)
            self.moveRight = False
        self.x += self.pace
        if self.x >= 1100:
            self.y += 20
            self.pace *= -1
        elif self.x <= 0:
            self.y += 20
            self.pace *= -1
        if self.y > 80:
            item.item = random.choice(item.itemList)
            self.y = -20
        # pygame.draw.rect(win, (0, 0, 255), self.hitBox, 2)


class Projectile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.stationary = False
        self.gravity = 4
        self.fall = False
        self.selectionList = [num for num in range(45, 1100, 5)]
        self.randomPos = random.choice(self.selectionList)
        self.itemList = ['steak', 'coin', 'bone', 'egg']
        self.item = random.choice(self.itemList)
        if self.item == 'steak':
            self.hitBox = (self.x, self.y, 60, 36)
        elif self.item == 'bone':
            self.hitBox = (self.x, self.y, 60, 39)
        elif self.item == 'egg':
            self.hitBox = (self.x, self.y, 48, 60)
        elif self.item == 'coin':
            self.hitBox = (self.x, self.y, 50, 50)

    def draw(self, surf, right):
        if self.item == 'steak':
            if right:
                surf.blit(steak_r, (self.x, self.y))
            else:
                surf.blit(steak_l, (self.x, self.y))
        elif self.item == 'bone':
            if right:
                surf.blit(bone_l, (self.x, self.y))
            else:
                surf.blit(bone_r, (self.x, self.y))
        elif self.item == 'egg':
            surf.blit(egg, (self.x, self.y))
        elif self.item == 'coin':
            surf.blit(coin, (self.x, self.y))

    def scale_down(self):
        if self.item == 'steak':
            win.blit(steak_scale, (self.x, self.y))
        elif self.item == 'bone':
            win.blit(bone_scale, (self.x, self.y))
        elif self.item == 'egg':
            win.blit(egg_scale, (self.x, self.y))
        elif self.item == 'coin':
            win.blit(coin_scale, (self.x, self.y))

    def drop(self):
        if self.item == 'steak':
            self.hitBox = (self.x, self.y, 60, 36)
        elif self.item == 'bone':
            self.hitBox = (self.x, self.y, 60, 39)
        elif self.item == 'egg':
            self.hitBox = (self.x, self.y, 48, 60)
        elif self.item == 'coin':
            self.hitBox = (self.x, self.y, 50, 50)
        if not pterosaurs.roundComplete:
            if not self.stationary:
                if self.x == self.randomPos:
                    self.fall = True
                    self.draw(win, True)
                    self.y += self.gravity
                    if self.y > 590 or dino.itemEaten:
                        self.stationary = True
                        self.fall = False
                        dino.itemEaten = False
            elif self.stationary:
                self.randomPos = random.choice(self.selectionList)
                self.stationary = False
                self.fall = False
        else:
            self.scale_down()
            if self.item == 'steak':
                self.x = 1040
                self.y = 10
            elif self.item == 'bone':
                self.x = 680
                self.y = 10
            elif self.item == 'egg':
                self.x = 330
                self.y = 5
            elif self.item == 'coin':
                self.x = 100
                self.y = 8
        # pygame.draw.rect(win, (0, 255, 0), self.hitBox, 2)

    def move(self):
        if self.item == 'steak':
            self.hitBox = (self.x, self.y, 60, 36)
        elif self.item == 'bone':
            self.hitBox = (self.x, self.y, 60, 39)
        elif self.item == 'egg':
            self.hitBox = (self.x, self.y, 48, 60)
        elif self.item == 'coin':
            self.hitBox = (self.x, self.y, 50, 50)
        if not pterosaurs.roundComplete:
            if not self.stationary and not self.fall:
                if pterosaurs.moveRight:
                    if self.item == 'steak':
                        self.x = pterosaurs.x + 45
                        self.y = pterosaurs.y + 130
                    elif self.item == 'bone':
                        self.x = pterosaurs.x + 45
                        self.y = pterosaurs.y + 120
                    elif self.item == 'egg':
                        self.x = pterosaurs.x + 40
                        self.y = pterosaurs.y + 120
                    elif self.item == 'coin':
                        self.x = pterosaurs.x + 50
                        self.y = pterosaurs.y + 135
                    self.draw(win, True)
                elif pterosaurs.moveLeft:
                    if self.item == 'steak':
                        self.x = pterosaurs.x + 95
                        self.y = pterosaurs.y + 130
                    elif self.item == 'bone':
                        self.x = pterosaurs.x + 95
                        self.y = pterosaurs.y + 120
                    elif self.item == 'egg':
                        self.x = pterosaurs.x + 85
                        self.y = pterosaurs.y + 120
                    elif self.item == 'coin':
                        self.x = pterosaurs.x + 100
                        self.y = pterosaurs.y + 135
                    self.draw(win, False)
            if self.stationary and not self.fall:
                self.draw(win, True)
        # pygame.draw.rect(win, (0, 255, 0), self.hitBox, 2)


class EasyTroll(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 320
        self.height = 200
        self.walkCount = 0
        self.attackCount = 0
        self.walkRight = False
        self.walkLeft = True
        self.attackRight = False
        self.attackLeft = False
        self.heading = None
        self.steps = 4
        self.hitBox = (self.x, self.y, self.width, self.height)

    def draw(self, right):
        if right:
            win.blit(ETR_walk[0], (self.x, self.y))
        else:
            win.blit(ETL_walk[0], (self.x, self.y))

    def move(self):
        if self.walkLeft:
            self.hitBox = (self.x + 70, self.y + 70, self.width - 180, self.height - 95)
            win.blit(ETL_walk[self.walkCount], (self.x, self.y))
            self.walkCount += 1
            self.x -= self.steps
            if self.walkCount > 9:
                self.walkCount = 0
            self.heading = 'L'
        elif self.walkRight:
            self.hitBox = (self.x + 110, self.y + 70, self.width - 180, self.height - 95)
            win.blit(ETR_walk[self.walkCount], (self.x, self.y))
            self.walkCount += 1
            self.x -= self.steps
            if self.walkCount > 9:
                self.walkCount = 0
            self.heading = 'R'
        if self.hitBox[0] <= 10:
            et_sound.play()
            self.walkRight = True
            self.walkLeft = False
            self.steps = self.steps * -1
        if self.hitBox[0] >= screenWidth - self.hitBox[2] - 10:
            et_sound.play()
            self.walkLeft = True
            self.walkRight = False
            self.steps *= -1
        # pygame.draw.rect(win, (0, 255, 0), self.hitBox, 2)

    def encounter(self, troll):
        if dino.hitBox[0] <= 10 and (self.attackLeft or self.attackRight):
            dino.x = 10
        if dino.hitBox[0] > screenWidth - dino.hitBox[2] - 35 and (self.attackRight or self.attackLeft):
            dino.x = screenWidth - 35 - dino.hitBox[2]
        if dino.y > 530:
            dino.y = 530
        if self.attackLeft:
            win.blit(ETL_attack[self.attackCount], (self.x, self.y))
            hit_sound.play()
            self.attackCount += 1
            if self.attackCount > 9:
                self.attackCount = 0
                self.attackLeft = False
                if self.heading == 'R':
                    self.walkRight = True
                    self.walkLeft = False
                else:
                    self.walkLeft = True
                    self.walkRight = False
            dino.health -= 1
            dino.attackJump = True
            dino.attack_jump(troll)
            if dino.health <= 0:
                dino.health = 0
                dino.dead()
        elif self.attackRight:
            win.blit(ETR_attack[self.attackCount], (self.x, self.y))
            hit_sound.play()
            self.attackCount += 1
            if self.attackCount > 9:
                self.attackCount = 0
                self.attackRight = False
                if self.heading == 'R':
                    self.walkRight = True
                    self.walkLeft = False
                else:
                    self.walkLeft = True
                    self.walkRight = False
            dino.health -= 1
            dino.attackJump = True
            dino.attack_jump(troll)
            if dino.health <= 0:
                dino.health = 0
                dino.dead()
        if not dino.died:
            if dino.hitBox[1]+dino.hitBox[3] >= self.hitBox[1]:
                if (self.hitBox[0] <= dino.hitBox[0]+dino.hitBox[2] <= self.hitBox[0]+self.hitBox[2]) or \
                        (self.hitBox[0]+self.hitBox[2] >= dino.hitBox[0] >= self.hitBox[0]):
                    if self.walkLeft:
                        if dino.heading == 'R':
                            self.walkRight = False
                            self.walkLeft = False
                            self.attackRight = False
                            self.attackLeft = True
                        else:
                            if dino.hitBox[0] >= self.hitBox[0]:
                                self.walkRight = False
                                self.walkLeft = False
                                self.attackLeft = False
                                self.attackRight = True
                            else:
                                self.walkRight = False
                                self.walkLeft = False
                                self.attackRight = False
                                self.attackLeft = True
                    else:
                        if dino.heading == 'L':
                            self.walkRight = False
                            self.walkLeft = False
                            self.attackLeft = False
                            self.attackRight = True
                        else:
                            if dino.hitBox[0] <= self.hitBox[0]:
                                self.walkRight = False
                                self.walkLeft = False
                                self.attackRight = False
                                self.attackLeft = True
                            else:
                                self.walkRight = False
                                self.walkLeft = False
                                self.attackLeft = False
                                self.attackRight = True
        else:
            dino.dead()


item = Projectile(200, 0)
pterosaurs = Pterosaurs(0, -20)
dino = Player(20, 530)
enemy = []
no_of_enemies = 2


for i in range(no_of_enemies):
    x = random.randint(130, 800)
    y = 450
    j = EasyTroll(x, y)
    enemy.append(j)


def game_window_update():
    win.blit(background, (0, 0))
    for k in enemy:
        k.move()
        k.encounter(k)
    pterosaurs.make_rounds()
    dino.move()
    item.move()
    item.drop()
    pterosaurs.move()
    dino.climb_boulder()
    dino.eat_item()
    dino.show_stats()
    display_items_on_stats()
    pygame.display.update()


run = True

while run:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                if len(enemy) > 0:
                    enemy.pop()
                else:
                    print('No more trolls')

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        dino.walkRight = True
    if keys[pygame.K_LEFT]:
        dino.walkLeft = True
    if keys[pygame.K_SPACE]:
        if not dino.jumpBoulder:
            dino.jump = True
    if keys[pygame.K_s]:
        pterosaurs.stationary = False
        pterosaurs.flyRight = True
        pterosaurs.flyLeft = False
    if keys[pygame.K_a]:
        pterosaurs.stationary = False
        pterosaurs.flyLeft = True
        pterosaurs.flyRight = False

    game_window_update()
