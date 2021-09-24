#Astrologer's stars
#for true           #for false
# *                 # ****
# **                # ***
# ***               # **
# ****              # *

choice=bool(int(input("Enter 1 for True and 0 for False \n")))
num=int(input("enter number of rows: "))
if choice==True:
    for i in range(1,num+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()

elif choice==False:
    for i in range(num, 0, -1):
        for j in range(1,i+1):
            print("*", end=" ")
        print()
