total_value = int(input("what is the amount of questions? "))
scores = []
x = 0
while x <= total_value:
    raw_score = total_value - x
    percent_score = raw_score / total_value * 100
    x = x + 1
    scores.append(percent_score)

for index, score in enumerate(scores):
    print(f"-{index}: {score}")