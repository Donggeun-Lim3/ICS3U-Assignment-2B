#!/usr/bin/env python3

# Created by Donggeun Lim
# Created on June 2020
# This program calculates area of rhombus

def main():
    # this function calculates area of rhombus

    # input
    length = int(input("Enter length of the rhombus (mm): "))
    width = int(input("Enter width of the rhombus (mm): "))

    # process
    area = length*width/2

    # output
    print("")
    print("Area is {}mm²".format(area))


if __name__ == "__main__":
    main()
