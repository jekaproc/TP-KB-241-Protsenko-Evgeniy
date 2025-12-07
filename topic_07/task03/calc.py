from operations import Calculator

def main():
    calc = Calculator()
    while True:
        if not calc.operations():
            break

if __name__ == "__main__":
    main()