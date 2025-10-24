import random
from colorama import init, Fore, Style

init(autoreset=True)

with open("words.txt", 'r', encoding='utf8') as f:
    words = [word.strip().lower() for word in f.readlines()]

word = random.choice(words)
word_list = list(word)
guessed = False

letter_display = [f"{Fore.WHITE}■{Style.RESET_ALL}" for _ in range(5)]

print("A 5-letter word has been generated!")

print(" ".join(letter_display))

print()

count = 0
max_count = 6

bad_letters = set()

while not guessed and count < max_count:
  
    word_guess = input(f"Attempt {count + 1}/{max_count} - Enter your guess: ").lower()
    
    if word_guess not in words:
        print(f"{Fore.RED}Please enter an existing word.\n")
        continue
    
    if len(word_guess) != 5:
        print(f"{Fore.RED}Word must be 5 letters long.\n")
        continue

    count += 1
    word_guess_list = list(word_guess)
    
    current_display = []
    
    for i, letter in enumerate(word_guess_list):
        if letter == word_list[i]:
            current_display.append(Fore.GREEN + letter + Style.RESET_ALL)
        elif letter in word_list:
            current_display.append(Fore.YELLOW + letter + Style.RESET_ALL)
        else:
            current_display.append(Fore.WHITE + "■" + Style.RESET_ALL)
            bad_letters.add(letter.upper())

    print(" ".join(current_display))
    
    if bad_letters:
        print(f"{Fore.RED}Incorrect letters: " + ", ".join(sorted(bad_letters)))
      
    print()

    if word_guess == word:
        guessed = True

if guessed:
    print(f"{Fore.GREEN}Congratulations! You guessed the word: {word.upper()}")
else:
    print(f"{Fore.RED}Out of attempts! The word was: {word.upper()}")
