from itertools import permutations

def cryptarithmetic_solver():
    puzzle = input("Enter the cryptarithmetic puzzle (e.g., 'SEND + MORE = MONEY'): ")
    words = puzzle.split()

    unique_letters = set(''.join(words))
    if len(unique_letters) > 10:
        print("Error: Too many unique letters.")
        return

    digits = list(range(10))
    for perm in permutations(digits, len(unique_letters)):
        digit_map = dict(zip(unique_letters, perm))
        if all(digit_map[word[0]] != 0 for word in words):
            num1 = int(''.join(str(digit_map[c]) for c in words[0]))
            num2 = int(''.join(str(digit_map[c]) for c in words[2]))
            result = int(''.join(str(digit_map[c]) for c in words[4]))
            if num1 + num2 == result:
                print("Solution found:")
                print(puzzle)
                print(f"{words[0]} = {num1}")
                print(f"{words[2]} = {num2}")
                print(f"{words[4]} = {result}")
                return

    print("No solution found.")

cryptarithmetic_solver()
