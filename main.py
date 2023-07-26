#ctrl+c is cancel. it helps to get out of accidental infinite loops



"""
#Printing 3by3 square using loop in loop


def main():
  print_square(3)

def print_square(size):

  #For each row
  for i in range(size):
  
    #for each brick in row
    for j in range(size):
    
      #print brick in row, but keep in same line
      
      print("#", end="")
      
    #print new line i.e enter
    print()

main()
    



#building a dictionary where key is name / house / hobbies. and in each name it is a key and has values i.e. dict in dict
#Use of None here is a feature in Python to have no value in it rather than empty
students = [
  {"name":"KK", "house":"BRD", "hobbies":"BB"},
  {"name": "Tim", "house": "BRD", "hobbies":"Lan"},
  {"name": "Ed", "house": "Breakout", "hobbies":None}  
]

for student in students:
  print(student["name"], student["house"], student["hobbies"], sep=", ")



#below prints the name and where they are from.
students = {
  "JJ": "AIA",
  "Ed": "Breakout",
  "Tim": "BF",
}

for student in students:
  print(student, students[student], sep=", ")



# dict uses { } . unrelated to f strings
#lists have location that is numeric. but dict can index by words
#the below can't print. only can have 1 unique key. the workaround is {"fruit": ["apple", "banana"]}
types = {
  "fruit": "apple",
  "fruit": "banana",
  "vegetable": "lettuce",
}

print(types["fruit"])

#below will print keys only

students = {
  "JJ": "AIA",
  "Ed": "B",
  "Tim": "BF",
}

for student in students:
  print(student)


#range doesn't take strings, it takes only int. Hence, use of len to print a list
#nesting len in range, it returns range an int, thus able to print the strings in list using range. this is same as range(3)
# i + 1 shows the ranking of the students, starting not from 0, but from 1
students = ["JJ", "Tim", "Ed"]

for i in range(len(students)):
  print(i + 1, students[i])



#Using for loop to print all the students

students = ["Tim", "JJ", "Ed"]

for student in students:
  print(student)


#Using a list aka [ ] and printing them based on their index. But this doesn't help when adding more students

student = ["Tim", "JJ", "Ed"]

print(student[0])
print(student[1])
print(student[2])


#meow 3 times, using your own created fn

def main():
  number = get_number()
  meow(number)

def get_number():
  while True:
    i = int(input("Number: "))
    if i > 0:
      return i

def meow(n):
  for _ in range(n):
    print("meow")

main()


#simpler version if while True

while True:
  n = int(input("What's n? "))
  if n > 0:
    break
    
for _ in range(n):
  print("meow")


#ask user an input. keep asking using the "While True" and continue if -ve. if positive int, then break = stop

while True:
  n = int(input("What's n? "))
  if n < 0:
    continue
  else:
    break
print("meow" * n)


#\n is to make new line. end="" is to remove the extra line at the end

print("meow\n" * 3, end="")

#meow 3 times using range. _ here is pythonic and indicating we're not using it for any other purpose. it is so that we can use the range fn

for _ in range(3):
  print("meow")


#another way to meow 3 times, using "for" and a list (characterized by square brackets)

for i in [0, 1, 2]:
  print("meow")

# meow 3 times
i = 0
while i < 3:
  print("meow")
  i += 1
  #above is basically i = i + 1
  # i < 3 as we start from 0, then 1, then 2. Total 3 times. 

  """