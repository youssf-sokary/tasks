import random
words = ["apple" , "banana" , "cherry" , "date" , "elderberry"]
original_word = random.choice(words)
scrambled_word = ''.join(random.sample(original_word,len(original_word)))
print("welcome to the world scramble game")
print(f"try to guess the original word from the scramled word: {scrambled_word} ")

attempts = 5

while attempts > 0:
    guess = input("enter your guess: ").strip()

    if not guess :
        print("wrong input")

        continue
    if guess == original_word:
        print("congratulations you won!")
        break

    else:
        attempts -= 1

        print(f"inccorect try again you have {attempts} attempts left")

    if attempts == 0 :
        print(f"game over the original word was {original_word}")
    