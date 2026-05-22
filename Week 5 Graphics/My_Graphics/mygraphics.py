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
user_inp = input("Which weather would you like to see? (Sunny or Rainy)? ").lower()
while user_inp not in ['sunny','rainy']:
    user_inp = input("Please enter between sunny or rainy: ").lower()

'''
This code visualizes a rainy or sunny day through graphics
'''

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    NUM_CLOUDS = 25
    NUM_TREES = 10
    random.seed(30)
    
    # ground 

    draw_ground(canvas)
    
    if user_inp == 'rainy':
        create_sky(canvas)
        draw_ground(canvas)
        for _ in range(NUM_CLOUDS):
        
            x = random.randint(0,CANVAS_WIDTH)
            y = random.randint(0,CANVAS_HEIGHT//4)
            color = get_cloud_color()
            draw_cloud(canvas,x,y,color)
        
        
        draw_moon(canvas)
        draw_cloud(canvas,120,15,'grey') # centre cloud


        
        
        #forest
        for i in range(10):
            if i == 0:
                x = 0
            # layer 1 of forest
            x = min(x + 40,CANVAS_WIDTH)
            color = get_tree_color()
            draw_tree(canvas,x,color)
            # layer 2 of forest
            x = min(x+30,CANVAS_WIDTH)
            draw_tree(canvas,x,color)
        raindrops(canvas)
        

    
    # sunny day 
    else:
        create_sky(canvas)
        
        for _ in range(10):

            x = random.randint(0,CANVAS_WIDTH)
            y = random.randint(0,CANVAS_HEIGHT//3)
            color = 'white'
            draw_cloud(canvas,x,y,color)
        draw_sun(canvas,(1/4)*CANVAS_WIDTH,10) #sun at the end to avoid being hidden
        draw_cloud(canvas, 90, 12, 'white') #cloud to cover sun
        draw_ground(canvas) # ground 

    #forest
        for i in range(10):
            if i == 0:
                x = 0
            # layer 1 of forest
            x = min(x + 40,CANVAS_WIDTH)
            color = get_tree_color()
            draw_tree(canvas,x,color)
            # layer 2 of forest
            x = min(x+30,CANVAS_WIDTH)
            draw_tree(canvas,x,color)
            
        

    # cluster of grey clouds 
    
    
    
def create_sky(canvas):
    
    color = "azure" if user_inp == 'sunny' else 'black'
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, color)
   
    
def draw_cloud(canvas, x, y, color):
    
    
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

def draw_sun(canvas,x,y):
    diameter = 50
    top_sun_x = x
    bottom_sun_x1 = top_sun_x + diameter
    top_sun_y = y
    bottom_sun_y1 = top_sun_y + diameter

    canvas.create_oval(top_sun_x,top_sun_y,bottom_sun_x1,bottom_sun_y1,'yellow')


def get_cloud_color():
    cloud_colors = [
    'dark grey',
    'grey',
    'slate grey',
    'dim grey',
    'dark slate grey',
    'light grey',
    'grey',
    'grey']

    return random.choice(cloud_colors)

def get_tree_color():
    tree_colors = [
    'dark green',
    'forest green',
    'dark green',
    'dark green',
    'lime green',
    'yellow green',
    'medium sea green',
    'pale green',
    'olive drab',
    'dark sea green',
    'forest green']

    return random.choice(tree_colors)

def raindrops(canvas):
    for _ in range(80):  # 50 raindrops
        x = random.randint(0, CANVAS_WIDTH)
        y = random.randint(20, CANVAS_HEIGHT)
        canvas.create_line(x, y, x-5, y+10, 'light slate grey')


def draw_ground(canvas):
    """Draws the ground as a rectangle at the bottom of the canvas."""
    canvas.create_rectangle(
        0,
        TREE_BOTTOM_Y,
        CANVAS_WIDTH,
        CANVAS_HEIGHT,
        "green"
    )

def draw_moon(canvas):
    canvas.create_oval(100,5,170,75,'white')

if __name__ == '__main__':
    main()