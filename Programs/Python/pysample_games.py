# Import Modules
import os, pygame
from pygame.locals import *
from pygame.compat import geterror
import time
if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

# Load data for generating image on the screen.
data_dir = "../data/test_game_data"


# Method to load image [1]
def load_image(name, colorkey=None):
    fullname = os.path.join(data_dir, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print('Cannot load image:', fullname)
        raise SystemExit(str(geterror()))
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

# Method to load sound [1]
def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join(data_dir, name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print('Cannot load sound: %s' % fullname)
        raise SystemExit(str(geterror()))
    return sound


class Bullet(pygame.sprite.Sprite):
    def __init__(self, player_rect):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('bullet.png', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        
        new_pos = self.rect.move((player_rect.right, player_rect.top - 10))
        self.rect = new_pos

    def update(self):
        newpos = self.rect.move((1, 0))
        self.rect = newpos
        # if self.rect.left > self.area.left:
        #     newpos = self.rect.move((self.area.right - self.rect.right,0))
        #     self.rect = newpos



# class EnemyBullet(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image, self.rect = load_image('player.png', -1)
#         screen = pygame.display.get_surface()
#         self.area = screen.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('player.png', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

    def move_down(self):
        if self.rect.bottom < self.area.bottom:
            newpos = self.rect.move((0, 1))
            self.rect = newpos
    
    def move_up(self):
        if self.rect.top > self.area.top:
            newpos = self.rect.move((0, -1))
            self.rect = newpos
        
    def move_left(self):
        if self.rect.left > self.area.left:
            newpos = self.rect.move((-1, 0))
            self.rect = newpos
    
    def move_right(self):
        if self.rect.right < self.area.right:
            newpos = self.rect.move((1, 0))
            self.rect = newpos

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('enemy.png', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

        newpos = self.rect.move((self.area.right - self.rect.right,0))
        self.rect = newpos

    def update(self):
        newpos = self.rect.move((-1, 0))
        self.rect = newpos
        if self.rect.left < self.area.left:
            newpos = self.rect.move((self.area.right - self.rect.right,0))
            self.rect = newpos


def main():

    black = (0, 0, 0)
    # Conduct Initialization
    pygame.init()
    screen = pygame.display.set_mode((600, 480))

    # Create background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(black)

    # Show background
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Initialise everything here...
    clock = pygame.time.Clock()
    player = Player()
    enemy = Enemy()
    screen.blit(player.image, player.rect)
    allsprites = pygame.sprite.RenderPlain((player, enemy))
    pygame.display.flip()
    
    going = True
    while going:
        clock.tick(60)

        key_state = pygame.key.get_pressed()

        if key_state[K_ESCAPE]:
            going = False
        if key_state[K_UP]:
            player.move_up()
            # player.move_down()
        if key_state[K_DOWN]:
            player.move_down()
            # player.move_up()
        if key_state[K_LEFT]:
            player.move_left()
            # player.move_left()
        if key_state[K_RIGHT]:
            player.move_right()  
            # player.move_right()
        if key_state[K_SPACE]:
            temp_rect = player.rect
            allsprites.add(Bullet(temp_rect))

        # Handling the input events
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False


        enemy.update()

        allsprites.update()
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()
    
    pygame.quit()

if __name__ == '__main__':
    main()


# Reference:
# Magimel, F., & Kluyver, T. (2019). chimp.py (Version 1.9.6) [Computer Software]. 
#   Retreived from https://github.com/pygame/pygame/blob/master/examples/chimp.py