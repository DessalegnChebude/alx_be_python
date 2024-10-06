import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator")
        sys.exit(1)
    else:
        try:
            numerator = int(sys.argv[1])
            denominator = int(sys.argv[2])
            result = safe_divide(numerator, denominator)
            print(result)
        except ValueError:
            print("Error: Please provide valid integer numbers as arguments.")
if __name__ == "__main__":
    main()