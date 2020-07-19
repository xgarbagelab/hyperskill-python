import random

languages = ['python', 'java', 'kotlin', 'javascript']
language = random.choice(languages)
lives = 8
correct_guess = ""
said = ""
hint = "-" * len(language)
print("H A N G M A N\n")
while True:
    choice = input("\nType \"play\" to play the game, \"exit\" to quit:")
    if choice == "exit":
        break
    elif choice == "play":
        while lives > 0:
            print("\n" + hint)
            guess = input("Input a letter: ")
            if len(guess.strip()) > 1:
                print("You should input a single letter")
                continue
            elif not guess.islower():
                print("It is not an ASCII lowercase letter")
                continue
            if guess in said:
                print("You already typed this letter")
                continue
            if guess in language:
                if guess not in said:
                    new_hint = [char if char == guess or char in correct_guess else "-" for char in language]
                    hint = ''.join(new_hint)
                    correct_guess += guess
            else:
                print("No such letter in the word")
                lives -= 1
            said += guess
            if set(correct_guess) == set(language):
                print("You guessed the word!")
                print("You survived!")
                break
            elif lives < 1:
                print("You are hanged!")
                break
