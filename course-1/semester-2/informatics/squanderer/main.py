import pygame, sys, math
from hero import *

pygame.init()

w = 1280
h = 720
w2 = 640
h2 = 360
a = 0
b = 0
c = 0
n = 32
sc = 96
spd = 3
PL_FL = False
stamina = 200
#x = 100
#y = 100
lis_per = {'x': 100, 'y': 100}
PL_ANG = 0
ans = 0
angle = 0
PL_FLAG = True

SCREEN = pygame.display.set_mode((w, h))#, pygame.FULLSCREEN)
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

TRASH = pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("assets/trash_can.png")))
TRASH1 = pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load("assets/trash_can1.png")))


PLAYER_MAP = pygame.image.load("assets/player_map.png")

PLAYER1 = [[pygame.transform.scale(PLAYER_MAP.subsurface((32*i, n+32*j, 32, 32)), (sc, sc)) for j in range(9) for _ in range(10)] for i in range(8)]


#PLAYER1 = [[PLAYER_MAP.subsurface((0, n, 32, 32)), PLAYER_MAP.subsurface((0, n+32, 32, 32))],
           #PLAYER_MAP.subsurface((32, n, 32, 32)), PLAYER_MAP.subsurface((32*2, n, 32, 32)), PLAYER_MAP.subsurface((32*3, n, 32, 32)),
           #PLAYER_MAP.subsurface((32*4, n, 32, 32)), PLAYER_MAP.subsurface((32*5, n, 32, 32)), PLAYER_MAP.subsurface((32*6, n, 32, 32)), PLAYER_MAP.subsurface((32*7, n, 32, 32))]
#PLAYER1 = [pygame.transform.scale(j, (64, 64)) for j in PLAYER1]
#PLAYER = [PLAYER_MAP.subsurface((0, 0, 16, 16)), PLAYER_MAP.subsurface((16, 0, 16, 16)), PLAYER_MAP.subsurface((32, 0, 16, 16))]
#PLAYER = [pygame.transform.scale(j, (64, 64)) for j in PLAYER for i in range(16)]
#PLAYER_REV = [pygame.transform.flip(i, True, False) for i in PLAYER]
PL_F = 0
x_sl = 440


PLAYER_c = pygame.transform.scale2x(pygame.image.load("assets/test_player.png").convert())
PLAYER_c.set_colorkey((0, 0, 0))

heros = [Swordsman('i am swordsman and i am here', 'sword', {'stg': 10, 'dxt': 4, 'itl': 1}),
         Magician('magic... mAgIc.. MAGIC!!!', 'magic', {'stg': 1, 'dxt': 6, 'itl': 10})]

clock = pygame.time.Clock()


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def save(file, name, x):
    with open(f"saves/{file}.txt", "r") as f:
        l = f.readline().split()
    with open(f"saves/{file}.txt", "w") as f:
        if name in l:
            l[l.index(name)+1] = x
        else:
            l.append(name)
            l.append(x)
        print(l)
        f.write(' '.join(l))

def load_save(file, name):
    with open(f"saves/{file}.txt") as f:
        l = f.readline().split()
        for i in l:
            if i == name:
                return l[l.index(i)+1]


def get_info(h, n):
    a = f'{h.stats[n]}'
    return a

