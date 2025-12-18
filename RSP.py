import random

print("=============================")
print(" Rock, Paper, Scissors Game ")
print("=============================")

user_scores = 0
computer_scores = 0
rounds = 5
current_round = 1

while current_round <= rounds:

    print(f"\nRound {current_round} of {rounds}")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    opt = input("Enter your choice: ")
    if opt == '4':
        print("Thanks for playing!")
        break

    if opt not in ['1', '2', '3']:
        print("Invalid choice! Please select again.")
        continue

    user_choice = {'1': 'Rock', '2': 'Paper', '3': 'Scissors'}[opt]
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])

    print("\nYou chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    
    elif (
        (user_choice == 'Rock' and computer_choice == 'Scissors') or 
        (user_choice == 'Paper' and computer_choice == 'Rock') or
        (user_choice == 'Scissors' and computer_choice == 'Paper')
    ):
        print("You Win!")
        user_scores += 1

    else:
        print("Computer Wins!")
        computer_scores += 1

    print("Score -> You:", user_scores, " Computer:", computer_scores)

    current_round += 1

print("=============================")
print("Game Over!")
print("=============================")
print("Final Score:")
print("You:", user_scores)
print("Computer:", computer_scores)

if user_scores > computer_scores:
    print("Congratulations!! You won the game!!")
elif computer_scores > user_scores:
    print("Computer won the game!!")
else:
    print("The game is a tie!")
