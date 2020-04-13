def calculateNGrams(piece_text:str, n : int)-> list:
    """Calculate the N-gram of the given string
    
    Complexity:
        The complexity of the algorithm most cases O(l) and worst case O(l*n/2) , l-> length
        of the piece of text, n-> length of the ngrams:
        (l-n+1)+(l-n+1)*n
        (l-n+1)*(1+n)
        l*n-2n+l+2
        l*n/2 - n + l/2 + 1
        O(l*n/2)
    Arguments:
        piece_text {str} -- The text from where the  N-grams will be calculated
        n {int} -- Length of the desire  N-grams
    
    Returns:
        list -- List of the  N-grams found in the input string that are of length n

    """

    #length of the piece of text
    l = len(piece_text)
    # loop to found n_grams, O(l-n+1)-> it loops over the str only one time and indexing in
    #python has a complexity of O(n), algorithm remains to be linear complexity, however complexity
    # may increased as n increases until it reaches l/2, it will decrease after that value. So real complexity
    # taking indexing in python in worst escenario will be O(l*n/2). 
    
    list_slang= [piece_text[idx:idx+n] for idx in range(0,l-n+1)]

    return list_slang


def mostFrequentNGram(piece_text:str, n: int)-> str:
    """Calculate the most frequente N-Gram from the posible  N-grams of the piece of text
    
    Arguments:
        piece_text {str} -- The text from where the  N-grams will be calculated
        n {int} -- Length of the desire  N-grams
    
    Returns:
        str -- Returns the most frequent N-gram found in the piece of text
    """

    n_grams = calculateNGrams(piece_text,n)
    dict_ngrams = dict()
    for n_g in n_grams:
        dict_ngrams[n_g]=0
    common=n_grams[0]
    
    for n_g in n_grams:
        dict_ngrams[n_g]+=1
        if dict_ngrams[common]<dict_ngrams[n_g]:
            common=n_g
    return common

print(calculateNGrams("Slang",2))
print(calculateNGrams("to be or not to be",9))

print(mostFrequentNGram("to be or not to be",2))        

print(mostFrequentNGram("The Internet was done so well that most people think of it as a natural resource like the Pacific Ocean, rather than something that was man-made. When was the last time a technology with a scale like that was so error-free? The Web, in comparison, is a joke. The Web was done by amateurs. " ,4))
