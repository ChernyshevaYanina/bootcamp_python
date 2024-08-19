import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('num_lines', type=int, help='Количество строк')
    args = parser.parse_args()

    data = sys.stdin.read()

    for line in data.splitlines()[:args.num_lines]:
        if len(line) == 32 and line.startswith('00000') and line[5]!= '0':
            print(line)

if __name__ == '__main__':
    main()
    