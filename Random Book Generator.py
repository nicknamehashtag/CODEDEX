
import random
("The Random Book Generator")
# the total list of books
books="Crime and Punishment","Love at the time of Cholera",'The Story Of My Experiments With Truth'
random_book=random.choice(books)
print(f'The book you have been chosed is:{random_book}')
try :
    opinion=input("Do You Want to Roll again??")
except NameError :
    print("enter a vaild answer")
finally :
    if opinion=="NO":
        print("THANK YOU YOU CAN READ THE PROVIDED BOOK")
    elif opinion=="YES":
        
        random_book=random.choice(books)
        print(f'The book you have been chosed is:{random_book}') 
    else :
        print("PLEASE ENTER A VALID ANSWER \"YES\" OR \"NO\"")

