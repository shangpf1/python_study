'''
python3 递归函数

'''

def f(n):
    if n==1:
        return 1
    return n * f (n-1)
print(f(3))            # 3的阶乘  3*2*1
print(f(5))            # 5的阶乘  5*4*3*2*1