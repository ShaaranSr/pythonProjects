#logical operators(and,or,not)= used to check two or more conditions are true
temp = int(input('What is the temperature outside?:'))

if not(temp >= 0 and temp <= 30):
    print('the temp is bad today')
    print('stay inside')
elif not(temp < 0 or temp > 30):
    print('the temp is good today')
    print('go outside')