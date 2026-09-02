backpack=[]
menu=["1. Add item to backpack","2. Remove item from backpack","3. View backpack","4. Exit"]
while True:
    print("======Backpack Menu:=======")

    for option in menu:
        

        print(f'{option}')
    try:
        user_choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue
    if user_choice < 1 or user_choice > 4:
        print("Invalid choice. Please enter a number between 1 and 4.")
        continue
    if user_choice == 1:
        item = input("Enter the item to add to the backpack: ")
        if item in backpack:
            print("YOU ALREADY OWN THIS")
        elif len(backpack )>= 5:
            print("YOUR BACKPACK IS FULL")
        else:
            backpack.append(item)
            print(f"{item} has been added to the backpack.")
    elif user_choice == 2:
        
            item = input("Enter the item to be removed from the backpack: ")
            if item in backpack:
                backpack.remove(item)
                print(f"{item} has been removed from the backpack.")
            else:
                print(f"{item} is not in the backpack.")
                
        
        
    elif user_choice == 3:
        if len(backpack) == 0:
            print("YOUR BACKPACK IS EMPTY")
        
        for item in backpack :
            print(f'your items are{item}')
    else:
        print("thank you")
        break
