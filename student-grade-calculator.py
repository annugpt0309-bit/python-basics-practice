name = input("Enter your name: ")
roll_number = input("enter your roll no.: ")
marks1 = int(input("Enter marks in subject 1: "))
marks2 = int(input("Enter marks in subject 2: "))
marks3 = int(input("Enter marks in subject 3: "))

total = marks1 + marks2 + marks3
average = total/3

if total >= 250:
    Grade =  "A"
elif total >= 180:
    Grade =  "B"
elif total >= 130:
    Grade =  "C"
elif total >= 70:
    Grade =  "D"
else:
    Grade =  "F"



if marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
    result = "Pass"
else:
   result = "Fail"      

print("----- Student Information -----")
print(f"Name: {name}")
print(f"Roll Number: {roll_number}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {Grade}")
print(f"Result:{result}")