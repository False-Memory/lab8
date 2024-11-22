from complexnumber import ComplexNumber

def main():
    # Example usage
    c1 = ComplexNumber(1, 2)
    print(c1) # output: 1 + 2i 
  
    c2 = ComplexNumber(3, 4)
    print(c2) # output: 3 + 4i

    c3 = c1 + c2
    print(c3) #4 + 6i

    c4 = c2 - c1
    print(c4) #2 + 3i

if __name__ == "__main__":
    main()