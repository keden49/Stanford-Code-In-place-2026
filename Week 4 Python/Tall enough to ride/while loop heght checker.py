"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""
min_height = 50
def main():
    while True:
        height =int(input("How tall are you? "))
        #print("You're tall enough to ride!" if height >= min_height else "You're not tall enough to ride, but maybe next year!")
        if height < min_height:
            print("You're not tall enough to ride, but maybe next year!")
            print("Try again ...")
            #loop restarts again
        else:
            print("You're tall enough to ride!")
            break #exist the while loop once min_height is satisfied 


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()