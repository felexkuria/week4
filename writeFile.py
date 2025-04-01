file=open("file.txt","w")
data =file.write("Hello, \n I am writing to a file")
print(data)

#write a random cstring to a file
file =open("schedule.csv", "w")
data =file.write("Monday, \n Tuesday,\n Wednesday, Thursday, Friday, Saturday, Sunday")
print(data)