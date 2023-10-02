# def addArr(arr):
#     return sum(arr)

# Function to add two numbers after converting them to integers
def addNum(a, b):
    a = StoN(a)
    b = StoN(b)
    return a + b

def subtractNum(a, b):
    a = StoN(a)
    b = StoN(b)
    return a - b

def multiNum(a, b):
    a = StoN(a)
    b = StoN(b)
    return a * b

def divNum(a, b):
    a = StoN(a)
    b = StoN(b)
    return a / b

def modNum(a, b):
    a = StoN(a)
    b = StoN(b)
    return a % b

# Function to convert a string to an integer
def StoN(n):
    try:
        return int(n)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")
        return 0

