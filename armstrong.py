num=int(input("Enter number: "))
result=0
temp=num
while temp!=0:
  digit=temp % 10
  result=result+digit**3
  temp=temp//10#15
print(result)
if result==num:
  print(f"{num} is an Armstrong number")
else:
  print(f"{num} is not an Armstrong number")