def count_words_and_lines(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)

            print(f"Number of lines in {filename}: {line_count}")
            print(f"Number of words in {filename}: {word_count}")
    except FileNotFoundError:
        print(f"File {filename} not found!")


count_words_and_lines("sample.txt")
count_words_and_lines("fruits.txt")


with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

with open("fruits.txt", "a") as fruits:
    fruits.write("Grapes")

with open("fruits.txt", "r") as fruits:
    new_content = fruits.readlines()
    for line in new_content:
        print(line.strip())

with open("new_file.txt", "a") as file:
    file.writelines(["Hello World!", "I am an AI Engineer", "A fullstack developer"])

with open("new_file.txt", "r") as file:
    content = file.read()
    print(content)
