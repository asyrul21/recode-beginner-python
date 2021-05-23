# The palindrome Checker
# 1. create a varible named word and assign it to the input() statement you learned last week
# 2. Transform this word to all lowercase by performing word.lower()
# 3. Set a flag named Palindrom and set it to True
# 4. Setup a for loop with enumeration, and check that the current letter must
# be equals to the letter at the same position from the bacl
# 5. If this is not true, you may change Palindrom to False, and break from the loop
# 6. Finally, if Palindrome is True, output something. Else, output a different message.


print("Welcome to the Palindrome Checker")
print()

word1 = input("Insert a word: ")
word1 = word1.lower()

palindrome = True
for idx, letter in enumerate(word1):
    if word1[idx] == word1[len(word1) - (idx + 1)]:
        palindrome = True
    else:
        palindrome = False
        break

print()
if(palindrome):
    print("This is a palindrome!")
else:
    print("Nope this is not.")
