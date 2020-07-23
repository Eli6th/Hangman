import random
import os

head = ""
arms = ""
body = ""
legs = ""

let = 0

def createWord():
  f = open("D:\\Code\\PythonProjects\\Hangman\\words.txt", "r")
  num = 0
  word = ""
  wordRange = 0

  for i in f:
    wordRange += 1

  f.close()

  wordNum = random.randint(1, wordRange)

  f = open("D:\\Code\\PythonProjects\\Hangman\\words.txt", "r")
  for x in f:
    num+=1
    if num == wordNum:
      word = x
  f.close()

  return word

def check (guesses):
  global head
  global arms
  global body
  global legs

  if guesses == 0:
    head = "   "
    arms = "   "
    body = "   "
    legs = "   "
  elif guesses == 1:
    head = " O "
    arms = "   "
    body = "   "
    legs = "   "
  elif guesses == 2:
    head = " O "
    arms = " | "
    body = "   "
    legs = "   "
  elif guesses == 3:
    head = " O "
    arms = "\| "
    body = "   "
    legs = "   "
  elif guesses == 4:
    head = " O "
    arms = "\|/"
    body = "   "
    legs = "   "
  elif guesses == 5:
    head = " O "
    arms = "\|/"
    body = " | "
    legs = "   "
  elif guesses == 6:
    head = " O "
    arms = "\|/"
    body = " | "
    legs = " / "
  elif guesses == 7:
    head = " O "
    arms = "\|/"
    body = " | "
    legs = "/'\ "

def guess(word, let, guessLet, guesses):
  guess = input("What letter would you like to guess?")
  correct = False
  letterNum = 0

  for i in word:
    letterNum += 1
    if guess == i:
      correct = True
      let[letterNum-1] = 1
  
  if correct == False:
    guessLet[guesses] = guess
  
  return correct

def show(word, let):
  correct = 0
  win = False
  for i in range (0, len(let)):
    if let[i] == 1:
      correct += 1
      print (word[i], end = " ")
    elif let[i] == 0:
      print ("_", end = " ")
  
  if correct == len(let):
    win = True
  
  return win

def main():
  guessLet = ["" for i in range(0, 7)]
  guesses = 0
  win = False

  word = createWord()
  global let 
  let = [0 for i in range(0, len(word)-1)]

  while guesses < 7 and win == False:
    check(guesses)
    for a in guessLet:
      print(a, end = " ")

    print()
    print(" ____")
    print(" |  |")
    print(" |", head)
    print(" |", arms)
    print(" |", body)
    print(" |", legs)
    print("_|_")

    print()
    win = show(word, let)
    if win == True:
      print()
      print("You guessed the correct word!")
      play()
      print()
      return
    print()
    print()

    correct = guess(word, let, guessLet, guesses)
    if correct == False:
      guesses += 1

  if win == True:
    print()
    print("You guessed the correct word!")
    print()
    return
  else:
    print()
    check(guesses)

    print(" ____")
    print(" |  |")
    print(" |", head)
    print(" |", arms)
    print(" |", body)
    print(" |", legs)
    print("_|_")
    print()
    print("The word was", word)
    print("You lost :(")
    play()
    print()
    return

def play():
  wPlay = input("Would you like to play a game of hangman? (Y/N)")
  if wPlay == 'Y' or wPlay == 'y':
    main()
  elif wPlay == 'N' or wPlay == 'n':
    print("Have a good day!")
  else:
    print("Invalid input. Try again.")
    play()

play()