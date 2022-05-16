# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
print(type(student_scores))
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# Task here is done to replicate max() function
high_score  = 0
for x in student_scores:
  if x > high_score:
    high_score = x
print(high_score)



