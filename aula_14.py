import pygame
# vermelho = "red"
# branco = "white"
# pygame.init()

# tela = pygame.display.set_mode((1920,980))
# tela.fill((255,0,0))
# pygame.display.flip()

# while True :
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#             pygame.quit()
#         tela.fill("black")
#         pygame.draw.rect(tela , vermelho , (750,350,375,250))
#         pygame.display.flip()

#         pygame.draw.circle(tela,branco,(750,150),100,0)
#         pygame.display.flip()
#         pygame.draw.ellipse(tela,("yellow"),(750,650,400,250))
#         pygame.display.flip()


vermelho = "red"
branco = "white"
pygame.init()

tela = pygame.display.set_mode((1920,980))
quadrado = pygame.Rect(250,250,50,50)
clock = pygame.time.Clock()

run = True
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                quadrado.move_ip([50,0])
            if event.key == pygame.K_LEFT:
                quadrado.move_ip([-50,0])
            if event.key == pygame.K_DOWN:
                quadrado.move_ip([0,50])
            if event.key == pygame.K_UP:
                quadrado.move_ip([0,-50])   


    tela.fill("white")
    pygame.draw.rect(tela , vermelho , quadrado)
    pygame.display.update()
