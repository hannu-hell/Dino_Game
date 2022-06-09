import pygame
pygame.init()

screenWidth = 1300
screenHeight = 640
clock = pygame.time.Clock()
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("The Exploring DINO")
background = pygame.image.load('background.jpg')


dead_right = [pygame.image.load('Dead (1).png'), pygame.image.load('Dead (2).png'),
              pygame.image.load('Dead (3).png'), pygame.image.load('Dead (4).png'), pygame.image.load('Dead (5).png'),
              pygame.image.load('Dead (6).png'), pygame.image.load('Dead (7).png'), pygame.image.load('Dead (8).png')]

dead_left = [pygame.image.load('Dead (1)L.png'), pygame.image.load('Dead (2)L.png'), pygame.image.load('Dead (3)L.png'),
             pygame.image.load('Dead (4)L.png'), pygame.image.load('Dead (5)L.png'), pygame.image.load('Dead (6)L.png'),
             pygame.image.load('Dead (7)L.png'), pygame.image.load('Dead (8)L.png')]

idle_right = [pygame.image.load('Idle (1).png'), pygame.image.load('Idle (2).png'), pygame.image.load('Idle (3).png'),
              pygame.image.load('Idle (4).png'), pygame.image.load('Idle (5).png'), pygame.image.load('Idle (6).png'),
              pygame.image.load('Idle (7).png'), pygame.image.load('Idle (8).png'), pygame.image.load('Idle (9).png'),
              pygame.image.load('Idle (10).png')]

idle_left = [pygame.image.load('Idle (1)L.png'), pygame.image.load('Idle (2)L.png'), pygame.image.load('Idle (3)L.png'),
             pygame.image.load('Idle (4)L.png'), pygame.image.load('Idle (5)L.png'), pygame.image.load('Idle (6)L.png'),
             pygame.image.load('Idle (7)L.png'), pygame.image.load('Idle (8)L.png'), pygame.image.load('Idle (9)L.png'),
             pygame.image.load('Idle (10)L.png')]

jump_right = [pygame.image.load('Jump (1).png'), pygame.image.load('Jump (2).png'), pygame.image.load('Jump (3).png'),
              pygame.image.load('Jump (4).png'), pygame.image.load('Jump (5).png'), pygame.image.load('Jump (6).png'),
              pygame.image.load('Jump (7).png'), pygame.image.load('Jump (8).png'), pygame.image.load('Jump (9).png'),
              pygame.image.load('Jump (10).png'), pygame.image.load('Jump (11).png'),
              pygame.image.load('Jump (12).png')]

jump_left = [pygame.image.load('Jump (1)L.png'), pygame.image.load('Jump (2)L.png'), pygame.image.load('Jump (3)L.png'),
             pygame.image.load('Jump (4)L.png'), pygame.image.load('Jump (5)L.png'), pygame.image.load('Jump (6)L.png'),
             pygame.image.load('Jump (7)L.png'), pygame.image.load('Jump (8)L.png'), pygame.image.load('Jump (9)L.png'),
             pygame.image.load('Jump (10)L.png'), pygame.image.load('Jump (11)L.png'),
             pygame.image.load('Jump (12)L.png')]

run_right = [pygame.image.load('Run (1).png'), pygame.image.load('Run (2).png'), pygame.image.load('Run (3).png'),
             pygame.image.load('Run (4).png'), pygame.image.load('Run (5).png'), pygame.image.load('Run (6).png'),
             pygame.image.load('Run (7).png'), pygame.image.load('Run (8).png')]

run_left = [pygame.image.load('Run (1)L.png'), pygame.image.load('Run (2)L.png'), pygame.image.load('Run (3)L.png'),
            pygame.image.load('Run (4)L.png'), pygame.image.load('Run (5)L.png'), pygame.image.load('Run (6)L.png'),
            pygame.image.load('Run (7)L.png'), pygame.image.load('Run (8)L.png')]

ETR_walk = [pygame.image.load('ETR_walk0.png'), pygame.image.load('ETR_walk1.png'), pygame.image.load('ETR_walk2.png'),
            pygame.image.load('ETR_walk3.png'), pygame.image.load('ETR_walk4.png'), pygame.image.load('ETR_walk5.png'),
            pygame.image.load('ETR_walk6.png'), pygame.image.load('ETR_walk7.png'), pygame.image.load('ETR_walk8.png'),
            pygame.image.load('ETR_walk9.png')]

ETL_walk = []
for i in ETR_walk:
    j = pygame.transform.flip(i, True, False)
    ETL_walk.append(j)

ETR_attack = [pygame.image.load('ETR_attack0.png'), pygame.image.load('ETR_attack1.png'), pygame.image.load('ETR_attack2.png'),
              pygame.image.load('ETR_attack3.png'), pygame.image.load('ETR_attack4.png'), pygame.image.load('ETR_attack5.png'),
              pygame.image.load('ETR_attack6.png'), pygame.image.load('ETR_attack7.png'), pygame.image.load('ETR_attack8.png'),
              pygame.image.load('ETR_attack9.png')]


# if self.walkRight and self.jumpBoulder:
#     if self.boulderPath[0] < self.x < self.boulderPath[1] - 35:
#         if self.walkCount < 10:
#             win.blit(walk_right[self.walkCount], (self.x, self.y))
#             self.walkCount += 1
#             self.x += self.steps
#             self.idle = False
#             self.walkLeft = False
#             self.heading = 'R'
#         else:
#             self.walkCount = 0
#             self.idle = True
#     else:
#         self.jumpCount = -7
#         self.jump = True
#         self.walkCount = 0
#         win.blit(walk_right[self.walkCount], (self.x, self.y))

count = 0
action = False


def test_character():
    global count, action
    if action:
        win.blit(ETR_attack[count], (200, 200+200))
        win.blit(dead_left[count], (380, 280+200))
        count += 1
        if count > 7:
            count = 0
            action = False
    else:

        win.blit(idle_left[0], (380, 280+200))
        win.blit(ETR_attack[0], (200, 200+200))



def game_window_update():
    win.blit(background, (0, 0))
    test_character()
    clock.tick(10)
    pygame.display.update()


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        action = True
    # if keys[pygame.K_LEFT]:
    #     dino.walkLeft = True
    # if keys[pygame.K_SPACE]:
    #     if not dino.jumpBoulder:
    #         dino.jump = True
    game_window_update()