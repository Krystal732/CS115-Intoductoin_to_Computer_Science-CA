def same(word):
    """
        Returns True if the word has the same character for the first and last letters
        Otherwise returns False
    """
    return word[0].lower() == word[len(word)-1].lower()


def consecutiveSum(x, y):
    """
        Returns the sum of consecutive integer numbers between x and y (both x,y not included)
    """
    return ((x+y)*(y-x-1))/2

    
