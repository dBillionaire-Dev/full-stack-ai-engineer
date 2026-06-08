import re

name_input = input(str("Enter your full name: "))
name = name_input.split()
print(f"Hello {name[0]}, Welcome to our platform")

# split()

sentence = "Python is fun"
words = sentence.split()
# print(words)

# join()
new_sentence = "|".join(words)
# print(new_sentence)


text = "I love Java"
updated_text = text.replace("Java", "Python")
print(updated_text)

messy = "     Hello, World     "
print(messy)
cleaned_text = messy.strip()
print(cleaned_text)
