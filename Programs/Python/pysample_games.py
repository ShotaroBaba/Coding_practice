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
    screen.blit(player.image, player.rect)
    allsprites = pygame.sprite.RenderPlain((player))
    pygame.display.flip()
    
    going = True
    while going:
        clock.tick(60)

        # Handling the input events
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            elif event.type ==  KEYDOWN:
                if event.key == K_ESCAPE:
                    going = False
                elif event.key == K_DOWN:
                    player.move_down()
                elif event.key == K_UP:
                    player.move_up()
                elif event.key == K_LEFT:
                    player.move_left()
                elif event.key == K_RIGHT:
                    player.move_right()
        
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