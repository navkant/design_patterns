class Demo:
    def __init__(self, x):
        print("inside Demo.__init__")
        self.x = x

    def __call__(self, *args, **kwargs):
        print("inside Demo.__call__")
        print("executing inner function")
        arg_1 = args[0]
        arg_2 = args[1]
        self.x(arg_1, arg_2, key_word_arg=kwargs)
        print("inner function executed")


def funcx(arg_1, arg_2, key_word_arg):
    print("inside funcx()")
    print(f"this [{arg_1}] and {[arg_2]} passed as argument")
    print(f"key word argument {key_word_arg}")


y = Demo(funcx)
y("99", 99, keyword="Navkant")


funcx("99", 99, keyword="Navkant")
