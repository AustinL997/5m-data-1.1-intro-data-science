# Question 1

# Write a function that prints "Fizz" when the number is divisible by 3, "Buzz" when the number is divisible by 5
# and "FizzBuzz" when the number is divisible by both 3 and 5.
# If the number is not divisible by either 3 or 5, the function should return the number itself.


def fizz_buzz(number): #Question 1
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else: 
        return number 
        

fizz_buzz(3)
fizz_buzz(5)
fizz_buzz(15)


# Question 2

# Write a function that takes a list of numbers and returns the sum of the squares of all the numbers.


def sum_of_squares(numbers): #Question 2
    return sum(n*n for n in numbers)

numbers = [1, 2, 3]
result = sum_of_squares(numbers)
print(result)

numbers = [2,4,6]
result = sum_of_squares(numbers)
print(result)


# Question 3

# Write a function that counts the number of vowels in a string.


def count_vowels(string): #Question 3
    count = 0
    for character in string:
        if character in 'AaEeIiOoUu':
            count += 1
    return count 

string = "Hello"
result = count_vowels(string)
print(result)

string = "aeiou"
result = count_vowels(string)
print(result)


# Question 4

# Write a function that counts the number of repeated characters in a string.


def count_repeats(string): #Question 4
    char_count = {}
    repeated_count = 0
    
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        
    for count in char_count.values():
        if count > 1:
            repeated_count += count
    return repeated_count

print(count_repeats("hello"))
print(count_repeats("aeiou"))


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
