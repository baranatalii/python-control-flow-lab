# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()


# Exercise 1: Vowel or Consonant

def check_letter():
    # Your control flow logic goes here
    letter = input("Please enter a letter (a-z or A-Z): ").lower()

    if len(letter) != 1 or not letter.isalpha():
        print("Invalid input. Please enter a single alphabetical letter.")
    elif letter in 'aeiou':
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")

# Call the function
check_letter()


# Exercise 2: Old enough to vote?

def check_voting_eligibility():
    # Your control flow logic goes here
    voting_age = 18
    
    try:
       
        age = int(input("Please enter your age: "))

        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
        elif age >= voting_age:
            print("You are eligible to vote!")
        else:
            print(f"You are not eligible to vote yet. You must be {voting_age} or older.")
            
    except ValueError:
        # This handles cases where the user types "twenty" instead of 20
        print("Invalid input. Please enter a numeric value for your age.")

# Call the function
check_voting_eligibility()

# Exercise 3: Calculate Dog Years

def calculate_dog_years():
    
    try:
        dog_age = int(input("Input a dog's age: "))
        
        if dog_age < 0:
            print("Age cannot be negative.")
        elif dog_age <= 2:
            dog_years = dog_age * 10
        else:
            # First 2 years are 20 (2 * 10), then 7 for every year over 2
            dog_years = 20 + (dog_age - 2) * 7
            
        if dog_age >= 0:
            print(f"The dog's age in dog years is {dog_years}.")
            
    except ValueError:
        print("Invalid input. Please enter a number.")

# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice

def weather_advice():
    # Your control flow logic goes here
    is_cold = input("Is it cold? (yes/no): ").lower()
    is_raining = input("Is it raining? (yes/no): ").lower()

    if is_cold == 'yes' and is_raining == 'yes':
        print("Wear a waterproof coat.")
    elif is_cold == 'yes' and is_raining == 'no':
        print("Wear a warm coat.")
    elif is_cold == 'no' and is_raining == 'yes':
        print("Carry an umbrella.")
    elif is_cold == 'no' and is_raining == 'no':
        print("Wear light clothing.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# Call the function
weather_advice()

# Exercise 5: What's the Season?

def determine_season():
    
    month = input("Enter the month of the year (Jan - Dec): ").capitalize()
    
    try:
        day = int(input("Enter the day of the month: "))
        
        # Check for valid day range
        if day < 1 or day > 31:
            print("Invalid day. Please enter a day between 1 and 31.")
            return

        if (month == 'Dec' and day >= 21) or month in ('Jan', 'Feb') or (month == 'Mar' and day <= 19):
            season = "Winter"
        elif (month == 'Mar' and day >= 20) or month in ('Apr', 'May') or (month == 'Jun' and day <= 20):
            season = "Spring"
        elif (month == 'Jun' and day >= 21) or month in ('Jul', 'Aug') or (month == 'Sep' and day <= 21):
            season = "Summer"
        elif (month == 'Sep' and day >= 22) or month in ('Oct', 'Nov') or (month == 'Dec' and day <= 20):
            season = "Fall"
        else:
            print("Invalid month entry. Please use the three-letter format (e.g., Jan).")
            return

        print(f"{month} {day} is in {season}.")

    except ValueError:
        print("Invalid input. Please enter a numeric value for the day.")

# Call the function
determine_season()