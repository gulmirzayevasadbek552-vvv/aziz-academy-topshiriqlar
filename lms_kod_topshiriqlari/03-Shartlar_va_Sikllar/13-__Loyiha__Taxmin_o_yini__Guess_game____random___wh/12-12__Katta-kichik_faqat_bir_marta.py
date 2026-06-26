s=8;n=0
while 1:
 k=int(input());n+=1
 print(("Low"if k<s else"Katta"if k>s else"Correct")if n<2 else("Correct"if k==s else"Wrong"))
 if k==s:break