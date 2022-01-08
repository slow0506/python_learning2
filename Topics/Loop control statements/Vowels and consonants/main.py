word = input()
vowels = "aeiou"
i = 0
for w in word:
    if word[i].isalpha():
        if w in vowels:
            print("vowel")
        else:
            print("consonant")
        i = i + 1
    else:
        break
