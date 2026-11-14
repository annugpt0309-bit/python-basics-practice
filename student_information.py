name = input("Enter your name: ")
roll_number = input("enter your roll no.: ")
marks1 = int(input("Enter marks in subject 1: "))
marks2 = int(input("Enter marks in subject 2: "))
marks3 = int(input("Enter marks in subject 3: "))

total = marks1 + marks2 + marks3
average = total/3

print("----- Student Information -----")
print(f"Name: {name}")
print(f"Roll Number: {roll_number}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")