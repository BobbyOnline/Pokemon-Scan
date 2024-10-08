import pygame
import os
import time
import threading
import random
from spritesheet import Spritesheet
import sys
from utils import checkCollisions




# creating the game window
WIDTH, HEIGHT = 800, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PokeScan!")
pygame_icon = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "icon.png"))
pygame.display.set_icon(pygame_icon)
pygame.init()

#few title screen vars
y = 0
checkt = False
# init color consts
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (56, 175, 43)
RED = (255,0,0)
YELLOW = (220, 203, 107)
SKY_BLUE = (0,200,255)

# framerate that the game uses
FPS = 30

# load in sound effects

try:
    tepigCry = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "assets", "sounds", "tepig.wav"))
    bulbaCry = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "assets", "sounds","bulbasaur.wav"))
    totoCry = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "assets", "sounds","totodile.wav"))
    select = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "assets", "sounds","select.wav"))
    trade = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "assets", "sounds","trade.wav"))
    hit = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "assets", "sounds","hit.wav"))
    enhit = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "assets", "sounds","enhit.wav"))
    # load in music

    battleMusic = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "assets", "sounds","battle.wav"))
    menuMusic = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "assets", "sounds","menu.wav"))
    victoryMusic = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "assets", "sounds","victory.wav"))
    drawMusic = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "assets", "sounds","draw.wav"))
    loseMusic = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "assets", "sounds","lose.wav"))
    soundsLoaded = True
except:
    soundsLoaded = False







# load in assets
BACKGROUND = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "background.png"))
TITLESCREEN = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "titlescreen.png"))
LOSESCREEN = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "losescreen.png"))
WINSCREEN = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "winscreen.png"))
DRAWSCREEN = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "drawscreen.png"))
TUT1 = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "tut1.png"))
TUT2 = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "tut2.png"))
TUT3 = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "tut3.png"))
OVERLAY = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "overlay.png"))
OVERLAY = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "overlay.png"))
H1 = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "r1.png"))
H2 = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "r2.png"))
H3 = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "r3.png"))
H4 = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "r4.png"))
H5 = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "r5.png"))
H6 = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", "r6.png"))


_bulbasaur = pygame.image.load(os.path.join(os.path.dirname(__file__), "data", "cards", "bulbasaur_card.png"))
_tepig = pygame.image.load(os.path.join(os.path.dirname(__file__), "data", "cards", "tepig_card.png"))
_tododile = pygame.image.load(os.path.join(os.path.dirname(__file__), "data", "cards", "tododile_card.png"))

#obtaining sprites for bulbasaur
bulbaFront = Spritesheet(os.path.join(os.path.dirname(__file__), "assets", "bulba_spritesheet.png"))
bulbaF_animation = [bulbaFront.parse_sprite('Layer 2.png'), bulbaFront.parse_sprite('Layer 3.png'),bulbaFront.parse_sprite('Layer 4.png'),
                   bulbaFront.parse_sprite('Layer 5.png'),bulbaFront.parse_sprite('Layer 6.png'),bulbaFront.parse_sprite('Layer 7.png')
                   ,bulbaFront.parse_sprite('Layer 8.png') ,bulbaFront.parse_sprite('Layer 9.png') ,bulbaFront.parse_sprite('Layer 10.png')
                   ,bulbaFront.parse_sprite('Layer 11.png') ,bulbaFront.parse_sprite('Layer 12.png')]

bulbaBack = Spritesheet(os.path.join(os.path.dirname(__file__), "assets", "bulbaB_spritesheet.png"))
bulbaB_animation = [bulbaBack.parse_sprite('Layer 2.png'), bulbaBack.parse_sprite('Layer 3.png'),bulbaBack.parse_sprite('Layer 4.png'),
                   bulbaBack.parse_sprite('Layer 5.png'),bulbaBack.parse_sprite('Layer 6.png'),bulbaBack.parse_sprite('Layer 7.png')
                   ,bulbaBack.parse_sprite('Layer 8.png') ,bulbaBack.parse_sprite('Layer 9.png') ,bulbaBack.parse_sprite('Layer 10.png')
                   ,bulbaBack.parse_sprite('Layer 11.png') ,bulbaBack.parse_sprite('Layer 12.png'),bulbaBack.parse_sprite('Layer 13.png')]

