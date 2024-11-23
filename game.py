import pygame

pygame.init()

window = pygame.display.set_mode((700,500))
pygame.display.set_caption("лабіринт")

background = pygame.transform.scale(pygame.image.load("background.jpg"),(700,500))
# player = pygame.transform.scale(pygame.image.load("heeo.png"),(50,50))
# enemy = pygame.transform.scale(pygame.image.load("cyborg.png"),(50,50))
# treasure = pygame.transform.scale(pygame.image.load("treasure.png"),(50,50))

game_over = False

clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load('jungles.ogg')
pygame.mixer.music.play()

kick = pygame.mixer.Sound("kick.ogg")

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image,player_x=0,player_y=0,player_speed=5):
        self.image = pygame.transform.scale(pygame.image.load(player_image),(65,65))
        self.rect = self.image.get_rect()
        self.x=player_x
        self.y=player_y
        self.speed = player_speed

    def draw(self):
        window.blit(self.image,(self.x,self.y))

player = GameSprite("hero.png",0,0,10)
enemy = GameSprite("cyborg.png",100,100,15)
treasure = GameSprite("treasure.png",200,200,5)

while not game_over:
    window.blit(background,(0,0))

    player.draw()
    enemy.draw()
    treasure.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pygame.display.update()
    clock.tick(60)

pygame.quit()