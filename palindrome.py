import sys

def main(text):
    x = sys.argv[1]    
    y = x.replace(" ", "")
    z = ''.join(filter(str.isalnum, y.lower()))
   
    
    if  z == (z[::-1]):
        return("It's a palindrome!")
    
    else:
        return("It's not a palindrome!")
            
print(main(sys.argv[1]))