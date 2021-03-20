# Name: Ashton Fritz
# Date 19-03-2021

import math as m
# Calculus single var


class C1:
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
        _func = self._func
        _func = _func.replace(self._var, str(self._value))

        while '^' in _func:
            left_ind = _func.index('^') - 1
            right_ind = _func.index('^') + 1
            left_val = int(_func[left_ind])
            right_val = int(_func[right_ind])
            _func = _func[:left_ind] + str(self.power(left_val, right_val)) + _func[right_ind + 1:]

        while 'rt' in _func:
            left_ind = _func.index('rt') - 1
            right_ind = _func.index('rt') + 2
            left_val = int(_func[left_ind])
            right_val = int(_func[right_ind])
            _func = _func[:left_ind] + str(self.root(left_val, right_val)) + _func[right_ind + 1:]

        while '/' in _func:
            left_ind = _func.index('/') - 1
            right_ind = _func.index('/') + 1
            left_val = int(_func[left_ind])
            right_val = int(_func[right_ind])
            _func = _func[:left_ind] + str(self.div(left_val, right_val)) + _func[right_ind + 1:]

        while '*' in _func:
            left_ind = _func.index('*') - 1
            right_ind = _func.index('*') + 1
            left_val = int(_func[left_ind])
            right_val = int(_func[right_ind])
            _func = _func[:left_ind] + str(self.mult(left_val, right_val)) + _func[right_ind+1:]

        while '+' in _func:
            left_ind = _func.index('+') - 1
            right_ind = _func.index('+') + 1
            left_val = int(_func[left_ind])
            right_val = int(_func[right_ind])
            _func = _func[:left_ind] + str(self.add(left_val, right_val)) + _func[right_ind + 1:]

        while '-' in _func:
            left_ind = _func.index('-') - 1
            right_ind = _func.index('-') + 1
            left_val = int(_func[left_ind])
            right_val = int(_func[right_ind])
            _func = _func[:left_ind] + str(self.sub(left_val, right_val)) + _func[right_ind + 1:]

        print(_func)

    def add(self, var1, var2):
        return var1 + var2

    def mult(self, var1, var2):
        return var1 * var2

    def div(self, var1, var2):
        return var1/var2

    def sub(self, var1, var2):
        return self.add(var1, -var2)

    def root(self, var1, var2):
        return var1**1/var2

    def power(self, var1, var2):
        return var1**var2


c = C1('xrt2','x',2)
c.eval1()

