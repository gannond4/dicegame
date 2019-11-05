import random
#list to check to see if number has already been guessed
guesses = []

#Max guess
max_guesses = 3
#Number of guesses taken
guesses_taken = 0

#Function to get guess from user
def take_a_guess():
    #Ask for guess convert it to int
    guess = int(input("Take a guess"))
    #return guess
    return guess

#Check if the guess is equal to the number rolled
def check_guess(guess, number):
    return guess == number

#Return a random number 1 to 6 just like a die
def get_a_number():
    return random.randint(1, 6)

def main():
    #global to let the variable be used in a function. if this isnt there it will throw error
    global max_guesses
    global guesses_taken
    global guesses

    print("Rolling die")
    number = get_a_number()
    #Look for guesses check if guesses_taken is not equal to max guess
    while guesses_taken != max_guesses:
        guess = take_a_guess()
        #check if guess is in guesses table
        #if it is tell user it is and just skip rest of loop
        if guess in guesses:
            print("You have already guessed this number")
            continue
        if check_guess(guess, number):
            print("Yah you got the number correct")
            exit(0)
        else:
            print("Sorry that guess if wrong")
            guesses_taken = guesses_taken + 1
            guesses.append(guess)
            print("You have " + str(max_guesses - guesses_taken) + " remaining")

if __name__ == '__main__':
    main()
