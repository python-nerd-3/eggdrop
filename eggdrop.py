import pygame
import os
from random import choice
from time import sleep
chickenTx = os.path.join("resources", "bgock.png")
eggTx = os.path.join("resources", "eggy.png")
nestTx = os.path.join("resources","nest.png")
nyoomTx = os.path.join("resources","nyoom.ogg")
explosionTx = os.path.join("resources","explosion.ogg")
powerupTx = os.path.join("resources", "powerup.ogg")
fontTx = os.path.join("resources","font.ttf")
#use tuple, not 2 args
pygame.init()
win = pygame.display.set_mode((1000,pygame.display.Info().current_h - 50))
splashes = ["nyoom", "best game of 2012","free download","banana","i got the chicken from roblox","no malware", "(not) for the nintendo 2DS","1 million downloads","我是狗","bundled with pointless black square (no longer pointless)", "return of the jedi", "also try cell machine", " FREE!!!!", "i ran out of ideas","the chicken goes at 0.03 miles per hour"]
pygame.display.set_caption("egg drop: {c}".format(c = choice(splashes)))
chicken = pygame.image.load(chickenTx)
pygame.display.set_icon(chicken)
eggt = pygame.image.load(eggTx)
chicken = pygame.transform.scale(chicken, (200,200))
eggt = pygame.transform.scale(eggt, (55,75))
nyoom = pygame.mixer.Sound(nyoomTx)
explosion = pygame.mixer.Sound(explosionTx)
music = pygame.mixer.music.load(powerupTx)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
print("i didnt ask pygame community")
offset = 150

#NoObligatoryOrginization
def main():
    global direc
    global chicken
    global nest
    global offset
    s = int(0)
    eggs = []
    hp = 4
    direc = 1
    r = True
    m = True
    chickenBox = pygame.Rect(0,300,200,200)
    sadbox = pygame.Rect(800,0,200,200)
    nestBox = pygame.Rect(choice(range(0,831)),pygame.display.Info().current_h - 80,154,92)
    nest = pygame.image.load(nestTx)
    nest = pygame.transform.scale(nest, (nest.get_width() / 2, nest.get_height() / 2))
    healthBox = pygame.Rect(800,200,200,50)
    playBox = pygame.Rect(400,600,200,200)
    while r:
        for event in pygame.event.get():
            #list of events
            if event.type == pygame.QUIT: #name of event = capital
                r = False
            if event.type == pygame.KEYDOWN and m == False:
                if event.key == pygame.K_SPACE:
                    print("egg")
                    egg = pygame.Rect(chickenBox.x + offset,chickenBox.y + 150,55,75)
                    eggs.append([egg,0])
                    pygame.mixer.Sound.play(nyoom)
                if event.key == pygame.K_LALT or event.key == pygame.K_RALT:
                    print("j")
                    if offset == 150:
                        offset = 0
                    elif offset == 0:
                        offset = 150
                    chicken = pygame.transform.flip(chicken, True, False)
            if event.type == pygame.MOUSEBUTTONDOWN and m == True:
                if 600 <= pygame.mouse.get_pos()[1]  <= 800 and 400 <= pygame.mouse.get_pos()[0] <= 600:
                    m = False
        win.fill((127,127,127))
        win.blit(nest,(nestBox.x,nestBox.y))
        for e in eggs:
            e[0].y += e[1]
            e[1] += 0.02
            win.blit(eggt,(e[0].x,e[0].y))
            if nestBox.x + 10 <= e[0].centerx <= nestBox.x + nestBox.width - 10 and e[0].y >= pygame.display.Info().current_h - 130:
                print("score")
                eggs.remove(e)
                nestBox.x = choice(range(0,1000 - nestBox.width))
                s += 1
                nestBox.width -= 1
                nest = pygame.transform.scale(nest, (nest.get_width() - 1, nest.get_height()))
                if s == 144:
                    print("you win")
            if e[0].y >= pygame.display.Info().current_h:
                eggs.remove(e)
                hp -= 1
        win.blit(chicken, (chickenBox.x, chickenBox.y))
        chickenBox.x += direc
        if chickenBox.x == 800:
            direc = -1
        elif chickenBox.x == 0:
            direc = 1
        pygame.draw.rect(win,(0,0,0),sadbox)
        text = pygame.font.Font(fontTx, 64).render(str(s), True, (255,255,255), (0,0,0))
        text2 = pygame.font.Font(fontTx, 64).render("Play", True, (0,0,0), (0,255,0))
        txtRc = text.get_rect()
        txtRc.center = (900, 100)
        win.blit(text, txtRc)
        text2Rc = text2.get_rect()
        text2Rc.center = (500,700)
        healthBox.width = hp * 50
        pygame.draw.rect(win,(255,0,0),healthBox)
        if m == True:
            pygame.draw.rect(win,(0,255,0),playBox)
            win.blit(text2,text2Rc)
        pygame.display.update()
        if hp == 0:
            break
    if r == False:
        pygame.quit()
    elif hp == 0:
        txt = pygame.font.Font(fontTx, 150).render("you exploded", True, (255,0,0), (0,0,0))
        textRc = txt.get_rect()
        textRc.center = (500,500)
        win.blit(txt, textRc)
        pygame.mixer.Sound.play(explosion)
        pygame.display.update()
        sleep(1)
        main()

if __name__ == "__main__":
    main() #holy cow sully uses __name__ = __main__ for once
