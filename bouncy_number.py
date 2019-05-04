def is_bouncy(num):
    increasing, decreasing = False, False
    num_str = str(num)
    for i in range(len(num_str)-1):
        if num_str[i+1] > num_str[i]:
            increasing = True
        elif num_str[i+1] < num_str[i]:
            decreasing = True
        if increasing and decreasing: 
            return True
    return False

count = 0
percentage = 0.0
n = 99
while int(percentage) != 99:    
    n = n + 1
    if is_bouncy(n):
        count = count + 1
    percentage = (count*100.0)/n
print('{0} is the least number for which the proportion of bouncy numbers is exactly 99%.'.format(n))
