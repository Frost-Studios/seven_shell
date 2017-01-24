"""

Adam Cherun
1/23/2017

This project's purpose is to create a Python module that can process the English language. 

----

TODO:

...

"""


class Base:
	
        @staticmethod
        def return_punc():
		
                """
                purpose:
                to return any possible puncuation 

                variables: 
                punc = ['.', ',', '/', '!', '(', ')', '[', ']', '{', '}', "'", '"']

                returns: 
                punc
                """

                punc = ['.', ',', '/', '!', '(', ')', '[', ']', '{', '}', "'", '"']

                return punc
		
        @staticmethod
        def return_vowels():
		
                """
                purpose: 
                to return the vowels of the English language

                variables:
                vowels = ['a', 'e', 'i', 'o', 'u']

                returns:
                variables
                """

                vowels = ['a', 'e', 'i', 'o', 'u']

                return vowels

class Filter:
	
	
        """
        purpose:
        to contain functions relevant to filtering sentences
        """

        def __init__(self):
                
                """
                purpose:
                to initalize the Filter class
                
                variables:
                self.filter_words = None
                """
                
                self.filter_words = None
	
        def load_filter_words(self):
                
                """
                purpose: 
                to load the hardcoded set of filter filter filter_words
                """
                
                self.filter_words = ["a", "an", "but", "can", "do", "for", "get", "it", "just", 
                        "there", "that", "the"]
                
        def add_filter_words(self, w):
                
                """
                purpose:
                to add filter words to self.filter_words
                """
                
                if type(w) is str:
                
                        self.filter_words.append(w)
                        
                else:
                        
                        print("Error: not string. || add_filter_words(self,w)")
                        
        def print_filter_words(self):
                
                """
                purpose:
                to print filter_words
                """
                
                print(self.print_filter_words)
                
        def return_filter_words(self):
                
                """
                purpose:
                to return the list self.filter_words
                
                returns:
                list of filter'd words
                """
                
                return self.filter_words
                
        def filter_sentence(self, s, t):
                
                """
                purpose:
                to filter a word; remove all words that are in self.filter_words
                
                returns:
                final seperated into a list or string (if t = 0, return is list; if t = 1, return is a string)
                """
                
                temp_word_list = []
                temp_buffer = ""
                
                length = len(s)
                i = 0
                
                for letter in s:
                        
                	i += 1 

                        if i == length and not temp_buffer in self.filter_words:
                                temp_buffer += letter
                                temp_word_list.append(temp_buffer)
                        elif letter == " ":
                                if temp_buffer in self.filter_words:
                                        temp_buffer = ""
                                        pass
                                else:
                                        temp_word_list.append(temp_buffer)
                                        temp_buffer = ""
                        else:
                                temp_buffer += letter
                                
                
                if t == 1:
                        return temp_word_list
                elif t == 2:
                        temp_string = ""
                        for item in temp_word_list:
                                temp_string += item
                                temp_string += " "
                        return temp_string
                else:
                        print("Error: type not found. || filter_sentence()")
			
				
A = Filter()
A.load_filter_words()
f = A.filter_sentence("Hello my name is Bob I am an rhino", 2)
print(f)

