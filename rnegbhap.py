
new = int(input("enter a integer number\n"))
odd = 0
even = 0
for num in range(0,new):
    if num%2 != 0:
        print("the odd numbers are ",num)
        odd += (num*num)
    if num%2 == 0:
        print("the even numbers are",num)
        even += (num*num)
print(odd , even)








