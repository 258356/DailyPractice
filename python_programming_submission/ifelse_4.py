input(real,float,string,complex,zero)

def check_float(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False
    
def check_int(potential_float):
    try:
        int(potential_float)
        return True
    except ValueError:
        return False

value=input("enter a number")

if(check_int(value)):
    if(int(value)==0):
        print("zero")
    else:
        print("Integer")

else:
    if(check_float(value)):
        print("Float")

    else:
        print("Complex")
