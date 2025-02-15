def rom_to_int(a):
  roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
  int_form=0
  for i in range(len(a)): #VIX
    if i+1<len(a) and roman[a[i]]<roman[a[i+1]]:#if 1<3 and V<I
      int_form -= roman[a[i]]# int_form = V
    else:
      int_form += roman[a[i]]
      
  return int_form

a=input("enter a roman numeral: ")
print(rom_to_int(a))
    


 