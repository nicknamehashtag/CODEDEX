import random

print("Welcome to the football game by Alanso's")
user_name = input("Enter your username: ")
print("Welcome dear", user_name)

# Score tracking
user_score = 0
computer_score = 0

print("\nNow let's toss the coin!")
while True:
    
        human_toss = (input("Enter heads or tails: "))
        if human_toss == "heads" or human_toss == "tails":
            print("You have entered a valid input.")
            break
        else:
            print("Invalid input. Please enter heads or tails.")

computer_toss = random.choice(['heads', 'tails'])

if human_toss == computer_toss:
    print("\nYou have won the toss and are ready to start!")
    
    # Simple passing loop
    playing = True
    while playing:
        try:
            passes = int(input("Enter a number between 1 and 3 to do a pass : "))
        except ValueError:
            print("Invalid input.") 
            passes = int(input("Enter a number between 1 and 3 to do a pass : "))

        computer_pass = random.randint(1, 3)
            
        if passes == computer_pass:
            
            print(f"Pass intercepted! Computer chose {computer_pass}.")
            print("You are now defending the ball.")
            defending = True
            while defending:
                    try:
                        defend = int(input("Enter a number between 1 and 3 to defend the ball: "))
                    except ValueError:
                        print("Invalid input")
                        
                    computer_attack = random.randint(1, 3)
                    
                    if defend != computer_attack:
                        computer_score += 1
                        print(f"Computer chose {computer_attack}. The computer has scored a goal! Computer score: {computer_score}")
                    else:
                        print(f"Computer chose {computer_attack}. Great defense! You have regained the ball.")
                        break
        print("the user score is", user_score, "the computer score is", computer_score)
        break       
        
       
        

else:
    print("\nComputer has won the toss and will start attacking!")
    
    defending = True
    while defending:
        try:
            defend = int(input("Enter a number between 1 and 3 to defend the ball: "))
        except ValueError:
            defend = 1
            
        computer_attack = random.randint(1, 3)
        
        if defend != computer_attack:
            computer_score += 1
            print(f"Computer chose {computer_attack}. The computer has scored a goal! Computer score: {computer_score}")
        elif defend == computer_attack:
            print(f"Computer chose {computer_attack}. Great defense! You have regained the ball.")
            print(f"Pass intercepted! Computer chose {computer_pass}.")
            print("You are now attacking the ball.")
            defending = True
            while defending:
                            try:
                                defend = int(input("Enter a number between 1 and 3 to defend the ball: "))
                            except ValueError:
                                print("Invalid input")
                                
                            computer_attack = random.randint(1, 3)
                            
                            if defend != computer_attack:
                                computer_score += 1
                                print(f"Computer chose {computer_attack}. The computer has scored a goal! Computer score: {computer_score}")
                            else:
                                print(f"Computer chose {computer_attack}. Great defense! You have regained the ball.")
                                break
        print("the user score is", user_score, "the computer score is", computer_score)
        break       
                
               
                  
   
       

print("\n--- Game Over ---")
print(f"Final Scores -> {user_name}: {user_score} | Computer: {computer_score}")