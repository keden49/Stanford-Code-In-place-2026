from graphics import Canvas

# each patch is a square with this width and height:
PATCH_SIZE = 100
CANVAS_WIDTH = PATCH_SIZE * 4
CANVAS_HEIGHT = PATCH_SIZE * 2

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # repetitive pattern 

    for r in range(2):
        if r == 0:
            for i in range(0,4,2):
                draw_square_patch(canvas, (i) * PATCH_SIZE, r *PATCH_SIZE)
                draw_circle_patch(canvas, (i + 1)* PATCH_SIZE,r * PATCH_SIZE)
        else: 
            # reverse pattern 
            for i in range(0,4,2):
                draw_square_patch(canvas, (i+1) * PATCH_SIZE, r *PATCH_SIZE)
                draw_circle_patch(canvas, (i)* PATCH_SIZE,r * PATCH_SIZE)
                

def draw_circle_patch(canvas, start_x, start_y):
    end_x = start_x + PATCH_SIZE 
    end_y = start_y + PATCH_SIZE
    canvas.create_oval(start_x,start_y,end_x,end_y, 'salmon')

def draw_square_patch(canvas, start_x, start_y):
    # draws a purple frame at (start_x, start_y)
    
    # size of square 

    end_x = start_x + PATCH_SIZE 
    end_y = start_y + PATCH_SIZE
    canvas.create_rectangle(start_x,start_y,end_x,end_y, 'purple')

    # size of inset 

    SIZE = 20
    top_x = start_x + SIZE 
    top_y = start_y + SIZE
    bottom_x = end_x - SIZE
    bottom_y = end_y - SIZE

    canvas.create_rectangle(top_x,top_y,bottom_x,bottom_y, 'white')




    
    
if __name__ == '__main__':
    main()