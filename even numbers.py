#print even number form 1 to 20 using while loop

i=0
while(True):
    i=i+1
    if(i%2!=0):
        continue
    print(i)
    if(i==20):
        break
