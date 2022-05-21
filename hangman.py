import random

"""
\033[  Escape code for fonts- always the same
1 = style/font - things like normal, bold, italic, underline
32 = Text color-different colors are assigned different numbers, 32 is an example and is bright green
40m = Background colour, 40 is black
"""

#unpacking font colors for the funsies
red, green, blue, white = '\033[2;31m', '\033[2;32m', '\033[2;34m', '\033[2;37m'

#make font color white so it looks snazzy
print(white)

#function to check the letter
def check_letter(letter, word_as_list):
    #list of indexes the letter is at in the word
    indexes = []

    #if the letter equals a letter at a certain index of the word, it adds it to the list
    for index in range(len(word_as_list)): 
        if word_as_list[index] == letter:
            indexes.append(index)
    return(indexes)

#function to print categories and choose one
def choose_category(category_list):
    #while loop so that if the person chooses an invalid category they start over
    while True:

        # prints each category in a numbered list
        for index in range(len(category_list)):
                print(f"{index+1}. {category_list[index]}")
        chosen = input("Enter the number or name of a category: ")

        #try except to see if its a number (index of the category) or the name of the category
        try:
            chosen == int(chosen)
        except ValueError:
            str_chosen = chosen
            if str_chosen in category_list:
                return str_chosen

            #if its anything else then its invalid
            else:
                print("That isn't one of the categories!")
                continue
        else:
            chosen_index = int(chosen)
        
        #check the index and turn it into a category name to return
        if chosen_index > len(category_list) or chosen_index <= 0:
            print("That is not a valid index! try again :(")
            continue
        else:
            int_chosen = category_list[chosen_index -1]
            return int_chosen
            
#function to put a letter into the unfinished word (i.e. put the letter 'a' in the word when the word is in the form _ _ _ _ _)
def put_letter_in_lines(current_lines, letter, indexes_of_letter_list):
    #make a list of the - and letters
    lines_as_list = list(current_lines)

    #for index in length of - and letters
    for index in range(len(lines_as_list)): 

        # if index matches one in the index list
        if index in indexes_of_letter_list: 

            #index in - and letter list is the letters
            lines_as_list[index] = str(letter)
    lines = "".join(lines_as_list)
    return lines

#guess letter function
def guess_letter(used):
    while True:
        guessed_letter = input("guess a letter(enter the phrase 'guess the word' to guess the word): ")

        #give the option to guess the whole word/phrase
        if guessed_letter == "guess the word":
            return "word guess"
        
        #if the letter is already used, guess something else
        elif guessed_letter in used:
            print("You already used that! Guess something else!")
            continue

        #if the guess is a symbol/character that is not a letter, it will be an error later, so return it here because some words/phrases do have symbols
        elif guessed_letter in "`~!@#$%^&*()_-+=|\}]{[\"':;?/>.<,":
            return guessed_letter
        
        #check for the chinese characters included since its a category
        elif guessed_letter in "你好再见小苹果于老师小吃玛":
            return guessed_letter
        
        #if its a number or somethin else
        elif type(guessed_letter) != str:
            print("That isn't a letter!")
            continue

        # cant be more than one letter 
        elif len(guessed_letter) > 1:
            print("Too many letters!")
            continue

        #lowercase only
        elif guessed_letter.upper() == guessed_letter:
            print("Please enter lowercase letters only!")
            continue
        else:
            return guessed_letter

#if the user chooses to guess a word
def guess_word(chosen_word):
    word = input("Enter the word: ")

    #add it to the used words list in case its wrong
    used_words.append(word)

    #check if its the same and return correct or no
    if word.lower() == chosen_word.lower():
        return "correct"
    else:
        return "nope"

