import re


# Python program to read an entire text file.
with open("mybio.txt", "r") as file:
    content = file.read()
    print(content)
print("-----------------------------------------------------------------------")

# Write a text file.
with open("mybio.txt", "w") as file:
    file.write("My name is Kevin, and this is a file text I have created from the MacBook terminal window so that I can use to practice file handling in Python.\n")
    file.write("Anyway, I am from Nairobi Kenya, but as I type this, I am in Dubai, and I am using my free time to learn Python as a programming language.\n")
    file.write("It has been an exhilarating journey, with lots of frustrations and learning.\n")
print("-----------------------------------------------------------------------")
with open("mybio.txt", "r") as file:
    content = file.read()
    print(content)
    first_line = content.split("\n")[0]
    print(first_line)
print("-----------------------------------------------------------------------")

# Append a line in the text file
with (open("mybio.txt", "a")) as file:
    file.write("This last line was appended.")
print("-----------------------------------------------------------------------")
with open("mybio.txt", "r") as file:
    content = file.read()
print(content)
print("-----------------------------------------------------------------------")

# Python program to read a file line by line and store it into a list.
with open("mybio.txt", "r") as file:
    content = file.read()
    print(content.split("\n"))
print("-----------------------------------------------------------------------")

# or
with open("mybio.txt", "r") as file:
    lines = file.readlines()  
    print(lines)
print("-----------------------------------------------------------------------")
with open("mybio.txt", "r") as file:
    line = file.readline()  
    print(line)
print("-----------------------------------------------------------------------")

# Python program to find the longest words.
word_length = 1
longest_word = ""
with open("mybio.txt") as file:
    content = file.read()
words = re.findall(r"\w+", content)
for word in words:
    if len(word) > word_length:
        word_length = len(word)
        longest_word = word

print(f"The longest word in the 'mybio.txt' is '{longest_word}' with {word_length} characters.")
