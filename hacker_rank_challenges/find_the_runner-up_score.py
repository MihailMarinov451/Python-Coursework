
n = int(input())
arr = map(int, input().split())

maxScore = -200
runnerUpScore = -200
for i in arr:
    if maxScore < i:
        runnerUpScore = maxScore
        maxScore = i
    elif i < maxScore and i > runnerUpScore:
        runnerUpScore = i

print(runnerUpScore)