#obtaining sprites for totodile
totoFront = Spritesheet(os.path.join(os.path.dirname(__file__), "assets", "toto_spritesheet.png"))
totoF_animation = [totoFront.parse_sprite('Layer 2.png'), totoFront.parse_sprite('Layer 3.png'),totoFront.parse_sprite('Layer 4.png'),
                   totoFront.parse_sprite('Layer 5.png'),totoFront.parse_sprite('Layer 6.png'),totoFront.parse_sprite('Layer 7.png')
                   ,totoFront.parse_sprite('Layer 8.png') ,totoFront.parse_sprite('Layer 9.png') ,totoFront.parse_sprite('Layer 10.png')
                   ,totoFront.parse_sprite('Layer 11.png')]

totoBack = Spritesheet(os.path.join(os.path.dirname(__file__), "assets", "totoB_spritesheet.png"))
totoB_animation = [totoBack.parse_sprite('Layer 2.png'), totoBack.parse_sprite('Layer 3.png'),totoBack.parse_sprite('Layer 4.png'),
                   totoBack.parse_sprite('Layer 5.png'),totoBack.parse_sprite('Layer 6.png'),totoBack.parse_sprite('Layer 7.png')
                   ,totoBack.parse_sprite('Layer 8.png') ,totoBack.parse_sprite('Layer 9.png') ,totoBack.parse_sprite('Layer 10.png')
                   ,totoBack.parse_sprite('Layer 11.png')]


#obtaining sprites for tepig
tepigFront = Spritesheet(os.path.join(os.path.dirname(__file__), "assets", "tepig_spritesheet.png"))
tepigF_animation = [tepigFront.parse_sprite('Layer 2.png'), tepigFront.parse_sprite('Layer 3.png'),tepigFront.parse_sprite('Layer 4.png'),
                   tepigFront.parse_sprite('Layer 5.png'),tepigFront.parse_sprite('Layer 6.png'),tepigFront.parse_sprite('Layer 7.png')
                   ,tepigFront.parse_sprite('Layer 8.png')]

tepigBack = Spritesheet(os.path.join(os.path.dirname(__file__), "assets", "tepigB_spritesheet.png"))
tepigB_animation = [tepigBack.parse_sprite('Layer 2.png'), tepigBack.parse_sprite('Layer 3.png'),tepigBack.parse_sprite('Layer 4.png'),
                   tepigBack.parse_sprite('Layer 5.png'),tepigBack.parse_sprite('Layer 6.png'),tepigBack.parse_sprite('Layer 7.png')
                   ,tepigBack.parse_sprite('Layer 8.png')]



font = pygame.font.Font(os.path.join(os.path.dirname(__file__), "assets", "pokemon_fire_red.ttf"), 64)
font_large = pygame.font.Font(os.path.join(os.path.dirname(__file__), "assets", "pokemon_fire_red.ttf"), 128)
font_small = pygame.font.Font(os.path.join(os.path.dirname(__file__), "assets", "pokemon_fire_red.ttf"), 32)

# resizing pokemon
BULBASAUR = pygame.transform.scale(_bulbasaur, (120, 178))
TEPIG = pygame.transform.scale(_tepig, (120, 178))
TOTODILE = pygame.transform.scale(_tododile, (120, 178))

