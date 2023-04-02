# Define a function that accepts 2 values and return its sum, subtraction and multiplication.

    def sum(a,b):
        return a + b, a * b, a / b

    print(sum(5,5))


# =============================================================================================


# Define a function that accepts roll number and returns whether the student is present or absent.

def attendance(roll_no):
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    if roll_no in lst:
        print("Student is Present")
    else:
        print("Student is Absent")


roll_no = int(input("Enter Roll No."))
attendance(roll_no)

#
# =============================================================================================


# Define a function in python that accepts 3 values and returns the maximum of three numbers.

def Findmax(a,b,c):
    return max(a,b,c)

 # There are Two Ways to Print The values
print(Findmax(10,5,80))
            # OR
print(f"The Maximum Number is: {Findmax(10,5,80)}")


# =============================================================================================


# Define a function that accepts a number and returns whether the number is even or odd.

def evodd(a):
    if a%2==0:
        print("Even")
    else:
        print("ODD")
    return a

a = int(input("Enter the Number"))
evodd(a)















