# input percentage
# input grade
# marks ( total marks = 100 marks)
# Results: pass or fail
# grade A = 90-100 marks or percentage >= 90
# grade B = 80-89 marks or percentage >= 80
# grade C = 70-79 marks or percentage >= 70
# grade D = 60-69 marks or percentage >= 60
# grade F = 50-59 marks or percentage >= 50

percentage = float(input("Enter percentage:"))
grade = input("Enter grade (A, B, C, D, F, G):")
marks = int(input("Enter your marks:"))

if percentage >= 50 and \
                (grade == "A" or grade == "B" or grade == "C" or grade == "D" or grade == "F") and \
                marks >= 50:
    
    print("Congratulations! You have passed the exam:")
else:
    print("You have failed the exam:")