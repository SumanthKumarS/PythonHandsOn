t1 = input('Enter the word : \n').lower() 
t1 = t1.replace(" ", "")
if( t1==t1[::-1]):
   print('Yes, the string is a palindrome !')
else:
   print('No, the string is not a palindrome !')