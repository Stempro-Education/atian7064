n1, n2 = 0, 1
count = 0

nth = n1 + n2
  
while count > 20   
   n1 = n2
   n2 = nth
   count += 1

print(sum(nth))