#get the image of the hangman- checks the number of errors and returns the appropriate image
def hang_imagename(errors):
    if errors == 0:
       
        return ["   +---+"
                "\n   |   |"
                "\n       |"
                "\n       |"
                "\n       |"
                "\n       |"
                "\n       |"
                "\n ========="]
    if errors == 1:
        return  ["   +---+"
                "\n   |   |"
                "\n       |"
                "\n   ()  |"
                "\n       |"
                "\n       |"
                "\n       |"
                "\n ========="]
    if errors == 2:
        return ["   +---+"
                "\n   |   |"
                "\n       |"
                "\n   ()  |"
                "\n   |   |"
                "\n       |"
                "\n       |"
                "\n ========="]
    if errors == 3:

        return ["   +---+"
                "\n   |   |"
                "\n       |"
                "\n   ()  |"
                "\n  /|   |"
                "\n       |"
                "\n       |"
                "\n ========="]
    if errors == 4:

        return ["   +---+"
                "\n   |   |"
                "\n       |"
                "\n   ()  |"
                "\n  /|\  |"
                "\n       |"
                "\n       |"
                "\n ========="]
    if errors == 5:

        return ["   +---+"
                "\n   |   |"
                "\n       |"
                "\n   ()  |"
                "\n  /|\  |"
                "\n  /    |"
                "\n       |"
                "\n ========="]
    if errors == 6:

        return ["   +---+"
                "\n   |   |"
                "\n       |"
                "\n   ()  |"
                "\n  /|\  |"
                "\n  / \  |"
                "\n       |"
                "\n ========="]
    if errors == 7:

        return ["   +---+"
                "\n   |   |"
                "\n       |"
                "\n   (U) |"
                "\n  /|\  |"
                "\n  / \  |"
                "\n       |"
                "\n ========="]
    if errors == 8: 

        return ["    +---+"
                "\n   |   |"
                "\n       |"
                "\n   (Ú) |"
                "\n  /|\  |"
                "\n  / \  |"
                "\n       |"
                "\n ========="]
    if errors == 9:

        return ["    +---+"
                "\n   |   |"
                "\n       |"
                "\n   (Ü) |"
                "\n  /|\  |"
                "\n  / \  |"
                "\n       |"
                "\n ========="]
    if errors == 10:

        return ["   +---+"
                "\n   |   |"
                "\n  [hat]|"
                "\n   (Ü) |"
                "\n  /|\  |"
                "\n  / \  |"
                "\n       |"
                "\n ========="]
    

#define categories and words in each category in a dictionary
categories = ["animals", "items on the periodic table!", "fall out boy songs w/wonderful names", "food (and drink)", "famous people woo", "random!", "pickup lines :D"]
categories_and_words = {
    "animals":["dog","elephant","llama","platypus","racoon", "cat", "dinosaur", "cow", "sheep"],
    "items on the periodic table!":["iron", "arsenic","mercury","helium","copper","sodium","aluminum","zinc","magnesium","chlorine","fluorine","Phosphorous"],
    "fall out boy songs w/wonderful names":["Thnks Fr th mmrs", "I slept with someone in fall out boy and all i got was this stupid song written about me", "GINASFS", "of all the gin joints in all the world", "sophmore slump or comeback of the year", "Snitches and talkers get stitches and walkers", "Dance dance", "Sugar we're going down swinging", "our lawyer made us change the name of this song so we wouldnt get sued", "im like a lawyer with the way im always trying to get you off (you and me)", "get busy living or get busy dying (do your part to save the scene and stop going to the shows)", "ive got a dark alley and a bad idea that says you should shut your mouth (summer song)", "i got all this ringing in my ears and none on my fingers"],
    "food (and drink)": ["strawberry", "turkey sandwich", "water", "applesauce", "oreo cookie", "charred nuts", "pickle"],
    "famous people woo":["JOHN CENA", "Taylor Swift", "Tom Hanks", "Chris Pratt", "Will Smith", "Julia Roberts", "Barack Obama", "Rick Astley"],
    #"chinese(you need to actually use chinese characters)":["你好","再见","小苹果","于老师","小吃", "玛老师"],
    "random!":["#slay", "pickup lines", "textbook", "tables and chairs", "i detest american television", "bongo the muffin", "duct tape", "wiggle", "BEANS", "gamer moment", "computation is sweeping the nation", "*bites lip*","[insert png here]", "naked crayons", "rubix cube"],
    "pickup lines :D":["you better call life support baby cause ive fallen for you and i cant get up", "are you helium cause you look high", "are you an endothermic reaction", "are you an overheating nuclear power plant cause youre looking pretty thermal", "you must be match fumes cause you take my breath away", "are you missing an electron because youre looking positively attractive", "theres a lot of elements on the periodic table but all i see is U and I", "hey baby id sacrifice my life for you like a charred nut on a paper clip","are you depleted plutonium because youre radioactive","hey you know my favorite element is uranium because its U", "are you uranium because i cant find you on ebay", "you must be the square root of negative one cause you cant be real", "cant help but notice youre the perfect person to have some dino nuggies with", "i might give up chicken for tofu but id never give you up", "roses are red, the copper two+ ion is blue, id love to have some dino nuggies with you", "to bean or not to bean"]
}    


