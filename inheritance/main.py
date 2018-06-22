class A:
    def method_print(self):
        print("method of A called")

    def method_return(self):
        text = ["method of A called"]
        return(text)


class B(A):
    def method_print(self):
        print("method of B called")
        super().method_print()

    def method_return(self):
        text = ["method of B called"]
        text += super().method_return()
        return(text)


class C(A):
    def method_print(self):
        print("method of C called")
        super().method_print()

    def method_return(self):
        text = ["method of C called"]
        text += super().method_return()
        return(text)


class D(B, C):
    def method_print(self):
        print("method of D called")
        super().method_print()

    def method_return(self):
        text = ["method of D called"]
        text += super().method_return()
        return(text)


if __name__ == '__main__':
    x = D()
    x.method_print()
    print(f'MRO: {D.mro()}')
