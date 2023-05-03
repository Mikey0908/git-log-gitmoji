import sys
import re
from emoji import emojize
from colors import color

def main():
    for line in sys.stdin:
        colored_line = line.strip()
        print(emojize(colored_line,language='alias'))

if __name__ == '__main__':
    main()

