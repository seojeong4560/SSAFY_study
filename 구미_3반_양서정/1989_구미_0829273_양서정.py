T = int(input())
for tc in range(1, T+1):
    word = input()
    for i in range(len(word)//2):
        if word[i] != word[-1 -i]:
            result = 0
        else:
            result = 1
    print("#{} {}".format(tc, result))
