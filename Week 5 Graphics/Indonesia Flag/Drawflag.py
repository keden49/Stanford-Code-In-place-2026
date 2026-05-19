from graphics import Canvas
import random

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():

    # canvas area
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    '''define dimensions'''

    # topmost left corner

    top_x = 0
    top_y = 0

    # topmost right corner

    bottom_x = CANVAS_WIDTH 
    bottom_y = CANVAS_HEIGHT / 2

    # specify flag color 

    color = 'red'

    # create rectangle

    canvas.create_rectangle(top_x,top_y,bottom_x,bottom_y, color)

    #create rectangle

    canvas.create_rectangle
    
    

if __name__ == '__main__':
    main()