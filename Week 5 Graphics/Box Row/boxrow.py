from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH / N_BOXES

def main():

    # create canvas area 
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    start_height = CANVAS_HEIGHT - BOX_SIZE

    for i in range(N_BOXES):
        # creating dimensions 
        top_x = i * BOX_SIZE
        top_y = start_height
        bottom_x = top_x + BOX_SIZE
        bottom_y = top_y + BOX_SIZE
        
        color = 'white'
        outline = 'black'
        canvas.create_rectangle(top_x,top_y,bottom_x,bottom_y,color,outline)


    
  


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
    