class Game():

    def __init__(self):
        # the pokemon that the user wants to play
        self.desired_pokemon = None
        self.enemy_pokemon = None
        #index for animation array
        self.index = 0
        self.skip = .5

        self.index1 = 0
        self.skip1 = .5

        # int that increments by 1 for each frame the game draws
        self.global_timer = 0

       
        self.pokemon_chosen_time = 0

        # holds hp of your pokemon
        # like usual, 0 is bulbasaur, 1 is tepig, 2 is totodile
        self.hps = [12] * 3
        self.enemy_hps = [12] * 3
        self.hpslocation = [628] * 3
        self.enemy_hpslocation = [124] * 3


    
     
        self.results_done = False

   
        self.gameResult = None

        self.inGame = False






    def _draw_window(self, pokemon):

        
        # for now, just using 0,1,2 for pokemon values, should make enum
        choice = None
        match(pokemon):
            case 0:
                choice = BULBASAUR
            case 1:
                choice = TEPIG
            case 2:
                choice = TOTODILE
            case default:
                choice = None

       
        WIN.blit(BACKGROUND, (0,0))
        WIN.blit(H1, (self.enemy_hpslocation[2], 12))
        WIN.blit(H2, (self.enemy_hpslocation[0], 42))
        WIN.blit(H3, (self.enemy_hpslocation[1], 73))
        WIN.blit(H4, (self.hpslocation[2], 321))
        WIN.blit(H5, (self.hpslocation[0], 351))
        WIN.blit(H6, (self.hpslocation[1], 379))
        WIN.blit(OVERLAY, (0, 0))

        # check if game is over, if so, draw results and ignore the rest of this function
        if not self.gameResult == None:
            result_text = font_large.render(self.gameResult, True, BLACK)
            if self.gameResult == 'WIN':
                WIN.blit(WINSCREEN, (50, 50))
            if self.gameResult == 'LOSE':
                WIN.blit(LOSESCREEN, (50, 50))
            if self.gameResult == 'TIE':
                WIN.blit(DRAWSCREEN, (50, 50))

            pygame.display.update()
            return


        # draw friendly, if picked
        if not choice == None:
            
            if choice == BULBASAUR:

                if self.index1 < 11:
                    self.skip1 = self.skip1 + .5

                    if self.skip1 % 2 == 0:  # used to artificially slow down the animation
                        self.index1 = self.index1 + 1

                    if (self.index1 > 10):
                        self.index1 = 0

                WIN.blit(bulbaB_animation[self.index1], (150, 300))


            elif choice == TOTODILE:

                if self.index1 < 9:
                    self.skip1 = self.skip1 + .5

                    if self.skip1 % 2 == 0:  # used to artificially slow down the animation
                        self.index1 = self.index1 + 1

                    if (self.index1 > 7):
                        self.index1 = 0

                WIN.blit(totoB_animation[self.index1], (150, 300))


            elif choice == TEPIG:
                if self.index1 >= 7:
                    self.index1 = 0
                
                if self.index1 < 7:
                    self.skip1 = self.skip1 + .5
                    if self.index1 > 6:
                        self.index1 = 0

                    if self.skip1 % 2 == 0:  # used to artificially slow down the animation
                        self.index1 = self.index1 + 1

                    if (self.index1 > 4):
                        self.index1 = 0
                    WIN.blit(tepigB_animation[self.index1], (150, 300))


        

        # draw opponent (IF player picked something, and after some delay)
        self._draw_opp()

        # show results of the mtach (IF player AND opp picked, and also after some delay)
        self._draw_results()

        # changed aren't visible until display is updated
        pygame.display.update()


    def _draw_opp(self):

        if self.pokemon_chosen_time == 0:
            return

        # don't do anything for 2 sec after player chooses pokemon
        if self.global_timer - self.pokemon_chosen_time < FPS*2:
            return


        while True:
            if self.enemy_pokemon == None:
                # choose enemy pokemon if didnt do that already
                val = random.randint(0,2)  # 0-2 int again, same as player's pokemon
                self.enemy_pokemon = val
                if val == 0:
                    if soundsLoaded:
                        pygame.mixer.Sound.play(bulbaCry)
                    # print("enemy chose: bulbasaur")
                elif val == 1:
                    if soundsLoaded:
                        pygame.mixer.Sound.play(tepigCry)
                    # print("enemy chose: tepig")
                else:
                    if soundsLoaded:
                        pygame.mixer.Sound.play(totoCry)
                    # print("enemy chose: totodile")

            # if computer tries to use a dead pokemon, simply try again
            if self.enemy_hps[self.enemy_pokemon] <= 0 and not self.results_done:
                self.enemy_pokemon = None
                continue

            # otherwise we are good
            break

        # draw opp

        choice = None
        match(self.enemy_pokemon):
            case 0:
                choice = BULBASAUR
            case 1:
                choice = TEPIG
            case 2:
                choice = TOTODILE
            case default:
                choice = None

        if choice == BULBASAUR:

            if self.index < 11:
                self.skip = self.skip + .5

                if self.skip % 2 == 0:  #used to artificially slow down the animation
                    self.index = self.index + 1

                if(self.index > 10):
                    self.index = 0

            WIN.blit(bulbaF_animation[self.index], (550, 150))

        elif choice == TOTODILE:
            if self.index < 11:
                self.skip = self.skip + .5

                if self.skip % 2 == 0:  # used to artificially slow down the animation
                    self.index = self.index + 1

                if (self.index > 8):
                    self.index = 0

            WIN.blit(totoF_animation[self.index], (550, 150))


        elif choice == TEPIG:
            if self.index < 7:
                self.skip = self.skip + .5
                if self.index > 6:
                    self.index = 0
                if self.skip % 2 == 0:  # used to artificially slow down the animation
                    self.index = self.index + 1

                if (self.index > 6):
                    self.index = 0

                WIN.blit(tepigF_animation[self.index], (550, 150))

    #old
        # after pokemon is drawn, also draw its hp
        # hp_text = font.render(f"{self.enemy_hps[self.enemy_pokemon]}/12", True, BLACK)
        # WIN.blit(hp_text,(550, 100))

    def _draw_results(self):
        if self.pokemon_chosen_time == 0 or self.enemy_pokemon == None:
            return

        # don't do anything for 3 sec (2 sec should have already been waited) after opp chooses their pokemon
        req_time = FPS * 3
        if self.global_timer - self.pokemon_chosen_time < req_time:
            return

        # display victory,tie,loss depending on player and enemy chosen pokemon
        result = None
        if self.desired_pokemon == self.enemy_pokemon:
            text = font.render("Fair Trade!", True, BLACK)
            WIN.blit(text, (360,30))
            result = 'tie'
        elif (self.desired_pokemon +1)%3 == self.enemy_pokemon:
            text = font.render("Enemy Resisted!", True, BLACK)
            WIN.blit(text, (300,30))
            result = 'lose'
        else:
            text = font.render("Super Effective!", True, BLACK)
            WIN.blit(text, (300,30))
            result = 'win'

        
        # adjust health from result of the battle
        if result == 'win' and not self.results_done:
            self.hps[self.desired_pokemon] -= 0
            self.enemy_hps[self.enemy_pokemon] -= 6
            self.enemy_hpslocation[self.enemy_pokemon] -= 36
            if soundsLoaded:
                pygame.mixer.Sound.play(hit)
        elif result == 'lose' and not self.results_done:
            self.hps[self.desired_pokemon] -= 6
            self.enemy_hps[self.enemy_pokemon] -= 0
            self.hpslocation[self.desired_pokemon] -= 36
            if soundsLoaded:
                pygame.mixer.Sound.play(enhit)
        elif result == 'tie' and not self.results_done:
            self.hps[self.desired_pokemon] -= 3
            self.enemy_hps[self.enemy_pokemon] -= 3
            self.hpslocation[self.enemy_pokemon] -= 18
            self.enemy_hpslocation[self.enemy_pokemon] -= 18
            if soundsLoaded:
                pygame.mixer.Sound.play(trade)
        self.results_done = True

        # normalize hp (don't let it go negative)
        if self.hps[self.desired_pokemon] < 0:
            self.hps[self.desired_pokemon] = 0
        if self.enemy_hps[self.enemy_pokemon] < 0:
            self.enemy_hps[self.enemy_pokemon] = 0

        # show the result for 2 seconds, then reset a bunch of stuff (so game repeats)
        # set both pokemon to None, reset time, etc...
        req_time_2 = req_time + (FPS * 2)
        if self.global_timer - self.pokemon_chosen_time < req_time_2:
            return

        # resetting stuff
        self.desired_pokemon = None
        self.enemy_pokemon = None
        self.pokemon_chosen_time = 0
        self.results_done = False

        # check if one team's hp is all zeros (game over)
        playerDead = True
        enemyDead = True
        for i in range(3):
            # if one pokemon has more than 0 hp, that person is not dead
            if not self.hps[i] == 0:
                playerDead = False
            if not self.enemy_hps[i] == 0:
                enemyDead = False

        if playerDead and enemyDead:
            self.gameResult = 'TIE'
            if soundsLoaded:
                pygame.mixer.Sound.stop(battleMusic)
                pygame.mixer.Sound.play(drawMusic)
            print('game over, it was a tie')
        elif playerDead:
            self.gameResult = 'LOSE'
            if soundsLoaded:
                pygame.mixer.Sound.stop(battleMusic)
                pygame.mixer.Sound.play(loseMusic)
            print('game over, you lose.')

        elif enemyDead:
            self.gameResult = 'WIN'
            if soundsLoaded:
                pygame.mixer.Sound.stop(battleMusic)
                pygame.mixer.Sound.play(victoryMusic)
            print('You win!! Congratulations!!')



    def choose_pokemon(self, pokemon):

        if not self.inGame:
            return

        # don't do anything while pokemon exists,
        # do not want to change these values in the middle of a turn
        # desired_pokemon is set back to None after turn is over
        if not self.desired_pokemon == None:
            return

        # if desired pokemon is dead, do nothing
        if self.hps[pokemon] <= 0:
            return

        self.desired_pokemon = pokemon
        self.pokemon_chosen_time = self.global_timer
        if pokemon == 0:
            # print("you chose: bulbasaur")
            if soundsLoaded:
                pygame.mixer.Sound.play(bulbaCry)
        elif pokemon == 1:
            # print("you chose: tepig")
            if soundsLoaded:
                pygame.mixer.Sound.play(tepigCry)
        else:
            # print("you chose: totodile")
            if soundsLoaded:
                pygame.mixer.Sound.play(totoCry)


    # maingame loop
    def run(self):
        clock = pygame.time.Clock()
        #play menu music
        menuMusic.set_volume(.1)
        if soundsLoaded:
            pygame.mixer.Sound.play(menuMusic)
        titlescreen = True
        while(titlescreen):
            global checkt
            checkt = False
            clock.tick(FPS)
            self.global_timer += 1
            # get the position of the mouse
            mouseX, mouseY = pygame.mouse.get_pos()
            # getting the keys pressed
            clicked = False
            # checking events
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    clicked = True
                # if the player quits
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # if the player quits
            # so the user clicked, and by any change the mouse's position was on the buttons
            if (clicked and checkCollisions(mouseX, mouseY, 3, 3, 260, 316, 120, 45)):
                if soundsLoaded:
                    pygame.mixer.Sound.play(select)
                clicked = False
                titlescreen = False
            if (clicked and checkCollisions(mouseX, mouseY, 3, 3, 420, 326, 120, 45)):
                tut = True
                if soundsLoaded:
                    pygame.mixer.Sound.play(select)
                while tut:
                    clock.tick(FPS)
                    self.global_timer += 1
                    # get the position of the mouse
                    mouseX, mouseY = pygame.mouse.get_pos()
                    # getting the keys pressed
                    clicked = False
                    # checking events
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            clicked = True
                        # if the player quits
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                    WIN.blit(TUT1, (50, 50))
                    if (clicked and checkCollisions(mouseX, mouseY, 3, 3, 557, 257, 120, 45)):
                        tut2 = True
                        if soundsLoaded:
                            pygame.mixer.Sound.play(select)
                        while tut2:
                            clock.tick(FPS)
                            self.global_timer += 1
                            # get the position of the mouse
                            mouseX, mouseY = pygame.mouse.get_pos()
                            # getting the keys pressed
                            clicked = False
                            # checking events
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                    clicked = True
                                # if the player quits
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            WIN.blit(TUT2, (50, 50))
                            if (clicked and checkCollisions(mouseX, mouseY, 3, 3, 557, 257, 120, 45)):
                                tut3 = True
                                if soundsLoaded:
                                    pygame.mixer.Sound.play(select)
                                while tut3:
                                    clock.tick(FPS)
                                    self.global_timer += 1
                                    # get the position of the mouse
                                    mouseX, mouseY = pygame.mouse.get_pos()
                                    # getting the keys pressed
                                    clicked = False
                                    # checking events
                                    for event in pygame.event.get():
                                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                            clicked = True
                                        # if the player quits
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            sys.exit()
                                    WIN.blit(TUT3, (50, 50))
                                    if (clicked and checkCollisions(mouseX, mouseY, 3, 3, 557, 257, 120, 45)):
                                        if soundsLoaded:
                                            pygame.mixer.Sound.play(select)
                                        checkt = True
                                        break
                                    pygame.display.update()
                                    if checkt == True:
                                        break
                            pygame.display.update()
                            if checkt == True:
                                break
                    pygame.display.update()
                    if checkt == True:
                        break

            global y
            while y > -360:
                WIN.fill(WHITE)
                WIN.blit(TITLESCREEN, (0,y))
                y = y - .75
                # print(y)
                pygame.display.update()
            WIN.blit(TITLESCREEN, (0, -360))
            pygame.display.update()

        # start music
        if soundsLoaded:
            pygame.mixer.Sound.stop(menuMusic)
            battleMusic.set_volume(.1)
            pygame.mixer.Sound.play(battleMusic)
        # condition to allow exiting the game
        run = True
        self.inGame = True
        while(run):
            # ensures the game runs at the desired frames per second
            clock.tick(FPS)
            self.global_timer += 1

            # get events
            for event in pygame.event.get():
                # if quit event, allow exiting the loop
                if event.type == pygame.QUIT:
                    run = False

            # update the window
            self._draw_window(self.desired_pokemon)
        pygame.quit()



if __name__ == '__main__':

    game = Game()

    # thread to run async task, just sets Game.desired_pokemon after waiting 5 seconds
    # this simulates a return from imageclassifier
    class thread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
    
        def run(self):
            time.sleep(2)
            val = random.randint(0,2)
            game.choose_pokemon(val)

    thread2 = thread();
    thread2.start()


    game.run()
