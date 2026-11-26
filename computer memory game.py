
import random
import time

sequence = []

print("Welcome to Memory Game!")

for i in range(5):

    number = random.randint(1, 9)
    sequence.append(number)

    print("Remember these numbers:")
    print(sequence)

    time.sleep(2)

    print("\n" * 30)

    answer = input("Enter the complete sequence: ")

    user_sequence = [int(x) for x in answer.split()]

    if user_sequence == sequence:
        print("Correct! Well done!")
    else:
        print("Wrong sequence!")
        print("Correct sequence:", sequence)
        break

print("Game over!")
