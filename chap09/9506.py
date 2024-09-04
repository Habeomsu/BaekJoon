while True:
    a = int(input())
    b=[]
    if a == -1:
        break;
    else:
        for i in range(1,a+1):
            if a%i==0 and a!=i:
                b.append(i)
    if sum(b) == a:
        b=list(map(str,b))
        answer=" + ".join(b)
        print(f'{a} = {answer}')
    else:
        print(f'{a} is NOT perfect.')