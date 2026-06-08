def is_palindrome(text):
    text = "".join(char.lower() for char in text if char.isalnum())
    return text == text[::-1]


input_text = input("Enter a string: ")
if is_palindrome(input_text):
    print(f'"{input_text}" is a palindrome.')
else:
    print(f'"{input_text}" is not a palindrome.')


def reverse_text(text):
    return text[::-1]


my_text = input("Enter a string to reverse: ")
reversed_text = reverse_text(my_text)
print(f"Reversed Text: {reversed_text}")
