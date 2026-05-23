from graphics import Canvas
import random

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base


START_HEIGHT = CANVAS_HEIGHT - BRICK_HEIGHT # keeps tarck of pyramid height 


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    build_pyramid(canvas,BRICKS_IN_BASE)
    



'''builds a single layer of bricks'''

def base(canvas,num_bricks):

    # Center base
        
    Lenght_base = BRICK_WIDTH * num_bricks
    

    # brick dimensions
    start_x = (CANVAS_WIDTH - Lenght_base) / 2
    start_x1 = start_x + BRICK_WIDTH
    start_y = START_HEIGHT
    start_y1 = start_y + BRICK_HEIGHT

    # draw base pyramids

    for i in range(num_bricks):

        canvas.create_rectangle(start_x,start_y,start_x1,start_y1,'yellow','black')

        # create bricks at different positions 

        start_x += BRICK_WIDTH
        start_x1 += BRICK_WIDTH

''' builds stacks of bricks to form a pyramid '''

def build_pyramid(canvas,num_bricks):
    global START_HEIGHT # refers to the general starting position
    
    
    # stops building  when bricks are over 
    # at each call builds a single layer 
    while num_bricks > 0:
        
        base(canvas,num_bricks)
        num_bricks = num_bricks - 1  # decrease bricks by 1 
        START_HEIGHT = START_HEIGHT - BRICK_HEIGHT # moves height upwards



    

if __name__ == '__main__':
    main()