#!/usr/bin/env python3

# Created by: Nathan Araujo
# Created on: Sept 21 2022
# This program calculates and displays the area and perimeter of a
# circle with radius of 15mm

import math


def main():
    print("For a circle that has a radius of 15 mm")
    print("")
    print("The area of the circle is {:.2f}mm^2".format(math.pi * 15**2))
    print("The circumference of the circle is {:.2f}mm".format(2 * math.pi * 15))


if __name__ == "__main__":
    main()
