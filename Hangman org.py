print("Welcome to Hangman Game \n")

input("Enter to see instructions.")

print("How to play? :- Firstly select your category in which you want to play \n" \
      "Their are some hints provided to you  and you have to guess the word. \n "\
      "You are provided with 6 lives in the game and each time you enter a wrong letter "\
      "1 life will be lost.\n"\
      "If the name to be guessed contains 2 or more than 2 words then ***DONOT*** give spaces in between the words.")


print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ ''')



import random

stages = [
    '''   _______
     |/      |
     |
     |
     |
     |
     |
    _|___ ''' ,

    '''   _______
     |/      |
     |      (_)
     |
     |
     |
     |
    _|___ ''',

    '''   _______
     |/      |
     |      (_)
     |       |
     |
     |
     |
    _|___ ''',

    '''   _______
     |/      |
     |      (_)
     |      \|
     |
     |
     |
    _|___ ''',

    '''   _______
     |/      |
     |      (_)
     |      \|/
     |
     |
     |
    _|___ ''',

    '''   _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |
     |
    _|___ ''',

    '''   _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___ ''',
    
    
    
    
]

category = input("Select your category. a if you are a kid , b if you are a teenager , c if you are an adult.").strip().lower()


#  FOR CATEGORY - KID 


if category == "a":

    word_list = ["apple" , "mango" , "banana" , "pear" , "peach" , "pineapple"] 

    lives = 6 

    choosen_word = random.choice(word_list)

    input("Enter to unlock hints")

    if choosen_word == "apple" :
        print(" Hints :-\n 1)I am a good source of vitamins and minerals\n" \
        "2) I am generally in red and green colour\n" \
        "3) I am an all season fruit. \n" 
        "GUESS WHO I AM ?"   )

    elif choosen_word == "mango" :
        print(" Hints :-\n 1)I have a sweet taste.\n" \
        "2) I am generally in yellow and green colour\n" \
        "3) I am a seasonal fruit. \n" 
        "GUESS WHO I AM ?"   )

    elif choosen_word == "banana" :
        print(" Hints :-\n 1)I am the fruit which helps people in low bp .\n" \
        "2) I am generally in yellow and green colour\n" \
        "3) I am not a seasonal fruit. \n" 
        "GUESS WHO I AM ?"   ) 

    elif choosen_word == "pear" :
        print(" Hints :-\n 1)I am a good source of vitamin C.\n" \
        "2) I am narrow at the stem and wider at the bottom.\n" \
        "3) I am a sweet and juicy fruit\n" 
        "GUESS WHO I AM ?"   )       

    elif choosen_word == "peach" :
        print(" Hints :-\n 1)I am a good source of vitamin A, C and fibers.\n" \
        "2) I am light pinkish orange in colour.\n" \
        "3) I am a seasonal fruit.\n" 
        "GUESS WHO I AM ?"   ) 

    elif choosen_word == "pineapple" :
        print(" Hints :-\n 1)I have leaves outside my cover.\n" \
        "2) I am generally elliptical in shape.\n"  \
        "3) I am a sweet and juicy fruit\n" 
        "GUESS WHO I AM ?"   )     

    placeholder = ""
    for position in range (0, len(choosen_word)):
        placeholder += "_"

    print(f"Remember that the no. of blanks = no. of letters in the word to be guessed : {placeholder}")

    game_over = False
    correct_letters = []

    while not game_over:
        guess = input("Guess the alphabet : ").strip().lower()

        if guess in correct_letters :
            print(f"You have already guessed {guess} ! Try another letter. ")

        display = ""
        count = 0
        for letter in choosen_word:
            if letter == guess:
                count+=1
                display += letter
                correct_letters.append(guess)

            elif letter in correct_letters:
                display += letter
                
            else :
                display += "_"  
        print(display)
        if count > 0:
            print(f"Correct letter guessed {lives}/6 remaining.") 

        count = 0                
        
        if guess not in choosen_word:
            lives -= 1 
            print(f"You guessed {guess}, That's not in the word.\nYour lost a life !\n{lives}/6 lives remaining.")
            print(stages[6-lives])
            if lives == 0 :
                game_over = True
                print("You lose.")
                
                print(f"The Correct word was : {choosen_word}")
        
        if "_" not in display :
            game_over = True
            print("You won!")
        
    input("Enter to exit .")     



# FOR CATEGORY - TEENAGER 



elif category == "b":
   
 
    word_list = ["asia" , "indiragandhi" , "sardarvallabhbhaipatel" , "diamond" , "jupiter" , "tungsten"] 

    lives = 6 

    choosen_word = random.choice(word_list)

    input("Enter to unlock hints")

    if choosen_word == "asia" :
        print(" Hints :-\n 1) It has 48 countries.\n " \
              " 2) The Himalayas are located here.\n " \
              " 3) The world’s largest population lives here. \n"\
              " 4) India is also part of this continent. \n" \
              "GUESS WHO I AM ?"   )

    elif choosen_word == "indiragandhi" :
        print(" Hints :-\n 1) Daughter of Jawaharlal Nehru.\n " \
              " 2) Became PM in 1966. \n " \
              " 3) Her surname sounds like a currency. \n" \
              " 4) Assassinated in 1984. \n" \
              "GUESS WHO I AM ?" )


    elif choosen_word == "sardarvallabhbhaipatel" :
        print(" Hints :-\n 1) His statue is the tallest in the world.\n" \
                           "2) Known as iron Man Of India \n" \
                           "3) From Gujarat.\n"\
                           "4) First Deputy PM of India.\n" \
              "GUESS WHO I AM ?"  ) 

    elif choosen_word == "diamond" :
        print(" Hints :-\n 1)Hardest Natural substance .\n " \
        "2) Made of pure carbon\n " \
        "3) Used in jewellery\n" \
        "4) Either found underground or formed under high pressure."
        "GUESS WHO I AM ?"   )       

    elif choosen_word == "jupiter" :
        print(" Hints :-\n 1) Planet with most moons\n " \
          "2) It is a gas giant.\n " \
          "3) Has a Great Red Spot.\n" \
          "4) Largest planet in the solar system\n" \
          "GUESS WHO I AM ?" )
 

    elif choosen_word == "tungsten" :
        print(" Hints :-\n 1) Hardest known metal.\n " \
        "2) Used in cutting tools\n "  \
        "3) Symbol W \n" \
        "4) Very high melting point. \n " \
        "GUESS WHO I AM ?"   )     

    placeholder = ""
    for position in range (0, len(choosen_word)):
        placeholder += "_"

    print(f"Remember that the no. of blanks = no. of letters in the word to be guessed : {placeholder}")

    game_over = False
    correct_letters = []

    while not game_over:
        guess = input("Guess the alphabet : ").strip().lower()

        if guess in correct_letters :
            print(f"You have already guessed {guess} ! Try another letter. ")

        display = ""
        
        count2 = 0
        for letter in choosen_word:
            if letter == guess:
                count2 += 1
                display += letter
                correct_letters.append(guess)
                
            elif letter in correct_letters:
                display += letter 
                
            else :
                display += "_"   
        print(display) 
        if count2 > 0:
            print(f"Correct letter guessed {lives}/6 remaining")

        count2 = 0       
        
        if guess not in choosen_word:
            lives -= 1 
            print(f"You guessed {guess}, That's not in the word.\nYour lost a life !\n{lives}/6 lives remaining.")
            print(stages[6-lives])
            if lives == 0 :
                game_over = True
                print("You lose.")
                
                print(f"The Correct word was : {choosen_word}")
        
        if "_" not in display :
            game_over = True
            print("You won!")

    input("Enter to exit .")

#  FOR CATEGORY - ADULT 



elif category == "c":


   
   
    word_list = ["markzuckerberg" , "saudiarabia" , "bengaluru" , "haryana" , "objectorientedprogramming" , "Recursion"] 

    lives = 6 

    choosen_word = random.choice(word_list)

    input("Enter to unlock hints")

    if choosen_word == "markzuckerberg" :
        print(" Hints :-\n 1) Started a company in a Harvard dorm room\n " \
              " 2) Youngest self-made billionaire.\n " \
              " 3) Bought Instagram & WhatsApp. \n"\
              " 4) Parent company starts with Meta Platform. \n" \
              "GUESS WHO I AM ?"   )

    elif choosen_word == "saudiarabia" :
        print(" Hints :-\n 1) World’s largest oil producer.\n " \
              " 2) Capital is Riyadh. \n " \
              " 3) Two holiest Islamic cities. \n" \
              " 4) Vision 2030. \n" \
              "GUESS WHO I AM ?" )


    elif choosen_word == "bengaluru" :
        print(" Hints :-\n 1) Known as India’s Silicon Valley.\n" \
                           "2) Hub for startups and IT companies \n" \
                           "3) Famous for Traffic & Tech Parks.\n"\
                           "4) Famous for Traffic & Tech Parks.\n" \
              "GUESS WHO I AM ?"  ) 

    elif choosen_word == "haryana" :
        print(" Hints :-\n 1)India’s 2nd largest milk-producing state.\n " \
        "2) Home to India’s biggest automobile hub \n " \
        "3) Highest per-capita income among major Indian states\n" \
        "4) Hosts the headquarters of ISRO’s Human Space Flight Centre"
        "GUESS WHO I AM ?"   )       

    elif choosen_word == "objectorientedprogramming" :
        print(" Hints :-\n 1) Based on objects and classes\n " \
          "2) Supports inheritance and polymorphism.\n " \
          "3) Languages include Java, Python, C++.\n" \
          "4) Models real-world entities\n" \
          "GUESS Which programming paradigm ?" )
 

    elif choosen_word == "Recursion" :
        print(" Hints :-\n 1) It allows one function to call itself.\n " \
        "2) Used in tree traversal, factorial, Fibonacci.\n "  \
        "3) Requires a base condition W \n" \
        "4) oo much of it causes a stack overflow. \n " \
        "What concept am I"   )     

    placeholder = ""
    for position in range (0, len(choosen_word)):
        placeholder += "_"

    print(f"Remember that the no. of blanks = no. of letters in the word to be guessed : {placeholder}")

    game_over = False
    correct_letters = []

    while not game_over:
        guess = input("Guess the alphabet : ").strip().lower()

        if guess in correct_letters :
            print(f"You have already guessed {guess} ! Try another letter. ")

        display = ""
        
        count3 = 0
        
        for letter in choosen_word:
            if letter == guess:
                count3 +=1
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter 
                
            else :
                display += "_"   
        print(display) 
        
        if count3 > 0:
            print(f"Correct letter guessed {lives}/6 remaining")

        count3 = 0       
        
        if guess not in choosen_word:
            lives -= 1 
            print(f"You guessed {guess}, That's not in the word.\nYour lost a life !\n{lives}/6 lives remaining.")
            print(stages[6-lives])
            if lives == 0 :
                game_over = True
                print("You lose.")
                
                print(f"The Correct word was : {choosen_word}")
        
        if "_" not in display :
            game_over = True
            print("You won!")

        
            
    input("Enter to exit .")