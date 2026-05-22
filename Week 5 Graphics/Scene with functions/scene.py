from graphics import Canvas
import math
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

CLOUD_WIDTH = 120
CLOUD_HEIGHT = 80

TRUNK_HEIGHT = 80
TRUNK_WIDTH = 20
LEAVES_SIZE = 60

TREE_BOTTOM_Y = CANVAS_HEIGHT - 20 


def main():
    
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_cloud(canvas,20,30,'pink')
    draw_cloud(canvas,160,10,'salmon')
    draw_cloud(canvas,280,25,'purple')
    draw_tree(canvas,70,'green')
    draw_tree(canvas,150,'red')
    draw_tree(canvas,320,'orange')
    draw_ground(canvas)
   
    
def draw_cloud(canvas, x, y, color):
    """
    This function draws one cloud. You can call it and pass in 
    different values of x and y (the location of the cloud) and
    color (the color of the cloud). 
    """
    
    # Top puff 
    # x,y are dimensions related to the canvas 
    
    # centering top puff

    t_puff_x = x + (1/4) * CLOUD_WIDTH
    t_puff_x1 = x + (3/4) * CLOUD_WIDTH

    t_puff_y = y
    t_puff_y1 = y + (2/3) * CLOUD_HEIGHT

    canvas.create_oval(t_puff_x,t_puff_y,t_puff_x1,t_puff_y1,color)

    # Left Puff 
   
    # Occupies 75% to the left leaving 25% unoccupied to the right  
    l_puff_x = x
    l_puff_x1 = x + (3/4) * CLOUD_WIDTH
    l_puff_y = y + (1/3) * CLOUD_HEIGHT
    l_puff_y1 = l_puff_y + (2/3) * CLOUD_HEIGHT # bottom of the cloud area 

    canvas.create_oval(l_puff_x,l_puff_y,l_puff_x1,l_puff_y1,color)

    # Right Puff 
    
    # # Occupies 75% to the right leaving 25% unoccupied to the left  
    r_puff_x = x + (1/4) * CLOUD_WIDTH
    r_puff_x1 = x + CLOUD_WIDTH
    r_puff_y = y + (1/3) * CLOUD_HEIGHT
    r_puff_y1 = y + CLOUD_HEIGHT

    canvas.create_oval(r_puff_x,r_puff_y,r_puff_x1,r_puff_y1,color)

# creating tree trunk
def draw_tree(canvas,x,color):

    # defining dimensions 
    top_x = x
    top_y = TREE_BOTTOM_Y - TRUNK_HEIGHT
    bottom_x = top_x + TRUNK_WIDTH
    bottom_y = top_y + TRUNK_HEIGHT

    canvas.create_rectangle(top_x,top_y,bottom_x,bottom_y,'brown' )

    # drawing leaves on top of trunk
    # leaf dimensions 
    

    top_leave_x = top_x - TRUNK_WIDTH
    top_leave_y = top_y - LEAVES_SIZE + 20 # overlap tree with leaves
    bottom_leave_x = top_leave_x + LEAVES_SIZE
    bottom_leave_y = top_leave_y + LEAVES_SIZE

    canvas.create_oval(top_leave_x,top_leave_y,bottom_leave_x,bottom_leave_y,color)


def draw_ground(canvas):
    """Draws the ground as a rectangle at the bottom of the canvas."""
    canvas.create_rectangle(
        0,
        TREE_BOTTOM_Y,
        CANVAS_WIDTH,
        CANVAS_HEIGHT,
        "green"
    )
    




if __name__ == '__main__':
    main()