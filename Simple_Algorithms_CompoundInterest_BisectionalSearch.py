# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 15:50:23 2022

@author: chris
"""
''' this code gives the minimum monthly payments required to pay off a debt within a year
 (to 1 pence accuracy) when given the balance of the debt and annual interest rate
 it calculates this by bisection search 
 I believe the complexity should be O(logn) --> bisectional search, where n is the size of the integer balance, as this
 increases the search range of the code
 I do not think the interest rate should affect the complexity as it represents a fixed percentage increase 
 each month'''


balance = 120
annualInterestRate = 0.2

#Monthly interest rate = (Annual interest rate) / 12.0
#Monthly payment lower bound = Balance / 12
#Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0


def YearBalance(balance, annualInterestRate, payment):
    '''
    given balance, decimal interest rate and a montly payment
    outputs a remaining balance
    '''
    months = 0
    totalpaid = 0
    #print (payment)
    
    while months < 12:
        balance -= payment
        totalpaid += payment
        balance += ((annualInterestRate/12)*balance)
        #print ("Month:", months, " Remaining balance:", round(balance, 2))
        months += 1
    #returns an approximation of the neccessary balance
    return balance


#payment estimate that always is underestimate

LB = (balance/12)
UB = (balance*(1+(annualInterestRate/12))**12)/12
payment = (LB + UB)/2
#print (YearBalance(balance, annualInterestRate, payment))
epsilon = 0.01


#until balance reaches suitably close to 0
while abs(YearBalance(balance, annualInterestRate, payment)) >= epsilon:
    payment = (LB + UB) / 2 
    #set the  payment value at the midoint between bounds
    #print ("LB: ", LB, " UB: ", UB, "payment: ", payment, "balance", YearBalance(balance, annualInterestRate, payment))
    
    if YearBalance(balance, annualInterestRate, payment) < 0: 
        UB = payment
    #if remaining balance is positive set UB as midpoint
    elif YearBalance(balance, annualInterestRate, payment) > 0:
        LB = payment
    #if remaining balance is negative set LB as midpoint
    elif YearBalance(balance, annualInterestRate, payment) == 0:
        break
    #print (payment)
    



        
    
    


print ('Lowest Payment: ', round(payment, 2))
