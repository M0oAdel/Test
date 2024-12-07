print ("hello world")
todays_date = "21-11-2024"
print ("the date of day is", todays_date)
x = 2 * 2
product = x
remainder = 1398 % 11
print ("",product,remainder)




january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

september_rainfall = 5.16
october_rainfall = 7.20
november_rainfall = 5.06
december_rainfall = 4.06
annual_rainfall += september_rainfall
print ("",annual_rainfall)



city_name = "St. Potatosburg"

#city_pop = 340000



cucumbers  =  3
price_per_cucumber = 3.25
total_cost = cucumbers * price_per_cucumber
print(total_cost)




quotient = 6/2
# the value of quotient is now 3, which makes sense



quotient = 7/2
# the value of quotient is 3, even though the result of the division here is 3.5

quotient1 = 7./2
# the value of quotient1 is 3.5
quotient2 = 7/2.
# the value of quotient2 is 3.5
quotient3 = 7./2.
# the value of quotient3 is 3.5



quotient1 = float(7)/2 
# the value of quotient1 is 3.5


cucumbers = 100.0
num_people = 6.0
# print ('total is',cucumbers/num_people)
# whole_cucumbers_per_person =  cucumbers / num_people
# print ('total is',whole_cucumbers_per_person)
float_cucumbers_per_person = cucumbers / num_people
print (float_cucumbers_per_person)






# Hi! I'm Maria and I live in script.py.
# I'm an expert Python coder.
# I'm 21 years old and I plan to program cool stuff forever.

age_is_12 = False
name_is_maria = True









float_1 = 0.25
float_2 = 40.0

product = float_1 * float_2
big_string = "The product was " + str(product)
------------------------------------------------

, let’s see how we can change them using string methods.

String methods let you perform specific tasks for strings.

We’ll focus on four string methods:

Preview: Docs Returns the length of an object, which can either be a sequence or collection.
len()
lower()
upper()
Preview: Docs Loading link description
str()
Let’s start with len(), which gets the length (the number of characters) of a string!

"""
Description:
Author:  
"""
STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %s s were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %s s very %s. Concerned, %s texted _, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where _s ruled the world."


print STORY
name = raw_input("Enter a name :  ")
######
adj1 = raw_input("input 1 :  ")
adj2 = raw_input("input 2 :  ")
adj3 = raw_input("input 3 :  ")
##########
verb = raw_input("Input UR Verb : ")
#############
noun1= raw_input("Enter UR Noun1 : ")
noun2= raw_input("Enter UR Noun2 : ")
################
animal = raw_input("Enter *An Animal :  ")
food = raw_input("Enter *A Food :  ")
fruit = raw_input("Enter *A Fruit :  ")
superhero = raw_input("Enter *A Superhero :  ")
country = raw_input("Enter *A Country :  ")
dessert = raw_input("Enter *A Dessert :  ")
year = raw_input("Enter *A Year :  ")
##############3
print STORY % (name, adj1, adj2, animal, food, verb, noun1, fruit, adj3, name, superhero, name, country, name, dessert, name, year, noun2)


"""
Description:
Author:  
"""
'''STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %s s were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %s s very %s. Concerned, %s texted _, who flew _ to %s and dropped %s in a puddle of frozen %s. %s woke up in the year _, in a world where _s ruled the world."

name = input("Enter a name :  ")
######
adj1 = input("input 1 :  ")
adj2 = input("input 2 :  ")
adj3 = input("input 3 :  ")
##########
verb = input("Input UR Verb : ")
#############
noun1= input("Enter UR Noun1 : ")
noun2= input("Enter UR Noun2 : ")
################
Animal = input("Enter *An Animal :  ")
Food = input("Enter *A Food :  ")
Fruit = input("Enter *A Fruit :  ")
Superhero = input("Enter *A Superhero :  ")
Country = input("Enter *A Country :  ")
Dessert = input("Enter *A Dessert :  ")
Year = input("Enter *A Year :  ")
############3
print ((STORY) (name,adj1,adj2,Animal,Food,verb,noun1,Fruit,adj3,name,Superhero,name,Dessert,name,Year,noun2,))
'''


"""
Description:
Author:  
"""
'''STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %s s were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %s s very %s. Concerned, %s texted _, who flew _ to %s and dropped %s in a puddle of frozen %s. %s woke up in the year _, in a world where _s ruled the world."

name = input("Enter a name :  ")
######
adj1 = input("input 1 :  ")
adj2 = input("input 2 :  ")
adj3 = input("input 3 :  ")
##########
verb = input("Input UR Verb : ")
#############
noun1= input("Enter UR Noun1 : ")
noun2= input("Enter UR Noun2 : ")
################
Animal = input("Enter *An Animal :  ")
Food = input("Enter *A Food :  ")
Fruit = input("Enter *A Fruit :  ")
Superhero = input("Enter *A Superhero :  ")
Country = input("Enter *A Country :  ")
Dessert = input("Enter *A Dessert :  ")
Year = input("Enter *A Year :  ")
############3
print ((STORY) (name,adj1,adj2,Animal,Food,verb,noun1,Fruit,adj3,name,Superhero,name,Dessert,name,Year,noun2,))
'''




Equal to (==)


Not equal to (!=)


Less than (<)

Less than or equal to (<=)


Greater than (>)

Greater than or equal to (>=)

def Store():
    print ("You've just entered To the Egy Store ")
    print ("Do you take the Movie on the CD or the DVD?")
    answer = input("Type CD or DVD and hit 'Enter'.").lower()
    if answer == "CD" or answer == "cd" or answer == "Cd":
        print ("This is the Your CD ")
    elif answer == "DVD" or answer == "dvd" or answer == "Dvd":
        print ("Of course this is the DVD")
    else:
        print ("You didn't pick CD or DVD! Try again.")
        Store()

Store()






