n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

tempNum = 0

for i in student_marks[query_name]:
    tempNum += i

print("{:.2f}".format(tempNum/len(student_marks[query_name])))