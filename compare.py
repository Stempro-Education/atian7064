def printFibList():
   print ("List of the first 20 fibonacci numbers:", number)
def printTriList():
   print("List of the first 20 triangular numbers:", trinumber)
def printSumFib():
   print("The sum of the first 20 fibonacci numbers is", numberSum)
def printSumTri():
   print("The sum of the first 20 triangular numbers is", trinumberSum)
def printDiff():
   print("The difference between the fibonacci and triangular numbers is", numberSum - trinumberSum)





def fibonacci():
   count = 0
   n1 = 0
   n2 = 1
   while count < 18:
      nth = n1 + n2
      n1 = n2
      n2 = nth
      number.append(nth)
      count += 1
   
   return sum(number)


def triangular():
   count = 2
   x = 1
   while count < 21:
      x = x + count
      trinumber.append(x) 
      count += 1
  
   return sum(trinumber)



##compare
number = [0,1]
trinumber = [1]
trinumberSum = triangular()
numberSum = fibonacci()
printFibList()
printTriList()
printSumFib()
printSumTri()
printDiff()