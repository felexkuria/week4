# Write a program that reads the content 
# of a text file and then prints the content to the console.
file =open("felex.txt", "r")

data = file.read()

print(data)