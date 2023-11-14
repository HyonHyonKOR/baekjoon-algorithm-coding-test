score_count = int(input())

score_list = list(map(int, input().split()))
high_score = max(score_list)
new_score_list = list(map(lambda score: score/high_score*100, score_list))

print(sum(new_score_list) / len(new_score_list))