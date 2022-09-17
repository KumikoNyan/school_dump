# Piglatin
user_input = input('Enter a Sentence: ').lower()
words = user_input.split()

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
both = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ñ', 'ñ']


for x, word in enumerate(words):
    if word[0] in vowels:

        if word[-1] not in both:
            words[x] = word[:-1] + "way" + word[-1] + "\n"
        
        if word[-1] in both:
            words[x] = words[x] + "way\n"

    else:

        has_vowel = False

        for z, letter in enumerate(word):

            if letter in vowels:
                if word[-1] not in both:
                    words[x] = word[z:-1] + word[:z] + "ay" + word[-1] +"\n"
                    has_vowel = True
                    break
    
        for y, letter in enumerate(word):

            if letter in vowels:
                if word[-1] in both:
                    words[x] = word[y:] + word[:y] + "ay\n"
                    has_vowel = True
                    break


pig_latin = ' '.join(words)
print("Pig Latin:\n",pig_latin)