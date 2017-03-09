# Program to sort alphabetically the words form a paragraph provided by the user

my_str = "Hello this Is an Example With cased letters"

#my_str = input("Enter a paragraphs: ")

words = my_str.split()

words.sort()

print("The sorted words are:")
for word in words:
   print(word)
