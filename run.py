import sys

def main(args):
    print("Hello, There!")
    print(f"We are joined by: {args}")


if __name__ == "__main__":
    main(sys.argv[1:])
