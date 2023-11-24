for nombres in range (1,20):
    if nombres % 3 == 0:
        print("Fizz")
    
    if nombres % 5 == 0:
        print("Buzz")
    
    if nombres % 3  == 0 and nombres % 5 == 0:
        print("FizzBuzz")
    
    else:
        print(nombres)
    
