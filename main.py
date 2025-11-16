import starterscreen
import pygame
class main():
    def __init__(self):
        pygame.init()

        window_x =720
        window_y = 500

        self.clock = pygame.time.Clock()

        self.window = pygame.display.set_mode((window_x, window_y))

        main.run(self)

    def run(self):

        run = True
        while run:

            if starterscreen.start().startin == True:
                self.logo = self.window.blit(starterscreen.start().startingbackground, (-240, -300))
                pygame.draw.rect(self.window, (255, 255,255), (720//2-150, 500/2-50, 300, 100))
                pygame.draw.rect(self.window, (255,255,255), (720//2-150, 500//2+100, 300, 100))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click_pos = event.pos


            pygame.display.update()
            self.clock.tick(30)

main()
