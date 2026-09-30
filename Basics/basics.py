def if_example(x): 
    if x: 
        return "x is True"
    else: 
        return "x is False"

def while_example(y): 
    count = 0
    while count < y: 
        print(count)
        count += 1

def for_example(z):
    for i in range(z): 
        print(i)

def pass_example():
    pass 

def break_example():
    for i in range(10): 
        if i == 5: 
            break
        print(i)

def continue_example():
    for i in range(10): 
        if i == 5: 
            continue
        print(i)

def try_except_example():
    try: 
        x = 1 / 0
    except ZeroDivisionError: 
        print("Cannot divide by zero")

def match_example(value):
    match value:
        case 1:
            return "Value is one"
        case 2:
            return "Value is two"
        case _:
            return "Value is something else"

if __name__ == "__main__": 
    print(if_example(True))
    while_example(5)
    for_example(3)
    pass_example()
    break_example()
    continue_example()
    try_except_example()
    print(match_example(1))
    print(match_example(3))