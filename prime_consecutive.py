def consecutive_sum_prime_number(g):
    news=[]
    for i in range(1,g):
        count=0
        for j in range(1,g):
            if i%j==0:
                count=count+1
        if count==2:
            news.append(i)
            
    new=news
    k=1
    x=sum(new)
    while x not in news:
        x=sum(new[:-k])
        #print(x)
        #print(new[:-k])
        k=k+1
    return x


consecutive_sum_prime_number(100)
