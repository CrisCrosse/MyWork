# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 15:50:23 2022

@author: chris
"""

balance = 4773
annualInterestRate = 0.2




	      
# Result Your Code Should Generate Below:
#Remaining balance: 31.38

def MinFixedPay(balance, annualInterestRate):
    '''
    given balance and decimal interest rate
    outputs the minimum monthly payment as a multiple of 10 to pay off the debt in a year
    '''
    
    

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
    payment = ((balance/12)//10)*10
#increases payment by 10 until 0 or negative account balance reached
    while YearBalance(balance, annualInterestRate, payment) >= 0:
        payment += 10
#returns iterated payment value
    return payment

        
    
    


print ('Lowest Payment: ', MinFixedPay(balance, annualInterestRate))
