def product( x , y ):
    if y != 0:
        return (x + product(x, y - 1))
    else:
        return 0
 
x = 7
y = 2
print( product(x, y))

def ispalindome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return ispalindome(s[1:-1])
        else:
            return False

a=str(input("Enter:"))
if(ispalindome(a)==True):
    print("Palindrome")
else:
    print("Palindrome")