def start():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        START_TEXT = get_font(20).render("press any button.", True, "White")
        START_RECT = START_TEXT.get_rect(center=(640, 660))
        SCREEN.blit(START_TEXT, START_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                play()

        pygame.display.update()
def play():
    global PLAYER, PL_F, PL_FL, lis_per,  spd, sc, PL_ANG, ans, angle, PL_FLAG, stamina
    PL_c = pygame.transform.rotate(PLAYER_c, angle)
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill((x_sl-440, x_sl-440, x_sl-440))

        #PLAY_BACK = Button(base_image=None, hovering_image=None, pos=(640, 460), text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        #PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        #PLAY_BACK.update(SCREEN)
        angle = round(-math.degrees(math.atan2((lis_per['y']-PLAY_MOUSE_POS[1]), (lis_per['x']-PLAY_MOUSE_POS[0]))))
        PL_c = pygame.transform.rotate(PLAYER_c, angle)
        #PLAY_PL_RECT = PLAYER.get_rect(center=(x,y))

        pygame.draw.rect(SCREEN, (0, 255, 50), (20, 700, stamina, 10))

        if PL_FLAG:
            SCREEN.blit(PL_c, (lis_per['x'] - int(PL_c.get_width() / 2), lis_per['y'] - int(PL_c.get_height() / 2)))
        else:
            SCREEN.blit(pygame.transform.scale(PLAYER1[PL_ANG][PL_F], (sc, sc)), (lis_per['x'] - int(PLAYER1[PL_ANG][PL_F].get_width() / 2), lis_per['y'] - int(PLAYER1[PL_ANG][PL_F].get_height() / 2)))
        #SCREEN.blit(PLAYER[PL_F] if PL_FL is False else PLAYER_REV[PL_F], (x - int(PLAYER[PL_F].get_width() / 2), y - int(PLAYER[PL_F].get_height() / 2)))
        #SCREEN.blit(PLAYER_REV[2], (300, 300))

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu()

        if keys[pygame.K_TAB]:
            PL_FLAG = True
        else:
            PL_FLAG = False

        if keys[pygame.K_ESCAPE]:
            menu()


        if keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]:
            PL_F += 1
            if keys[pygame.K_LSHIFT] and stamina > 0:
                spd = 5
                stamina -= 1
            else:
                spd = 3

        else:
            PL_F = 0

        if not keys[pygame.K_LSHIFT] and stamina < 200:
            stamina += 0.5
        if keys[pygame.K_SPACE]:
            pass

        if PL_F >= len(PLAYER1[PL_ANG]):
            PL_F = 0
        if keys[pygame.K_w] or keys[pygame.K_k]:
            lis_per['y'] -= spd
        if keys[pygame.K_s] or keys[pygame.K_j]:
            lis_per['y'] += spd
        if keys[pygame.K_a] or keys[pygame.K_h]:
            lis_per['x'] -= spd
        if keys[pygame.K_d] or keys[pygame.K_l]:
            lis_per['x'] += spd

        if -15 < angle < 15:
            PL_ANG = 7

        if -15 > angle > -75:
            PL_ANG = 5

        if -75 > angle > -105:
            PL_ANG = 3

        if -105 > angle > -165:
            PL_ANG = 4

        if -165 > angle > -180 or 180 > angle > 165:
            PL_ANG = 6

        if 165 > angle > 105:
            PL_ANG = 1

        if 105 > angle > 75:
            PL_ANG = 0

        if 75 > angle > 15:
            PL_ANG = 2


        PLAY_TEXT = get_font(10).render(f"{angle}", True, "black")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(1000, 10))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        pygame.display.update()
        clock.tick(60)

