import os
import random
import game_config as gc

from pygame import image, transform

car_count = {}
for x in gc.CAR_FILES:
    car_count[x] = 0

def available_car():
    return [a for a,c in car_count.items() if c < 2]

class car:
    def __init__(self, index):
        self.index = index
        self.row = index // gc.NUM_TILES_SIDE
        self.col = index % gc.NUM_TILES_SIDE
        self.name = random.choice(available_car())
        car_count[self.name] += 1

        self.image_path = os.path.join(gc.CAR_DIR,self.name)
        self.image = image.load(self.image_path)
        self.image = transform.scale(self.image, (gc.IMAGE_SIZE - 2*gc.MARGIN,gc.IMAGE_SIZE - 2*gc.MARGIN))
        self.box = self.image.copy()
        self.box.fill((100,200,100))
        self.skip = False