import random

# create function that generates random numbers.
def secret_list(max_range):
    secret_list=[]
    for i in range(4):
        secret_list.append(random.randint(1,max_range))
    return secret_list


#GameInt game will be run below.
def menu():
    student_name= input("\nplease enter your name: ")
    print("\nHi" ,student_name, "Welcome to GameInt" 
          "\nTry to guess the four secret colours \n"
          "You have only 8 attempts\n"
          "There are 6 colours in below list\n"
          "(1)White\n(2)Blue\n(3)Red\n(4)Yellow\n(5)Green\n(6)Purple\n"
          "No need to write the colours, just need to enter the number of that colour\n"
          "Example: for Blue colour you just need to enter '2'\n"
          "If you want to T E R M I N A T E  the game without going into 8th guess just enter '0000'")
menu()

def validation():
    attempts=1
    number=[]
    gameint_list = secret_list(6)
    print(gameint_list)
    
    while attempts<=8:
        
        print("\n")
        string=""
        try:
            for i in range(4):
                x=0
                value = int(input("\nplease enter a number between 1-6: "))
                number.append(value)
                if value>6:
                    print("Value Error")

        except ValueError:
            print("Integer required.Please Enter 4 digits from the beginning")
            continue
        if number==[0,0,0,0]:
            print("You quit the game ")
            break
        else:
      
            for i in number :
                if i in gameint_list:
                    if gameint_list[x]==i:
                        print(1,end=' ')
                        string+="1"
                    else:
                        if  i in gameint_list:
                            print(0,end=' ')
                            string+="0"
                else:
                    print("-",end=' ')
                    string+="-"
                x+=1 

            number.clear()
            if string=="1111" :
                print("\nCongratulations !!!!! You have won the game.You won the game in ",attempts,"attempts")
                break
            else:
                attempts += 1
                
                
    else:
        print("\nYou lost the game the guessed number was",gameint_list)
validation()

while True:
    request=input("\nDo you want to play another game or quiet?(Y/N) ")
    if request.lower()=="y":
        menu()
        validation()
    elif request.lower()=="q":
        break
    else:
        print("Thanks for the game!")
