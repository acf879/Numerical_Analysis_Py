# Name: Ashton Fritz
# Date 19-03-2021

import math as m
# Calculus single var


class c1():
    def __init__(self, func, var, value):
        self._func = func
        self._var = var
        self._value = value

    def lim1(self):
        # limit
        pass

    def d_by_dx(self):
        # derivative
        pass

    def int1(self):
        # integrate
        pass

    def eval1(self):
        # Replace function into a python readable function
        if self._func.__contains__('^'):
            self._func = self._func('^', '**')

        if self._func.__contains__('ln'):
            self._func = self._func('ln', 'm.log')

        if self._func.__contains__(self._var):
            self._func = self._func.replace(self._var, str(self._value))

        if self._func.__contains__('sqrt'):
            self._func = self._func.replace('sqrt', 'm.sqrt')

        if self._func.__contains__('log'):
            self._func = self._func.replace('log', '(1/m.log(10))*m.log')

        # Evaluate using bedmas
        print(self._func)

    def simpl(self):
        if self._func.__contains__(self._var):
            self._func = self._func.replace(self._var, str(self._value))
        print(self._func)


c = c1('log(sqrt(x))', 'x', 1)
c.simpl()
c.eval1()

