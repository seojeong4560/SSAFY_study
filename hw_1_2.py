score = {
'python': 80,
'django': 89,
'web': 83
}

#성적 딕셔너리에 추가
score['algorithm'] = 90
print(score)

#성적 딕셔너리 수정
score['python'] = 85
print(score)

#전체 과목 평균 점수
average = sum(score.values())/len(score)
print(average)
