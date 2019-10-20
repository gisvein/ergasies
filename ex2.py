input_file = input("Enter File name : ")
file_txt = open(input_file)
text = file_txt.read()
spaces = 0
tabs = 0
for character in text:
    if character == " ":
        spaces = spaces +1
    if character == "\t":
        tabs +=1
print(spaces)
print(tabs)