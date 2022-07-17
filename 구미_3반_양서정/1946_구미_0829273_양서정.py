T=int(input())
for tc in range(1,T+1):
    N=int(input())
    text=''
    for _ in range(N):
        S,n=input().split()
        text+=S*int(n)
    print("#{}".format(tc))
    for i in range(len(text)):
        if i%10==9:
            print(text[i])
        elif i==len(text)-1:
            print(text[i])
        else:
            print(text[i],end='')
