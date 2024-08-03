import random
while True:
    print("""   press 1 for rock 
        press 2 for paper
        press 3 for scissor  """)

    computer = random.choice([1,2,3])



    user= int(input("enter your choice "))
    if user not in [1,2,3]: 
        print("wrong input") 
    
    print(f"user has chosen {user}")
    print(f"computer has chosen {computer}")


    if(computer == 1 and user ==2):
        print("user wins")
    elif(computer == 2 and user ==3):
        print("user wins")
    elif(computer == 3 and user ==1):
        print("user wins")
    elif(computer == 2 and user ==1):
        print("computer wins")
    elif(computer == 3 and user ==2):
        print("computer wins")
    elif(computer == 1 and user ==3):
        print("computer wins")
    if(computer==user):
        print("draw") 


    play_again = input("Do you want to play again? Y for yes and N for no: ").strip().lower()
    if play_again not in ['y', 'n']:
        print("Enter correct input")
        continue
    elif play_again == 'n':
        break

        