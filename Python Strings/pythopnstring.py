'''String literals in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

Strings can be output to screen using the print function. For example: print("hello").

Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters. However, Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.
'''
'''
Example
Get the character at position 1 (remember that the first character has the position 0):
'''
a = "Hello, World!"
print(a[1])
'''The strip() method removes any whitespace from the beginning or the end:'''
print(a.strip())



'''
Example
The len() method returns the length of a string:

'''
a = "Hello, World!"
print(len(a))
'''
Example the lower() Method returns the string  in lower case

 '''
print(a.lower())

""" anther Example  
 The upper() method returns the syting in the upper case
"""
print(a.upper())

""" Another method Example " replace() method" replaces a string with another string"""
print(a.replace("H", "J"))

"""Example
The split() method splits the string into substrings if it finds instances of the separator:"""

print(a.split(",")) # returns ['Hello', ' World!']
