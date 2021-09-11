import string

def cipher_cipher_using_lookup(text,  key, characters = string.ascii_lowercase, decrypt=False):

 if key < 0:

    print("key cannot be negative")

return None

    n = len(characters)

 if decrypt==True:

          key = n - key
          
    table = str.maketrans(characters, characters[key:]+characters[:key])
    
    translated_text = text.translate(table)
    
    return translated_text

            translated += LETTERS[num]
        else:
            translated += symbol
return translated

 if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
    input()