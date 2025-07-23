import random 
print ("Hi,Welcome the game ROCK🗿 vs PAPER📄 vs SCISSORS ✂, \nRules for this game is :\n1.Rock vs Paper : Paper wins\n2.Rock vs Scissors : Rock wins\n3.Paper vs Scissors : Scissors wins") 
while True:
    print ("Enter your choice :\n1.Rock \n2.Paper \n3.Scissors") 
    choice=int(input ("Enter your choice:")) 
    if choice<1 or choice>3:
        print ("Enter valid choice ")
    if choice==1:
       choice_name='Rock' 
    elif choice==2:
      choice_name='Paper'
    else:
       choice_name='Scissors'
    print("Your choice is:",choice_name)
    comp_choice=random.randint(1, 3) 
    if comp_choice==1:
     comp_name='Rock'
    elif comp_choice==2:
     comp_name='Paper'
    else:
     comp_name='Scissors'   
    print("Computer's choice is :", comp_name) 
    print(choice_name,"vs", comp_name) 
    if choice_name==comp_name:
     result="DRAW"
    elif (choice_name=='Rock' and comp_name=='Paper') or ( comp_name=='Rock' and choice_name=='Paper') :
     result='Paper'
    elif (choice_name=='Paper' and comp_name=='Scissors') or ( comp_name=='Paper' and choice_name=='Scissors') :
     result='Scissors'
    else :  
         result='Rock'
         
         if result=='DRAW':
                print("it's a ties") 
         elif result==choice_name:
                print("You are winner") 
         else :
               print ("Computer is winner ")  
         print(" Do you want to continue? (Y/N) ") 
         ans=input().lower() 
         if ans=='n':
           break
print (" Thanks for playing ")    