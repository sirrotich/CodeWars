# Return an array containing the numbers from 1 to N, where N is the parametered value. N will never be less than 1 (in C#, N might be less then 1).

# C# ONLY: If N is smaller then or equal to 0, throw an ArgumentOutOfRangeException!
# Replace certain values however if any of the following conditions are met:

# If the value is a multiple of 3: use the value 'Fizz' instead
# If the value is a multiple of 5: use the value 'Buzz' instead
# If the value is a multiple of 3 & 5: use the value 'FizzBuzz' instead
# C# method calling example:

# string[] result = FizzBuzz.GetFizzBuzzArray(3); // => [ "1", "2", "Fizz" ]


def fizzbuzz(n):
    x = []
    if(n > 0):
        i = 1
        while i<= n:
            if(i%3==0) and (i%5==0):
               x.append('FizzBuzz')
            elif(i%5==0):
               x.append('Buzz')
            elif(i%3==0) :
               x.append('Fizz')
            else:
               x.append(i)
            i +=1
        return (x)
        