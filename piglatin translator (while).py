# Piglatin translator (While loops ver.)

# some lists
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
both = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ñ', 'ñ']

# main
user_input = input("Enter a sentence: ").lower()
words = user_input.split()
w_count = 0

# where i suffered
while w_count < len(words):

    # putting the list into the loop
    words = user_input.split()

    # first letter vowel check
    if words[w_count][0] in vowels:

        # if punct
        if words[w_count][-1] not in both:
            rvp = words[w_count][:-1] + "way" + words[w_count][-1]
            print(rvp)
        
        # if no punct
        if words[w_count][-1] in both:
            rv = words[w_count] + "way"
            print(rv)

    
    if words[w_count][0] not in vowels:

        a = words[w_count].find('a')
        A = words[w_count].find('A')
        e = words[w_count].find('e')
        E = words[w_count].find('E')
        i = words[w_count].find('i')
        I = words[w_count].find('I')
        o = words[w_count].find('o')
        O = words[w_count].find('O')
        u = words[w_count].find('u')
        U = words[w_count].find('U')

    # based on the vowels list
        vowel_list = [a, e, i, o, u, A, E, I, O, U]

        vowel_list.sort()
        while -1 in vowel_list:
            vowel_list.remove(-1)
    
        # we want to find first vowel in the word
        find_vowel = vowel_list[0]

        # if punct for consonant
        if words[w_count][-1] not in both:
            rcp = words[w_count][find_vowel:-1] + words[w_count][0:find_vowel] + "ay" + words[w_count][-1]
            print(rcp)
        
        # if no punct for consonant
        if words[w_count][-1] in both:
            rc = words[w_count][find_vowel:] + words[w_count][0:find_vowel] + "ay"
            print(rc)
    
    # to exit the loop
    w_count += 1