numbers=[1,-2,3,-4,5,6,-7,-8,9,10]
num_count=0
for i in numbers:
   if i>0:
      num_count+=1
      print("positive Number",i)
   else:
       print("Negative Number",i)
print(num_count)