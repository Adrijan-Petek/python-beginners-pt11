"""Part 11: using a small package"""
from mypkg import utils

def main():
    print("2 + 3 =", utils.add(2,3))
    print("4 * 5 =", utils.multiply(4,5))

if __name__ == '__main__':
    main()
