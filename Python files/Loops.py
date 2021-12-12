#while loop= a statement that executes it's block of code, as long its condition
#            remains true
# can also be done by / name= none
# while not name:
#none = ''
#name = none
#while len(name) == 0:
# name = input('Enter your name:')
#print('Hello ' + name )

#for loop = a statement executes it's block of code, for a limited amount of time
#         while loop = unlimited
#         for loop = limited

#for i in range(10+1):
#    print(i)
#for i in range(50,100+1,2):
#    print(i)
#for i in 'Shaaran':
#    print(i)
#import time

#for blue in range(10,0,-1):
#    print(blue)
#    time.sleep(1)
#print('Happy birthday')

#nested loops= the 'inner loop' will finish all of its iterations before finishing
#             one iteration of the 'outer loop'
#import time
#rows = int(input('Enter no. of rows: '))
#columns = int(input('Enter no. of columns: '))
#symbol = input('Enter a symbol: ')
#for i in range(4):
#   time.sleep(1)
#   for j in range(5):
#     time.sleep(1)
#     print(symbol,end='')
#   print()

#Loop control statements= changes a loop execution from its normal sequence
#break = used to terminate the loop entirely
#continue = skips to the next iteration of the loop
#pass = does nothing, acts as a placeholder

#while True:
#    name = input('Enter your name:')
#    if name != '':
#     break

#phone_number = '999-888-1234'
#for i in phone_number:
#    if i == '-':
#        continue
#    print(i, end='')

#for i in range(1,21):
#    if i == 13:
#        continue or pass
#    else:
#        print(i)
