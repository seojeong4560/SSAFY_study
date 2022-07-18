#사용자가 입력한 각 자릿수를 더해 출력하는 코드

print("숫자를 입력하세요")
num = input()

print(sum(int(n) for n in num))