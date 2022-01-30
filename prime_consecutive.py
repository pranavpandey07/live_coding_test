
#Question no1 solution.
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


#Question no 2 solution

def strictly_smaller_strictly_bigger(nums):
    new=[]
    for i in range(0,len(nums)):
        greater=0
        smaller=0
        for j in nums:
            if nums[i]>j:
                greater=greater+1
            elif nums[i]<j:
                smaller=smaller+1
            else:
                pass
        if greater>=1 and smaller>=1:
            new.append(i)
    return len(new)
      
nums = [11,7,2,15]    
strictly_smaller_strictly_bigger(nums)
