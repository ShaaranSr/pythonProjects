import random
import time
while True:
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)

    player = None
    while player not in choices:
      player = input("Rock, paper or scissors: ").lower()

      if player == computer:
         time.sleep(0.5)
         print("computer: " + computer)
         print("player: " + player)
         time.sleep(1.5)
         print("Its tie!")
      elif player == "rock":
          if computer == "paper":
            time.sleep(0.5)
            print("computer: " + computer)
            print("player: " + player)
            time.sleep(1.5)
            print("You lose!")
          if computer == "scissors":
            time.sleep(0.5)
            print("computer: " + computer)
            print("player: " + player)
            time.sleep(1.5)
            print("You win!")
      elif player == "paper":
          if computer == "scissors":
            time.sleep(0.5)
            print("computer: " + computer)
            print("player: " + player)
            time.sleep(1.5)
            print("You lose!")
          if computer == "rock":
            time.sleep(0.5)
            print("computer: " + computer)
            print("player: " + player)
            time.sleep(1.5)
            print("You win!")
      elif player == "scissors":
          if computer == "rock":
            time.sleep(0.5)
            print("computer: " + computer)
            print("player: " + player)
            time.sleep(1.5)
            print("You lose!")
          if computer == "paper":
            time.sleep(0.5)
            print("computer: " + computer)
            print("player: " + player)
            time.sleep(1.5)
            print("You win!")
    time.sleep(2)
    play_again = input("play again (yes/no): ")
    if play_again != "yes":
        break
time.sleep(1)
print("Thanks for playing with me :)")