def new_game():
    hn = 0
    while True:
        SCREEN.blit(BG, (0, 0))

        NEW_GAME_MOUSE_POS = pygame.mouse.get_pos()

        NEW_GAME_TEXT = get_font(45).render("This is the NEW GAME screen.", True, "White")
        NEW_GAME_RECT = NEW_GAME_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(NEW_GAME_TEXT, NEW_GAME_RECT)

        NEW_GAME_BACK = Button(base_image=None, hovering_image=None, pos=(160, 650), text_input="BACK", font=get_font(45), base_color="White", hovering_color="Green")
        NEW_GAME_START = Button(base_image=None, hovering_image=None, pos=(1120, 650), text_input="START", font=get_font(45), base_color="White", hovering_color="Green")

        NEW_GAME_STATSS = Button(base_image=None, hovering_image=None, pos=(200, 350), text_input=f"strange: {get_info(heros[hn], 'stg')}", font=get_font(25), base_color="White", hovering_color="White")
        NEW_GAME_STATSD = Button(base_image=None, hovering_image=None, pos=(200, 450), text_input=f"dexterity: {get_info(heros[hn], 'dxt')}", font=get_font(25), base_color="White", hovering_color="White")
        NEW_GAME_STATSI = Button(base_image=None, hovering_image=None, pos=(200, 550), text_input=f"intelligence: {get_info(heros[hn], 'itl')}", font=get_font(25), base_color="White", hovering_color="White")

        NEW_GAME_HERO = Button(base_image=None, hovering_image=None, pos=(250, 200), text_input=f"{heros[hn].clas}", font=get_font(45), base_color="White", hovering_color="White")
        NEW_GAME_HL = Button(base_image=None, hovering_image=None, pos=(125, 200), text_input="<", font=get_font(45), base_color="White", hovering_color="Green")
        NEW_GAME_HR = Button(base_image=None, hovering_image=None, pos=(375, 200), text_input=">", font=get_font(45), base_color="White", hovering_color="Green")
        #NEW_GAME_MAP = Button(base_image=None, hovering_image=None, pos=(1120, 650), text_input="START", font=get_font(45), base_color="White", hovering_color="Green")
        #NEW_GAME_ML = Button(base_image=None, hovering_image=None, pos=(1120, 650), text_input="START", font=get_font(45), base_color="White", hovering_color="Green")
        #NEW_GAME_MR = Button(base_image=None, hovering_image=None, pos=(1120, 650), text_input="START", font=get_font(45), base_color="White", hovering_color="Green")

        for button in [NEW_GAME_BACK, NEW_GAME_START, NEW_GAME_STATSS, NEW_GAME_STATSD, NEW_GAME_STATSI, NEW_GAME_HERO, NEW_GAME_HL, NEW_GAME_HR]:
            button.changeColor(NEW_GAME_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NEW_GAME_BACK.checkForInput(NEW_GAME_MOUSE_POS):
                    main_menu()
                if NEW_GAME_START.checkForInput(NEW_GAME_MOUSE_POS):
                    start()
                if NEW_GAME_HR.checkForInput(NEW_GAME_MOUSE_POS):
                    if hn < 1:
                        hn += 1
                    else:
                        hn = 0
                if NEW_GAME_HL.checkForInput(NEW_GAME_MOUSE_POS):
                    if hn > 0:
                        hn -= 1
                    else:
                        hn = 1

        pygame.display.update()


def options():
    global x_sl
    while True:
        SCREEN.blit(BG, (0, 0))

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)


        OPTIONS_BACK = Button(base_image=None, hovering_image=None, pos=(640, 460), text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
        OPTIONS_SLIDE = Button(base_image=None, hovering_image=None, pos=(x_sl, 360), text_input="*", font=get_font(75), base_color=(x_sl-440, x_sl-440, x_sl-440), hovering_color="Green")


        for button in [OPTIONS_BACK, OPTIONS_SLIDE]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    save('opt', 'x_sl', str(x_sl))
                    main_menu()

        if OPTIONS_SLIDE.checkForInput(OPTIONS_MOUSE_POS):
            if 440 < OPTIONS_MOUSE_POS[0] < 440 + 254:
                x_sl = OPTIONS_MOUSE_POS[0]

        pygame.display.update()


def load_menu():
    global SV_F
    sv1 = load_save('opt', 'sv1')
    sv2 = load_save('opt', 'sv2')
    while True:
        SCREEN.blit(BG, (0, 0))

        LOAD_MOUSE_POS = pygame.mouse.get_pos()

        LOAD_TEXT = get_font(100).render("SAVES", True, "#b68f40")
        LOAD_RECT = LOAD_TEXT.get_rect(center=(640, 100))

        SAVE1_BUTTON = Button(base_image=None, hovering_image=None, pos=(640, 250), text_input=sv1, font=get_font(75), base_color="#2D3E3E", hovering_color="White")
        SAVE1_BUT_TRASH = Button(base_image=TRASH, hovering_image=TRASH1, pos=(1100, 250), text_input=None, font=None, base_color=None, hovering_color=None)
        SAVE2_BUTTON = Button(base_image=None, hovering_image=None, pos=(640, 400), text_input=sv2, font=get_font(75), base_color="#2D3E3E", hovering_color="White")
        SAVE2_BUT_TRASH = Button(base_image=TRASH, hovering_image=TRASH1, pos=(1100, 400), text_input=None, font=None, base_color=None, hovering_color=None)
        QUIT_BUTTON = Button(base_image=None, hovering_image=None, pos=(640, 550), text_input="BACK", font=get_font(75), base_color="#2D3E3E", hovering_color="White")

        SCREEN.blit(LOAD_TEXT, LOAD_RECT)

        for button in [SAVE1_BUTTON, SAVE2_BUTTON, QUIT_BUTTON, SAVE1_BUT_TRASH, SAVE2_BUT_TRASH]:
            button.changeColor(LOAD_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SAVE1_BUTTON.checkForInput(LOAD_MOUSE_POS):
                    SV_F = True
                    if sv1 == '--empty--':
                        save('opt', 'sv1', 'SAVE-1')
                        save('sv1', 'x', '100')
                        save('sv1', 'y', '100')

                        for i in ['x', 'y']:
                            lis_per[i] = int(load_save('sv1', i))
                        new_game()
                    else:
                        for i in ['x', 'y']:
                            lis_per[i] = int(load_save('sv1', i))
                        play()

                if SAVE1_BUT_TRASH.checkForInput(LOAD_MOUSE_POS):
                    f = open('saves/sv1.txt', 'w')
                    f.close()
                    save('opt', 'sv1', '--empty--')
                    sv1 = load_save('opt', 'sv1')
                if SAVE2_BUTTON.checkForInput(LOAD_MOUSE_POS):
                    SV_F = False
                    if sv2 == '--empty--':
                        save('opt', 'sv2', 'SAVE-2')
                        save('sv2', 'x', '100')
                        save('sv2', 'y', '100')

                        for i in ['x', 'y']:
                            lis_per[i] = int(load_save('sv2', i))
                    else:
                        for i in ['x', 'y']:
                            lis_per[i] = int(load_save('sv2', i))
                    new_game()
                if SAVE2_BUT_TRASH.checkForInput(LOAD_MOUSE_POS):
                    f = open('saves/sv2.txt', 'w')
                    f.close()
                    save('opt', 'sv2', '--empty--')
                    sv2 = load_save('opt', 'sv2')
                if QUIT_BUTTON.checkForInput(LOAD_MOUSE_POS):
                    main_menu()
        pygame.display.update()

def main_menu():
    global x_sl
    x_sl = int(load_save('opt', 'x_sl'))
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(base_image=None, hovering_image=None, pos=(640, 250), text_input="PLAY", font=get_font(75), base_color="#2D3E3E", hovering_color="White")
        OPTIONS_BUTTON = Button(base_image=None, hovering_image=None, pos=(640, 400), text_input="OPTIONS", font=get_font(75), base_color="#2D3E3E", hovering_color="White")
        QUIT_BUTTON = Button(base_image=None, hovering_image=None, pos=(640, 550), text_input="QUIT", font=get_font(75), base_color="#2D3E3E", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    load_menu()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def menu():
    global x, y, SV_F
    x_p_q = -40
    x_p_p = -40
    x_p_o = -40
    x_p_s = -40
    while True:
        SCREEN.blit(pygame.transform.scale(BG, (100, 120)), (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()


        PLAY_BUTTON = Button(base_image=None, hovering_image=None, pos=(x_p_p, 35), text_input="PLAY", font=get_font(15), base_color="#2D3E3E", hovering_color="White")
        SAVE_BUTTON = Button(base_image=None, hovering_image=None, pos=(x_p_s, 60), text_input="SAVE", font=get_font(15), base_color="#2D3E3E", hovering_color="White")
        OPTIONS_BUTTON = Button(base_image=None, hovering_image=None, pos=(x_p_o, 85), text_input="OPTIONS", font=get_font(10), base_color="#2D3E3E", hovering_color="White")
        QUIT_BUTTON = Button(base_image=None, hovering_image=None, pos=(x_p_q, 105), text_input="QUIT", font=get_font(15), base_color="#2D3E3E", hovering_color="White")

        MENU_TEXT = get_font(20).render("MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(50, 10))
        SCREEN.blit(MENU_TEXT, MENU_RECT)


        for button in [PLAY_BUTTON, QUIT_BUTTON, OPTIONS_BUTTON, SAVE_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        if QUIT_BUTTON.pos() < 50:
            x_p_q += 3
        if OPTIONS_BUTTON.pos() < 50 and QUIT_BUTTON.pos() == 50:
            x_p_o += 3
        if SAVE_BUTTON.pos() < 50 and OPTIONS_BUTTON.pos() == 50:
            x_p_s += 3
        if PLAY_BUTTON.pos() < 50 and SAVE_BUTTON.pos() == 50:
            x_p_p += 3


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if SAVE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    if SV_F:
                        for i in lis_per:
                            save('sv1', i, str(lis_per[i]))
                    else:
                        for i in lis_per:
                            save('sv2', i, str(lis_per[i]))

                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    #pygame.quit()
                    #sys.exit()
                    main_menu()

        pygame.display.update()


class Button():
    def __init__(self, base_image, hovering_image, pos, text_input, font, base_color, hovering_color):
        self.image = base_image
        self.base_image = base_image
        self.hovering_image = hovering_image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        if self.text_input is not None:
            self.text = self.font.render(self.text_input, True, self.base_color)
            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def pos(self):
        return self.x_pos

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        if self.text_input is not None:
            screen.blit(self.text, self.text_rect)


    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if self.text_input is not None:
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                self.text = self.font.render(self.text_input, True, self.hovering_color)
            else:
                self.text = self.font.render(self.text_input, True, self.base_color)
        else:
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                self.image = self.hovering_image
            else:
                self.image = self.base_image


main_menu()
