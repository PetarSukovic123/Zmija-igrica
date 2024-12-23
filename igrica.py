import pygame
import time
import random

pygame.init()

širina = 800
visina = 600

bijela = (255, 255, 255)
crna = (0, 0, 0)
crvena = (213, 50, 80)
zelena = (0, 255, 0)
plava = (50, 153, 213)

velicina_bloka = 20
brzina_zmije = 15

ekran = pygame.display.set_mode((širina, visina))
pygame.display.set_caption("Zmija")

sat = pygame.time.Clock()

stil_fonta = pygame.font.SysFont("bahnschrift", 25)
rezultat_font = pygame.font.SysFont("comicsansms", 35)

def tvoj_rezultat(rezultat):
    vrijednost = rezultat_font.render("Rezultat: " + str(rezultat), True, plava)
    ekran.blit(vrijednost, [0, 0])

def nasa_zmija(velicina_bloka, lista_zmije):
    for x in lista_zmije:
        pygame.draw.rect(ekran, zelena, [x[0], x[1], velicina_bloka, velicina_bloka])

def poruka(poruka, boja):
    por = stil_fonta.render(poruka, True, boja)
    ekran.blit(por, [širina / 6, visina / 3])

def igra():
    kraj_igre = False
    zatvaranje = False

    x1 = širina / 2
    y1 = visina / 2

    promjena_x1 = 0
    promjena_y1 = 0

    lista_zmije = []
    duzina_zmije = 1

    hrana_x = round(random.randrange(0, širina - velicina_bloka) / 20.0) * 20.0
    hrana_y = round(random.randrange(0, visina - velicina_bloka) / 20.0) * 20.0

    while not kraj_igre:

        while zatvaranje:
            ekran.fill(crna)
            poruka("Izgubio si! Pritisni Q za izlaz ili C za novu igru", crvena)
            tvoj_rezultat(duzina_zmije - 1)
            pygame.display.update()

            for dogadjaj in pygame.event.get():
                if dogadjaj.type == pygame.KEYDOWN:
                    if dogadjaj.key == pygame.K_q:
                        kraj_igre = True
                        zatvaranje = False
                    if dogadjaj.key == pygame.K_c:
                        igra()

        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                kraj_igre = True
            if dogadjaj.type == pygame.KEYDOWN:
                if dogadjaj.key == pygame.K_LEFT:
                    promjena_x1 = -velicina_bloka
                    promjena_y1 = 0
                elif dogadjaj.key == pygame.K_RIGHT:
                    promjena_x1 = velicina_bloka
                    promjena_y1 = 0
                elif dogadjaj.key == pygame.K_UP:
                    promjena_y1 = -velicina_bloka
                    promjena_x1 = 0
                elif dogadjaj.key == pygame.K_DOWN:
                    promjena_y1 = velicina_bloka
                    promjena_x1 = 0

        if x1 >= širina or x1 < 0 or y1 >= visina or y1 < 0:
            zatvaranje = True
        x1 += promjena_x1
        y1 += promjena_y1
        ekran.fill(crna)
        pygame.draw.rect(ekran, crvena, [hrana_x, hrana_y, velicina_bloka, velicina_bloka])
        glava_zmije = []
        glava_zmije.append(x1)
        glava_zmije.append(y1)
        lista_zmije.append(glava_zmije)
        if len(lista_zmije) > duzina_zmije:
            del lista_zmije[0]

        for x in lista_zmije[:-1]:
            if x == glava_zmije:
                zatvaranje = True

        nasa_zmija(velicina_bloka, lista_zmije)
        tvoj_rezultat(duzina_zmije - 1)

        pygame.display.update()

        if x1 == hrana_x and y1 == hrana_y:
            hrana_x = round(random.randrange(0, širina - velicina_bloka) / 20.0) * 20.0
            hrana_y = round(random.randrange(0, visina - velicina_bloka) / 20.0) * 20.0
            duzina_zmije += 1

        sat.tick(brzina_zmije)

    pygame.quit()
    quit()

igra()