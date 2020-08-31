import os

IMAGE_SIZE = 200
SCREEN_SIZE = 512
NUM_TILES_SIDE = 4
NUM_TILES_TOTAL = 16
MARGIN = 6

CAR_DIR = 'images'
CAR_FILES = [x for x in os.listdir(CAR_DIR) if x[-3:].lower() == 'png']

assert len(CAR_FILES) == 8