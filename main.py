from ast import Pass
import pygame
import random
pygame.init()

class DrawingInfomartion():
    BLACK = 0,0,0
    WHITE = 255,255,255
    GREEN = 0,255,0
    RED = 255,0,0
    BACKGROUND_COLOR = WHITE
    GRADIENTS = [
        (128,128,128),
        (160,160,160),
        (192,192,192)
    ]
    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self,width,height,lst):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_lst(lst)

    def set_lst(self,lst):
        self.lst = lst
        self.max_val = max(lst)
        self.min_val = min(lst)
        self.block_width = round((self.width - self.SIDE_PAD)/ len(lst))
        self.block_height = round((self.height - self.TOP_PAD)/ (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2


def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info):
    lst = draw_info.lst
    for i,val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
        color = draw_info.GRADIENTS[i % 3]
        pygame.draw.rect(draw_info.window,color,(x,y, draw_info.block_width,draw_info.height))


def generate_starting_list(n,max_value,min_value):
    lst = []
    for _ in range(n):
        val = random.randint(min_value,max_value)
        lst.append(val)
    return lst

def main():
    run = True
    clock = pygame.time.Clock()
    n = 60
    min_value = 0
    max_value = 100
    lst = generate_starting_list(n,max_value,min_value)
    draw_info = DrawingInfomartion(800,600,lst)

    while run:
        clock.tick(60)
        pygame.display.update()
        draw(draw_info)

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == "__main__":
    main()
