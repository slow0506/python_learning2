word = input()
if len(word) % 2 == 0:
    middle = int(len(word)/2)
elif len(word) % 2 == 1:
    middle = int((len(word)-1)/2)

for n in range(0, middle+1):

    if word[n] != word[len(word)-1 - n]:
        print("Not palindrome")
        break
else:
    print("Palindrome")



