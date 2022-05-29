''' In this file we are going to run our main program we will ask for the name of two users in this script
and
-- we will need random choice from the computer we will import it from RandomChoice module

#writing an algorithm for scissor paper rock
1. Ask for the name of user
2. Display the welcome page
3. Creating variables named userCount and computerCount to count the number of games win by them respectively
4. We will play 3 rounds
5. Opening loop for 3 times
6. Create a varaible named choiceOfUser and ask user its answer(rock or paper or scissor)
7. create another varaible named choiceOfComputer and import from RandomChoice module
8. If choiceOfUser is equalsnto the choiceOfCOmputer then it's draw
9. Elif choiceOfUser is rock and choiceOfOmputer is scissor then increment the userCount since he win first round and continue to the second round and viceversa
10. Elif choiceOfUser is paper and choiceOfCOmputer is scissor then increment the computerCount and viceversa
11. Compare userCount and computerCount
12 If userCOunt > then userwins
13. else computerwins

'''
from os import system

#defining the welcomePage function
def welcomePage(userName) :

    system("CLS")
    print("\n"*3 + "\t"*5 + "-"*5 + " WELCOME TO ROCK PAPER AND SCISSOR " + "-"*5)

    


if __name__ == "__main__" :

    system("CLS")

    #asking for the name of the user 
    nameOfUser = input("\n"*3 + "\t"*6 + "Enter your name : ")

    #invoking the welcome page function
    welcomePage(nameOfUser)
