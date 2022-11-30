import string



### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        #pass #delete this line and replace with your code here
        
        # string.ascii_lowercase and string.ascii_uppercase
        # string.punctuation, plus the space (' ') and all 
        # numerical characters (0 - 9) found in string.digits
        
        #assign variables to lower then uppercase letters and create a dict
        lowerletters = string.ascii_lowercase
        upperletters = string.ascii_uppercase
        
        letter_dict = {}
        
        
        #iterate through the first then second string, adding each value to the dictionary with
        #increasing value
        for i in range(0, len(lowerletters)):
                letter_dict[i] = lowerletters[i]
        for i in range(0, len(upperletters)):
                letter_dict[i+26] = upperletters[i]
        
        #print (letter_dict)
        #assert input conditions true
        
        assert 0 <= shift < 26
        #within whole code you can use a while loop, try and the except to ask for repeated input
        
            
        #make a copy of the dictionary and add the shift to each key whilst adjusting
        #for circular movement
        
        
        ####case before adjustment for circular movement:
            # for i in letter_dict:
            # # where i is between 0-26 and does not require shuffling back
            # shift_dict[i+shift] = letter_dict[i]
        
        shift_dict = {}
        
        for i in letter_dict:
            
            # where i is between 0-26 and does not require shuffling back
            if 0 <= (i + shift) <= 25:
                #print (letter_dict[i])
                shift_dict[i+shift] = letter_dict[i]
            #where i is between 0-26 and does require shuffling
            if i < 26 and i+shift > 25:
                shift_dict[i+shift-26] = letter_dict[i]
           
            #where is between 27-51 and does not require shuffling
            if 26 <= (i + shift) <= 51:
                shift_dict[i+shift] = letter_dict[i]
           
            #where i is between 27-51 and requires shuffling
            if i > 25 and i+shift > 51:
                
                shift_dict[i+shift-26] = letter_dict[i]
                
        #lettershift_dict assigning the original letters as keys to 
        #corresponding shifted letters as values
        
        lettershift_dict ={}
        
        #assign values of letter_dict as keys corresponding to values of shift_dict
        for i in letter_dict:
            #lettershift_dict[letter_dict[i]] = shift_dict[i]
            #shift_dict[i] = lettershift_dict[letter_dict[i]] 
            lettershift_dict[shift_dict[i]] = letter_dict[i]
        
        # print (letter_dict) 
        
        # print ("")
        
    
        # print (shift_dict)
        
        # print ("")
        
    
        # print (lettershift_dict)
        
        
        
        
    
        #return the dictionary
        return lettershift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        #pass #delete this line and replace with your code here
        
        #use self.get_message_text() to access the message and create local dict
        shift_dict = self.build_shift_dict(shift)
        #print (shift_dict)
        
        mess = self.get_message_text()
        
        #create a string to return
        new_mess = ''
        #print (mess)
        
        #PUNCTUATION
        punct = string.punctuation
        punct += ' '
        punct += string.digits
        
        
        #add each shifted letter to a new string or if punctuation add as is
        for char in mess:
            
            if char not in punct: # string.punctuation, plus the space (' ') and all 
        # numerical characters (0 - 9) found in string.digits
            #print (char)
                new_mess += str(shift_dict[char])
            else:
                new_mess += char
        
        #return string
        #print(new_mess)
        return(new_mess)
        
            
        
        
        
        



class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text) DONE
            self.valid_words (list, determined using helper function load_words) DONE
            self.shift (integer, determined by input shift) DONE
            self.encrypting_dict (dictionary, built using shift) DONE?
            self.message_text_encrypted (string, created using shift) DONE?

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        #pass #delete this line and replace with your code here
        
        #sets message_text and valid_words
        Message.__init__(self, text)
        
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)
        
        
        
        

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        #pass #delete this line and replace with your code here
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        #pass #delete this line and replace with your code here
        copy_encrypting_dict = self.encrypting_dict.copy()
        return copy_encrypting_dict
        

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        #pass #delete this line and replace with your code here
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        #pass #delete this line and replace with your code here
        
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        #pass #delete this line and replace with your code here
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        #pass #delete this line and replace with your code here
        
        greatestvalidwords = 0
        bestdecrypt = (0, Message.get_message_text(self))
        decryptstring = ''
        decryptwords = []
        
        
        #iterate over the encrypted message with 26 shifts increasing by one each time
        #inclusive of checking the message itself as decrypted
        for i in range(0,26):
            
            #over each iteration, get the new string 
            decryptstring = self.apply_shift(i)
            
            #split the string by spaces 
            decryptwords = decryptstring.split(' ')
            #print (decryptwords)
            
            #check if each word is in valid words(which ignores punctuation) and count
            counter = 0
            for y in decryptwords:
                
                if is_word(CiphertextMessage.get_valid_words(self), y):
                    counter += 1
                
            
            #if the no. of valid words is greater than what we have, store the shift value
            #and the string in the tuple, if equal do not store
            if counter > greatestvalidwords:
                
                greatestvalidwords = counter
                #print (counter, i)
                bestdecrypt = (i, decryptstring)
            
            
            
        #return the bestdecrypt
        return bestdecrypt
            
            
        

#Example message test case
# build_shift_dict(self, shift)

# message = Message('Nonsense words: remind front animal severe clerk mistake flow pull complain splendid tire town old vowel tear food weekday stir baby record engineer ring surround suggest afraid profession somewhere hollow sink raise furniture active sea possible destructive')
# message.build_shift_dict(2)
# print (message.apply_shift(22))



#Example test case (PlaintextMessage)
# plaintext = PlaintextMessage('hello', 2)
# print('Expected Output: jgnnq')
# print('Actual Output:', plaintext.get_message_text_encrypted())

# dictionary = plaintext.get_encrypting_dict()
# print (dictionary)



def decrypt_story():
    encryptstory = CiphertextMessage(get_story_string())
    return encryptstory.decrypt_message()

print(decrypt_story())
