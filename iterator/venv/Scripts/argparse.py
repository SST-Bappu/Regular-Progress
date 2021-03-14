import argparse

if __name__ == "__main__":
    #parser = argparse.ArgumentParser
    parser = argparse.ArgumentParser(description='Process some integers.' )
    parser.add_argument("--number1", help = "First Number")
    parser.add_argument("--number2",help = "Second Number")
    parser.add_argument("--Operation",help ="Operation")
    args = parser.parse_args()

    print(args.number1)
    print(args.number2)
    print(args.operation)