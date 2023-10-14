# scores = (100, 98, 99)
# print(scores)
# scores[1] = 99  # 'tuple' object does not support item assignment
# print(scores)

scores = (100, 98, 99)
print(scores)
scores_list = list(scores)  # 리스트로 변환
print(scores_list)
scores_list[1] = 99  # 리스트 상태에서 수정 후
scores = tuple(scores_list)  # 튜플로 변환
print(scores)
