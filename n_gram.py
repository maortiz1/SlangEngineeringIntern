def calculateNGrams(piece_text:str, n : int)-> list:
    """Calculate the n-gras of the given string
    
    Arguments:
        piece_text {str} -- The text from where the ngrams will be calculated
        n {int} -- Length of the desire ngrams
    
    Returns:
        list -- List of the ngrams found in the input string that are of length n
    """

    l = len(piece_text)

    list_slang= [piece_text[idx:idx+n] for idx in range(0,l-n+1)]

    return list_slang

print(calculateNGrams("Slang",10))
print(calculateNGrams("to be or not to be",2))

