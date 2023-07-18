'''
Created on _______________________
@author:   _______________________

CS515 - Hw 2
'''
import sys
from functools import reduce
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo', 'spam', 'spammy', 'zzyzva']

# Implement your functions here.
def letterScore(letter, scorelist):
    if scorelist == []:
        return 0
    elif letter == scorelist[0][0]:
        return scorelist[0][1]
    else:
        return letterScore(letter, scorelist[1:])
    
def wordScore(S, scorelist):
    if S == "":
        return 0
    else:
        return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def scoreList(Rack):
    y = filter(lambda x : word_in_rack(x, Rack), Dictionary)
    return list(map(lambda word: [word, wordScore(word, scrabbleScores)], y))

    
def bestWord(Rack):
    sList = scoreList(Rack)
    if sList == []:
        return ["",0]
    return reduce(lambda x,y: x if x[1]>y[1] else y, sList)


def word_in_rack(word, Rack):
    if len(word) == 1 and word[0] in Rack:
        return True
    elif word[0] in Rack:
        index_letter = Rack.index(word[0])
        return word_in_rack(word[1:], Rack[:index_letter] + Rack[index_letter + 1:])
    else:
        return False











    
    
