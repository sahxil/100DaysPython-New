student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

max1 = -float('inf')

for i in student_scores:
    if i > max1:
        max1 = i

print(max1)