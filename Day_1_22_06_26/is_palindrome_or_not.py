#Problem statement: Use two pointers to scan a list or string from both ends or 
# at different speeds.
print("Press 1: for palindrome checking")
a = int(input("Enter Your choice here \n"))
if a == 1:
    lst= input("Enter string/numerics to check for palindrome or not:")
    
    def is_palindrome(list):
        left , right = 0, len(list)-1
        while left<right:
            if list[left] != list[right]:
                return False
            left +=1
            right -=1
        return "Yes it is Palindrome"
    print(is_palindrome(lst))    