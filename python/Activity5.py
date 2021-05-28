# Run the algorithm to see who wins
if user1_answer == user2_answer:
    print("It's a tie!")
elif user1_answer == 'rock':
    if user2_answer == 'scissors':
        print("Rock wins! and Congratulations ", user1)
    else:
        print("Paper wins! and Congratulations ", user2)
elif user1_answer == 'scissors':
    if user2_answer == 'paper':
        print("Scissors win! and Congratulations ", user1)
    else:
        print("Rock wins! and Congratulations ", user2)
elif user1_answer == 'paper':
    if user2_answer == 'rock':
        print("Paper wins! and Congratulations ", user1)
    else:
        print("Scissors win! and Congratulations ", user2)
else:
    print("Invalid input! You have not entered rock, paper or scissors, try a
