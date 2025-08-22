# loops is used for repeation
# while and for loop



# x=1
# while x<=10:
#     print(x)
#     x+=1



# x=1
# while x<=10:
#     if x==5:
#         break
#     print(x)
#     x+=1



# x=0
# while x<10:
#      x+=1
#      if x==5:
#         continue
#      print(x)


#task
# print 1 to 50 number
# in this 25 to 35 must be skip

x=1
while x<=50: #loop runs from 1 to 50
   if 25<=x and x<=35: #it check num is between 25 and 35
      x+=1              #increment
      continue        #skip printing and go back to the while loop
   print(x)   #if condition is true last 2 line will not execute 
   x+=1        


