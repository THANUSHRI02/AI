import random

def getDigits(num):
    return [int(i) for i in str(num)]

def noDuplicates(num):
    num_li = getDigits(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False

def generateNum():
    while True:
        num = random.randint(1000, 9999)
        if noDuplicates(num):
            return num

def numOfBullsCows(num, guess):
    bull_cow = [0, 0]
    num_li = getDigits(num)
    guess_li = getDigits(guess)
    used_digits = set()
    
    for i, j in zip(num_li, guess_li):
        if j in num_li:
            if j == i:
                bull_cow[0] += 1
                used_digits.add(j)
            elif j not in used_digits:
                bull_cow[1] += 1
    
    return bull_cow

def heuristicFunction(possible_nums, previous_guess, bull_cow):
    prev_bulls, prev_cows = bull_cow
    guess_digits = getDigits(previous_guess)
    digit_counts = [0] * 10
    
    for num in possible_nums:
        for digit in getDigits(num):
            digit_counts[digit] += 1
    
    for digit in guess_digits:
        if digit == prev_bulls:
            possible_nums = [num for num in possible_nums if getDigits(num) == guess_digits]
        elif digit == prev_cows:
            possible_nums = [num for num in possible_nums if getDigits(num) != guess_digits]
        else:
            possible_nums = [num for num in possible_nums if digit in getDigits(num)]
    
    return possible_nums

# Secret Code
num = generateNum()
possible_numbers = list(range(1000, 10000))
print("WELCOME TO SECRET NUMBER GAME")
print("RULES")
print("It should be a 4 digit number")
print("Number should not have repeated digits")
print("Bulls denotes the number of digits in correct position")
print("Cows denotes the number of digits that have been guessed correctly")
tries = int(input('Enter number of tries: '))

while tries > 0:
    guess = int(input("Enter your guess: "))
    
    if not noDuplicates(guess):
        print("Number should not have repeated digits. Try again.")
        continue
    if guess < 1000 or guess > 9999:
        print("Enter 4 digit number only. Try again.")
        continue
    
    bull_cow = numOfBullsCows(num, guess)
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
    tries -= 1
    
    if bull_cow[0] == 4:
        print("You guessed right!")
        break
    
    possible_numbers = heuristicFunction(possible_numbers, guess, bull_cow)
    print(f"Remaining possible numbers: {possible_numbers}")
    print(f"Number of possible numbers: {len(possible_numbers)}")
    
else:
    print(f"You ran out of tries. Number was {num}")
