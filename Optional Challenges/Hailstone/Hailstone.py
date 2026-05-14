def main():
    n = int(input("Enter a number: "))
   
    '''program run until n = 1'''
    while n != 1:
        
        '''prints different statements depending on wheter n is odd or even
           which is validated by n % 2 == 0 because even numbers have a remainder of 0'''
        print(f"{n} is even, so I take half: {n//2}" if n % 2 == 0 else f"{n} is odd, so I make 3n + 1: {3*n + 1}" )
        
        
        # reassigning n
        if n % 2 == 0:
            n = n // 2 
        else:
            n = 3 * n + 1 
   
     

if __name__ == "__main__":
    main()