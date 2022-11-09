# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 13:49:13 2022

@author: chris
"""
# s = input("Give string: ")

def Substring(string):
    '''
    where string is a string
    outputs the longest alphabetically ordered substring from the starting character
    '''
    pos1 = 0
    pos2 = 1
    #basecase where just one character is the length
    if len(string) == 1:
        return string
    # while the parser remains alphabetically ordered or equal
    while string[pos1] <= string[pos2]:
        if pos2+1 == len(string):
            return string
        #if the last character is at pos2 return the whole string 
        # code was breaking when clause not included as it would iterate to pos1 
        #being the last character
        else:    
            pos1 += 1
            pos2 += 1
        # iterate through the string until unordered
    return string[:pos2]
    


s = "abcdeopilabcdefghijklmanaspijrbhsazlsajjnaut"


ordsub = {}



for i in range(len(s)):
    temp = s[i:]
    # temp is the substring removing previously iterated characters
    # store the longest substring from the strarting point and the length in a dictionary, 
    ordsub[Substring(temp)] = len(Substring(temp))

lengths = max(ordsub.values())



for y in ordsub:
    if lengths == ordsub[y]:
        print ("Longest substring in alphabetical order is:", y)
        break
        

    
    

# for char in s:
    
#     ordsub[Substring]
    
    




# def slice(a):
#     return num_list[a]

# if slice(2) < slice(3):
#     print ("lower third value than fourth")
# else:
#     print ("higher fourth value than third")

# while (pos2+1) < len(num_list):
#     #until the whole string has been parsed
    
#     #first parsing run based on the first letter being the start
#     if slice(pos1) < slice(pos2):
#         startvalue = pos1
        
    
#         #compare the first and second list values and if in order compare second and third
#         while slice(pos1) < slice(pos2):
#             print ("pos1: ", slice(pos1))
#             print ("pos2: ", slice(pos2)) 
#             if pos2 != (len(num_list)-1):
#                     pos2 += 1
#                     pos1 += 1
#         endvalue = pos2 - 1
            
#         print (startvalue, endvalue)
#         print (s[startvalue:(endvalue + 1)])
        
        
        