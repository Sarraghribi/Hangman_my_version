hangman={0:'''
        ____________
         |''',
        1:'''
        ____________
         |
         O''',
        2:'''
        ____________
         |
         O
        /''',
        3:'''
        ____________
         |
         O
        / \\''',
        4:'''
        ____________
         |
         O
        / \\
         |''',
        5:'''
        ____________
         |
         O
        / \\
         |
        /''',
        6:'''
        ____________
         |
         O
        / \\
         |
        / \\ '''}
import random #here i made 3 lists a list for each level
my_list1=["SARRA","NIDHAL","ADAM","TOURKIA","MARIA"]
my_list2=["CHALLENGE","SCIENCE","STATISTIC","","PLATFORM","PYTHON"]
my_list3=["AWKWARD","BLIZZARD","GOSSIPY","PUZZLING","DUPLEX","AMOUR"]
print("choose the level:easy,medium or difficult") #here is the message that let the user choose a level

#handle level selection
no_repetition=[] #this is a list to put in every used letter
mistake_count=6
mistake_step=1 #the step counter exist to differentiate levels
level=""
levels=["easy","medium","difficult"]
while level not in levels: #the while loop keep running aslong as the input is not easy ,medium or difficult 
  level=input()
  if level=="easy":
    mistake_step=1 #this means the user have 6 tries((mistake count/mistake step)=6/1)
    word=random.choice(my_list1)
  elif level=="medium":
    mistake_step=2 #this means the user have 3 tries(6/2)
    word=random.choice(my_list2)
  elif level=="difficult":
    mistake_step=3#this means the user have 2 tries(6/3)
    word=random.choice(my_list3)
  else:#if the user write smth different than the 3 levels names
    print("please choose a right level name from easy,medium,difficult")
#hidden_word output
hidden_word="-"*len(word)
print(f"hidden word is: {hidden_word}")
print('==============================================')  

#runing the game
while mistake_count>0 and hidden_word.count("-")>0:
  index_count=0
  print("pick a letter") 
  #checking the input letter
  picked_letter=input().capitalize()
  if picked_letter.isalpha()==False or len(picked_letter)>1: #if the user was dumb like Gian said and give in the input smth diffrent than a letter or more than a letter
     print("please choose one alphabetic character")
  elif picked_letter in no_repetition: #if the letter is already used
     print(f"you have alreay chosen {picked_letter}!")
  else: #if it is a new letter we add it to the list no repetition
    no_repetition.append(picked_letter)
    #working with the input letter
    for letter in word: #loop through every letter in the targed word
        if letter==picked_letter : #check in this itiration if the picked letter is the letter that the for loop working with 
         hidden_word=hidden_word[:index_count]+picked_letter+hidden_word[index_count+1:] #update the hidden word using the index of the right picked letter
        index_count+=1 #the index counter works with the for loop
    #playing     
    if word.count(picked_letter)>0: #this means that the inputed letter exist one or more than one time in the word
      print(f"CORRECT!the word contains the {picked_letter}")
      print(f"hidden word is: {hidden_word}") #to show the updated hidden word for the user
    else:#if the inpued letter does not exist in the word
      mistake_count -=mistake_step #the mistake counter depend to the step counter for every level
      print(f"WRONG! number of mistakes left : {int(mistake_count/mistake_step)}") #to give the correct number of mistakes lefted for the user
      print(hangman[6-mistake_count])
      print('==============================================')
# check final result
if mistake_count==0:
  print("HANGED!")
else:
  print("CONGRATULATIONS")
