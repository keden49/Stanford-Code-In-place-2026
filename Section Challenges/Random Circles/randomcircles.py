from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20

def main():
    print('Random Circles')
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for _ in range(N_CIRCLES):
         draw_circle(canvas)

   
    
def random_color():
    """
    This is a function to use to get a random color for each circle. We have
    defined this for you and there is no need to edit code in this function,
    but feel free to read it over if you are interested. 
    """
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)

def draw_circle(canvas):

    color = random_color() # get random color 
    # limit the top left coordinates to the Canvas Dimensions 
    top_x = random.randint(0,CANVAS_WIDTH)
    top_y = random.randint(0,CANVAS_HEIGHT)

    canvas.create_oval(top_x,top_y,top_x + CIRCLE_SIZE,top_y + CIRCLE_SIZE,color)

if __name__ == '__main__':
    main()