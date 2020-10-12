# --------------
# Code starts here

# Create the lists 
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']

# Concatenate both the strings
new_class = class_1 + class_2
print(new_class)

# Append the list
new_class.append("Peter Warden")

# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove("Carla Gentry")

# Print the list
print(new_class)


# Create the Dictionary
course = ["Math", "English", "History", "French", "Science"]
marks = [65,70, 80, 70, 60]

#courses = zip(course,marks)
courses = {}
for i,j in zip(course,marks):
    courses[i] = j
print(courses)

# Slice the dict and stores  the all subjects marks in variable


# Store the all the subject in one variable `Total`
total = sum(marks)

# Print the total
print(total)

# Insert percentage formula
percentage = (total / 500)*100

# Print the percentage
print(percentage)



# Create the Dictionary
student = ["Geoffrey Hinton", "Andrew Ng", "Sebastian Raschka", "Yoshua Benjio", "Hilary Mason", "Corinna Cortes", "Peter Warden"]

marks = [78, 95, 65, 50, 70, 66, 75]

mathematics = {}
for i,j in zip(student,marks):
    mathematics[i] = j
print(mathematics)


# calculate the topper of subject

topper = max(mathematics,key = mathematics.get)
print (topper)


# Given string
print(topper.split(" "))

# Create variable first_name 
first_name = topper.split(" ")[0]

# Create variable Last_name and store last two element in the list
Last_name = topper.split(" ")[1]

# Concatenate the string
full_name = Last_name +" "+ first_name

# print the full_name
print(full_name)

# print the name in upper case
certificate_name = full_name.upper()
print(certificate_name)
# Code ends here


