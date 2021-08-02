def fizzBuzz():
    for num in range(1, 100):
        if num%3 == 0 and num%5 == 0:
            print('fizzbuzz')
            continue
        elif num%3 == 0:
            print('fizz')
            continue
        elif num%5 ==0:
            print('buzz')
            continue
        elif num%3 != 0 and num%5 != 0:
            print(num)
            
        
#the indentation is extremely important in python.
fizzBuzz()
        
