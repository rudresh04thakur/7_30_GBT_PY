class UserError(Exception):
    pass
  
class UserError_2(Exception):
    pass
try:
    raise UserError_2
    print(2/4)
    
except(ZeroDivisionError):
    print("Hi this is error")
except(UserError):
    print("Demo User Error")
except(UserError_2):
    print("Demo User Error 3333")
else:
    print("ggg")
finally:
    print("You can not divied any number by zero")