#first game loop- start of the game, repeats once per game but repeats multiple times for multiple games
gamer = True
while gamer == True:
    print("Welcome to hangman! \nObjective: guess the word \nHow to play: Pick a category when prompted. You will be shown the word and the number of letters, and then you just guess letters until you lose or get the word. You can also choose to guess the whole word\nRules/Tips: \n1. Characters(!@#$%^&*()~`_-+={[}]|\:;\"'<,>.?/}) are allowed, but numbers are not \n2. Guess vowels first cause theres a lot of words with those\n3. I don't know if this is a rule but if the man gets hanged you lose \nHave fun and try not to let the man die\n")
    #have the user choose a category using the function defined above
    chosen_category = choose_category(categories)
    
    #pick a word from chosen category using function
    chosen_word = random.choice(categories_and_words[chosen_category]).lower()
    #make it a list 
    chosen_word_list = list(chosen_word)
    chosen_word_letter_lines = ""
    #create what will be printed for the user- it will look like this: _ _ _ _ _ _ _ _ 
    for letter in chosen_word_list:
        if letter == " ":
            chosen_word_letter_lines = chosen_word_letter_lines + " "
        else:
            chosen_word_letter_lines = chosen_word_letter_lines + "-"
    

    #define used letters list and used words
    used_letters = []
    used_words = []

    #define # of errors
    errors = 0

#user ready to start
    while True:
        ready = input("Are you ready to play? (y/n) ")
        if ready == "n":
            continue
        if ready == "y":
            break
        else:
            print("invalid answer")
            continue

    #game loop- main part that repeats asking for a letter/word
    while True:
        #start by checking for game over from last round of asking letters
        if errors > 10:
            print("Game over! The person has been hanged.")
            break   
        #print category, lines, errors, and used letters/words
        print()
        print(f"Your category is: {chosen_category}.")
        print(f"used letters: {used_letters}")
        print(f"used words: {used_words}")
        print(f"errors: {errors}/10")

        #change the font to green for the lines and hang image!
        print(green)
        print(chosen_word_letter_lines)
        
        #gets the list of lines from the function and prints each line
        image_list = hang_imagename(errors)
        for line in image_list:
            print(line)
        #change font back to white
        print(white)

        #guess and check letter with function
        guessed_letter = guess_letter(used_letters)

        #if the result is the word guess, then run the guess_word function instead
        if guessed_letter == "word guess":
            guessed_word_result = guess_word(chosen_word)
            #if the guess_word function returns correct then its correct, it will break out of the game function and go to line 339
            if guessed_word_result == "correct":
                print(f"Congratulations! You got the word: {chosen_word}!")
                break
            else:
                #otherwise its like no youre wrong and adds 1 to errors
                print("Sorry, incorrect.")
                errors +=1
                continue
        
        #otherwise add to the used letters list
        used_letters.append(guessed_letter)
        #check the letter to see if its valid and then return the indexes
        guessed_letter_indexes = check_letter(guessed_letter, chosen_word_list)

        #if it wasnt anywhere then oops wrong letter
        if guessed_letter_indexes == []:
                print("Sorry, that letter is not in the word.")
                errors +=1      

        #else it is somewhere then change that value in the lines using function
        else:
            chosen_word_letter_lines = put_letter_in_lines(chosen_word_letter_lines, guessed_letter, guessed_letter_indexes)

        #check if word is finished by joining the letters/lines
        letters_at_moment = "".join(chosen_word_letter_lines)
        if chosen_word == letters_at_moment:
            print(f"Congratulations! You got the word: \n'{chosen_word}' !")
            break
        else:
            #else start back by guessing letters
            continue

        
    #back to the first while loop- this comes up if you break out of the inner game loop by winning or losing
    # check if you would like to play again and either break out of this loop and make gamer false so the game stops or just break this loop and start back at the beginning of main loop
    while True:
        cont = input("Would you like to play again? (y/n) ") 
        if cont == "n":
            gamer = False
            break
        elif cont == "y":
            break
        else:
            print(red)
            print("bro enter a valid yes or no")
            print(white)
            continue

            
                
                
                
            

        

