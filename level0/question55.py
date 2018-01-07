try:
    x = 5/0
except ZeroDivisionError as e:
    print('3')
    print(e)
except RuntimeError as e:
    print("2")
    print(2)
except AttributeError as e:
    print("1")
    print(e)
except Exception as e:
    print(type(e))
finally:
    print('I will must be printed ')
    