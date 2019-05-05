try:
    print(2/None)
except(ZeroDivisionError):
    print("Hi this is error")
except:
    print("demo")
finally:
    print("You can not divied any number by zero")