"""Truth-table based digital logic verification demo."""
def half_adder(a: int, b: int):
    return a ^ b, a & b

def verify():
    expected = {(0,0):(0,0),(0,1):(1,0),(1,0):(1,0),(1,1):(0,1)}
    return [(inputs, half_adder(*inputs), result, half_adder(*inputs)==result) for inputs,result in expected.items()]

if __name__ == "__main__":
    for inputs, actual, expected, passed in verify():
        print(inputs, "actual=", actual, "expected=", expected, "PASS" if passed else "FAIL")
