# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 13:27:47 2022

@author: chris
"""
print ("Please think of a number between 0 and 100!")




start_value = 1
end_value = 100
midpoint = 0
inp = "baseline"
accept = 'hlc'

while inp != 'c':
    midpoint = int((end_value + start_value)/2)
    print ("Is your secret number", midpoint, "?")
    inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if inp == 'h':
        end_value = midpoint
        #print (end_value)
    if inp == 'l':
        start_value = midpoint
        #print (start_value)
    if inp == 'c':
        break
    if inp not in accept:
        print ("Sorry, I did not understand your input")



print ("Game over. Your secret number was: ", midpoint  )
