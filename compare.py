##fib numbers
n1 = 0
n2 = 1
count = 0
number = [0,1]


while count < 18:
   nth = n1 + n2
   n1 = n2
   n2 = nth
   number.append(nth)
   count += 1

numberSum = sum(number)
##tri numbers
count = 2
trinumber = [1]
x = 1

while count < 21:
   x = x + count
   trinumber.append(x) 
   count += 1

trinumberSum = sum(trinumber)



##compare
print("List of the first 20 fibonacci numbers:", number)
print("List of the first 20 triangular numbers:", trinumber)
print("The sum of the first 20 fibonacci numbers is", numberSum)
print("The sum of the first 20 triangular numbers is", trinumberSum)
print("The difference between the fibonacci and triangular numbers is", numberSum - trinumberSum)
