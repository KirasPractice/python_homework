

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
           guesses.append(letter)

           check = ''
           for character in secret_word:
                 if character in guesses:
                       check += character
                 else:
                       check += "_"
           print(check)

           all_guessed = True
           for character in secret_word:
            if character not in guesses:
                 all_guessed = False
           return all_guessed  

    return hangman_closure("a")
make_hangman("hello")
                
secret = input("Enter the secret word: ")
hangman = make_hangman(secret)

guessed = False 

while not guessed:
    letter = input("Guess a letter: ")
    guessed = hangman(letter)   

print("You guessed the whole word!")

        
        
    
    
   

     
  
         
                
                
            

