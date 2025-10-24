# 🎮 Python Console Wordle

A simple Wordle-inspired console game written in Python. Guess the 5-letter word in 6 tries or less! Colors indicate how close your guess is:

* 🟩 Green – Correct letter in the correct position
* 🟨 Yellow – Correct letter in the wrong position
* ⬜ White – Letter not in the word

---

## Features

* Real English 5-letter words
* 6 attempts per game
* Visual feedback using colors in the console
* Tracks incorrect letters
* Easy to play and extend

---

## How to Play

**Step 1: Clone the repository**

```
git clone https://github.com/alas-m/WordleCMD.git
cd WordleCMD
```

**Step 2: Install dependencies**

```
pip install colorama
```

**Step 3: Run the game**

```
python wordle.py
```

**Step 4: Enter your guesses and try to find the hidden 5-letter word!**

---

## Example Output

```
A 5-letter word has been generated!
■ ■ ■ ■ ■

Attempt 1/6 - Enter your guess: apple
A ■ ■ P L E     Incorrect letters: A, P, L, E
```

*(Colors appear in the console: green/yellow/white squares)*

---

## How it Works

* Random word selection from a text file (`words.txt`)
* Letter-by-letter comparison for coloring
* Tracks and displays incorrect letters
* Game ends when word is guessed or attempts run out

---

## Future Improvements

* Persistent high scores
* Timer or scoring system
* Multiplayer mode
* GUI version

---

## License

MIT License
