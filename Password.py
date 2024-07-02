#Write A Program in Python To Check Strength Of The Password Given As An Input
#Password Creation  Guidelines

#Password Should Be Of 8 Characters
#Password Should Contain One Special Character
#Password Should Contain One Lowercase Character and One Uppercase Character
#Password Should Contain One Number

def Checker(a):

    if len(a) == 8 or len(a) > 8:
       print("Enough Characters")
    else:
       print("Not Enough Characters")

   #Guidelines For a Strong Password
    pro = any(x.isupper() for x in a)
    noob = any(x.islower() for x in a)
    Expert = any(x.isdigit() for x in a)
    spec = any(x in '!@#$%^&*()-_=+{}[]\\|;:\'",.<>?/~`' for x in a) 

    if pro and noob and Expert and spec:
      print("Strong Password")
    elif pro and noob and Expert:
      print("Weak Password")
    elif pro and noob:
       print("Weak Password")
    elif pro and Expert:
       print("Weak Password")
    elif noob and Expert:
       print("Weak Password")
    elif Expert and spec:
       print("Weak Password")
    elif noob and spec:
       print("Weak Password")
    elif pro and spec:
      print("Weak Password")
    elif pro:
      print("Weak Password")
    elif Expert:
       print("Weak Password")
    elif spec:
       print("Weak Password")
    else:
       print("Weakest")
    
a = input("Enter Your Password\n")
boss = Checker(a)
 
