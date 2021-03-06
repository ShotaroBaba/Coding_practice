# Import Modules
import os, pygame
from pygame.locals import *
from pygame.compat import geterror
import time
from random import randint

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

# Load data for generating image on the screen.
data_dir = "../data/test_game_data"

bullet_pos_pad_height = -20
enemy_shoot_interval = 500
enemy_generate_interval = 800
out_of_screen_margin = 80


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
# Will be added later.
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

# Bullet class
class Bullet(pygame.sprite.Sprite):
    # Later the move value might be added for
    # achieving flexibility.
    def __init__(self, player_rect, pos_pad = (-20, -20), bullet_image = "bullet.png"):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(bullet_image, -1)
        screen = pygame.display.get_surface()
        self.mask = pygame.mask.from_surface(self.image)
        self.area = screen.get_rect()
        new_pos = self.rect.move((player_rect.right + pos_pad[0], player_rect.top - pos_pad[1]))
        self.rect = new_pos

    # Move left every time
    # TODO: Bullet can track the movement of the player.
    def update(self, left_or_right):
        if left_or_right == "right":
            newpos = self.rect.move((1, 0))
            self.rect = newpos
            if self.rect.right > self.area.right or \
            self.rect.left < self.area.left or \
            self.rect.bottom > self.area.bottom or \
            self.rect.top < self.area.top:
                self.kill()
        elif left_or_right == "left":
            newpos = self.rect.move((-3, 0))
            self.rect = newpos
            if self.rect.right > self.area.right or \
            self.rect.left < self.area.left or \
            self.rect.bottom > self.area.bottom or \
            self.rect.top < self.area.top:
                self.kill()

    def hit(self):
        self.count += 1
        # enemy defeated if a certain number of bullet are hit.
        if(self.count > self.num_count):
            self.kill()
            del self

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('player.png', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.num_count = 10
        self.count = 0

        # TODO: Implement level up later
        self.power_up = 0

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

    def hit(self):
        self.count += 1
        # Player is defeated if a certain number of bullet are hit.
        if(self.count > self.num_count):
            self.kill()
            del self

# If enemy is normal, then it is counted as 10.
class Enemy(pygame.sprite.Sprite):
    def __init__(self, num_count = 10, rect_random = False):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('enemy.png', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        newpos = self.rect.move((self.area.right - self.rect.right + out_of_screen_margin,0))
        self.rect = newpos
        if rect_random:
            self.rect.y = randint(0, self.area.bottom - self.area.top - (self.rect.bottom - self.rect.top))
        self.count = 0
        self.num_count = num_count
        self.out_of_screen_left = self.area.left - out_of_screen_margin
    
    def update(self):
        newpos = self.rect.move((-1, 0))
        self.rect = newpos
        if self.rect.left < self.out_of_screen_left:
            newpos = self.rect.move((self.area.right - self.rect.right + out_of_screen_margin,0))
            self.rect = newpos
            self.rect.y = randint(0, self.area.bottom - self.area.top - (self.rect.bottom - self.rect.top))


    def hit(self):
        self.count += 1
        # enemy defeated if a certain number of bullet are hit.
        if(self.count > self.num_count):
            self.kill()
            del self

def main():

    # Background is black.
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
    player_sprites = pygame.sprite.RenderPlain((player))
    enemy_sprites = pygame.sprite.RenderPlain((enemy))
    player_bullet_sprites = pygame.sprite.RenderPlain(())
    enemy_bullet_sprites = pygame.sprite.RenderPlain(())
    pygame.display.flip()
    
    # Set user events and timer
    enemy_shoot_event = USEREVENT + 1
    difficulty_up_event = USEREVENT + 2
    enemy_added_event = USEREVENT + 3

    # Set the timers for these events
    pygame.time.set_timer(enemy_shoot_event, enemy_shoot_interval)
    pygame.time.set_timer(enemy_added_event, enemy_generate_interval)

    going = True
    count = 0
    while going:
        clock.tick(70)

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
            player_bullet_sprites.add(Bullet(player.rect))
        
        # Handling the input events
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            
            # Shoot every 0.5 seconds.
            if event.type == enemy_shoot_event:
                for ene in enemy_sprites.sprites():
                    enemy_bullet_sprites.add(Bullet(ene.rect, (-30, -15), "enemy_bullet.png"))
            if event.type == enemy_added_event:
                enemy_sprites.add(Enemy(rect_random = True))

        # Enemy move
        for ene in enemy_sprites.sprites():
            ene.update()

        # Check whether the player bullet is hit by the enemy.
        for i in pygame.sprite.groupcollide(enemy_sprites, player_bullet_sprites, dokilla = False, dokillb = True, collided = pygame.sprite.collide_mask).keys():
            i.hit()

        # If the player is hit by the enemy, then it will disappear
        pygame.sprite.groupcollide(enemy_sprites, player_sprites, dokilla = True, dokillb = True, collided = pygame.sprite.collide_mask)
        
        # Check whether the enemy bullet is hit by the player.
        if pygame.sprite.spritecollide(player, enemy_bullet_sprites, True, collided = pygame.sprite.collide_mask) != []:
            player.hit()

        if len(enemy_sprites.sprites()) == 0:
            enemy_sprites.add(Enemy(rect_random = True))

        # Update locations
        player_sprites.update()
        enemy_sprites.update()
        player_bullet_sprites.update("right")
        enemy_bullet_sprites.update("left")
        
        # Collided with enemy
        screen.blit(background, (0, 0))

        player_sprites.draw(screen)
        enemy_sprites.draw(screen)
        player_bullet_sprites.draw(screen)
        enemy_bullet_sprites.draw(screen)
        pygame.display.flip()
    
    pygame.quit()

if __name__ == '__main__':
    main()


# Reference:
# Magimel, F., & Kluyver, T. (2019). chimp.py (Version 1.9.6) [Computer Software]. 
#   Retreived from https://github.com/pygame/pygame/blob/master/examples/chimp.py