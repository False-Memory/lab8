from fraction import Fraction

def main():
    f1 = Fraction(3,4)
    f2 = Fraction(5,6)
    f3 = Fraction(5,6)

    f4 = f1 + f2        # 19/12
    print(repr(f4)) 
    f4 = f1 - f2        # -1/12
    print(repr(f4))
    print(f2 == f3)     # True
    print(f1 != f2)     # True
    print(f1 < f2)      # True
    print(f2 <= f3)     # True
    print(f2 > f1)      # True
    print(f2 >= f3)     # True
    print(float(f2))    # 0.8333333333333334

if __name__ == "__main__":
    main()
