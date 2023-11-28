"""The factorial of a non-negative integer N, denoted by N! ,is the product of all positive integers less than or equal to N.5!=5x4x3x2x1=120"
"""
def factorial():
    fact=1
    input_num=int(input("Enter a non-negative number:"))
    for num in range(input_num,0,-1):
        fact=fact*num
    print(f"Factorial of {num} is {fact}")

if __name__=="__main__":
    factorial()