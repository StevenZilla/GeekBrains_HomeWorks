n = int(input()) 
num_list = list(map(int, input().split())) 
x = int(input()) 
nums_new = [abs(x-i) for i in num_list] 
print(num_list[nums_new.index(min(nums_new))])