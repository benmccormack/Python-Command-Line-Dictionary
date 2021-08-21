# Author: Ben McCormack
# Purpose : Python Command Line Dictionary Project
# Date : 21/08/2021


import difflib # library that will be used to detect the similarity between words
from difflib import get_close_matches # Will get close matches to the word that the user has entered

import json # this library will provide a function that allows us to load the json file into the program
data = json.load(open("data.json"))

class Dictionary:
    """
        This class contains all the functions for the dictionary

        ...
        Attributes"
        -----------
            word : str
            Used to store the word entered by the user

            meaning : str
            Used to store the definition(s) that is/are returned to the screen

        Methods:
        -----------
            def __init__(self):
                Declares the word and translation variables.
                Also gets user input for word
            
            def translate(self):
                Coverts users input to all lower case and checks if the word exists as a key in the JSON file,
                if it does it will assign the definition variable its value(s) and call the printDefinition() function.
                In the case the word does not exist, it will call the spellCheck() function.

            def spellCheck(self):
                Uses the get_close_matches() function to check for keys in the dictionary with a similar spelling to that
                of the word entered by the user, picks key with highest similarity and asks user if they meant this word.
                Otherwise returns a message that word doesn't exist. Also has error check method to check if user has
                entered Y/N to signify if the suggested word is what they meant. Calls printDefinition() function if the
                user signifies that the suggested word is what they meant.

            def printDefinition(self):
                Prints the definition of the word, checks if the word has multiple defintions by checking if its type is a
                list, if this is the case then each definition is printed on a new line. If the word only has a single meaning
                then the meaning us returned



    """
    def __init__(self):
        word = input("Enter word: ")
        self.word = word
        self.meaning = str



    def translate(self):
        self.word = self.word.lower()

        if self.word in data:
            self.meaning = data[self.word]
            self.printMeaning()
        else:
            self.spellCheck()

    def spellCheck(self):
        if len(get_close_matches(self.word, data.keys()))>0:
            answer = input("Did you mean %s instead? Enter Y is yes or No if no    " % get_close_matches(self.word, data.keys())[0]) # get the element in the list with the highest similarity and display it

            if(answer == "Y"):
                self.meaning = data[get_close_matches(self.word, data.keys())[0]]
                self.printMeaning()

            elif(answer == "N"):
                return "Word does not exist, please double check it and try again"

            else:
                return "Invalid character entered"

        else:
            return "Word does not exist, please double check and try again"

    def printMeaning(self):
        if(type(self.meaning) == list):
            for item in self.meaning:
                print(item)
        else:
            print(self.meaning)

d = Dictionary()
d.translate()


