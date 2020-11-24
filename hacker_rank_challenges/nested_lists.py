def printSecondLowestGrade(records):

    minGrade = records[0][1]
    records = list(filter(lambda x: x[1] > minGrade, records))
    minGrade = records[0][1]
    records = list(filter(lambda x: x[1] == minGrade, records))
    records = sorted(records, key = lambda x: x[0])

    for i in records:
        print(i[0])

    return 1



records = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name,score])

records = sorted(records, key=lambda x: x[1])

printSecondLowestGrade(records)
