#importing libraries
import math

#some context for the user
print()
print("This program is designed to calculate interest for either investments or bonds...")
print()
print("You can choose by typing either 'investment' or 'bond': ")


#asking would they like bond or investment
user_input = input("What type would you like to calculate today?\n")
print()

#is the user entering a specified term, if not ask again
while user_input.lower() not in ["bond", "investment"]:
    print(user_input + " is not a valid selection...")
    user_input = input("please enter 'investment' or 'bond' \n")
    
#Investment logic
if user_input.lower() == "investment":
    print("Investment selected:")
    
    #asking users the terms of the finance and converting values
    amount_deposited = input("How much would you like to deposit? (no '£' needed)\n")
    interest_rate = input("What is the interest rate you would like to use? (no '%' needed)\n")
    number_years = input("How many years do you want to invest for?\n")
    user_input = input("Would you like to calculate using 'simple' or 'compound' method?\n")
    
    r = float(interest_rate) / 100
    p = float(amount_deposited)
    t = float(number_years)
    
    #Interest Check
    while user_input.lower() not in ["simple", "compound"]:
        user_input = input("please enter 'simple' or 'compound'\n")
    
    #Simple   
    if user_input.lower() == "simple":
        a = p * (1+r*t)
        print("Depositing £" + amount_deposited + " with an interest rate of " + interest_rate + " %" + " for " + 
              number_years + " years using simple interest will return you:")
        print("£" + format(a, '.2f'))
    
    #Compound
    elif user_input.lower() == "compound":
        a = p*math.pow((1+r),t)
        print()
        print("Depositing £" + amount_deposited + " with an interest rate of " + interest_rate + " %" + " for " + 
              number_years + " years using compound interest will return you:")
        print("£ " + format(a, '.2f'))
        
        
        
        
    
#Bond logic
elif user_input.lower() == "bond":
        print("Bond selected")
        print()
        
        house_value = input("what is the current value of the property? (no '£' needed)\n")
        print()
        
        interest_rate = input("What is the interest rate you would like to use? (no '%' needed)\n")
        print()
        
        number_months = input("And how many months are you looking to repay in?\n")
            
        p = float(house_value)
        i = (float(interest_rate)/100)/12
        n = int(number_months)
        
        repayment = (i*p)/(1-(1+i)**(-n))
        
        print()
        print("For a house costing £" + house_value + " with an interest rate of " + interest_rate + " %" + " over " + 
              number_months + " months, your monthly repayment will be: ")
        print("£ " + format(repayment, '.2f'))
              
              
              
              
        
print()       
print("Finished")