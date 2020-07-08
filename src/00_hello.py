# Print "Hello, world!" to your terminal
print("Hello, world! how sad it is to be you right now")


def stupid_addition(a, b):
    if type(a) == str and type(b) == str:
        print(int(a + b))
        # z = int(a + b)
        # print(z)
        # print(int(a), int(b))
    elif type(a) == int and type(b) == int:
        print(str(a + b))
    else:
        print("none")


stupid_addition("7", "8")  # expected 78
stupid_addition(7, 8)  # expectred 15
stupid_addition(7, "8")  # expected none
