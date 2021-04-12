# a = "abcde"
# b = "cad"
# # if(a.endswith(b)):
# #     print("True")
# # else:
# #     print("False")
# if b in a[-len(a):]:
#     print("True")
# else:
#     print("False")
# a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# dict = {"NORTH":"SOUTH","EAST":"WEST","WEST":"EAST","SOUTH":"NORTH"}
# res = []
# for i in a:
#     if res and dict[i] == res[-1]:
#         res.pop()
#         print(res)
#     else:
#         res.append(i)
#         print(res)
# print(res)
# def Fibonacci(n):
#     a = 0
#     b = 1
#     if n<=0:
#         print("Incorrect input")
#     elif n == 1:
#         return b
#     else:
#         for i in range(2,n):
#             c = a+b
#             a = b
#             b = c
#         return b
# print(Fibonacci(20))

# def productFib(prod):
#     current_value = 0
#     x = 0
#     fib1 = 0
#     fib2 = 1

#     while current_value < prod:
#         x += 1
#         fib1 = fib(x)
#         fib2 = fib(x+1)
#         current_value = fib1 * fib2
#     if current_value == prod:
#         print([fib1, fib2, True])
#     print ([fib1, fib2, False])

# def fib(n):
#     a,b = 1,1

#     for i in range(n-1):
#         a,b = b,a+b
#     return a
# productFib(0)

import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title = "**Please Drink Water Now!!",
            message ="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            app_icon = "path to your .ico file",
            timeout = 12
        )

        # time.sleep(6)
        time.sleep(60*60)