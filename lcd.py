#!/usr/bin/env python

import sys

"""
The LCD display table of digits 0~9.
We can alse include float numbers and negative numbers by add "-" and "." in
the  table.
"""
LCD_DISPLAY_TABLE = (
        "-|| ||-",
        "  |  | ",
        "- |-| -",
        "- |- |-",
        " ||- | ",
        "-| - |-",
        "-| -||-",
        "- |  | ",
        "-||-||-",
        "-||- |-"
        )


def error(exitcode, fmt, *args):
    print >>sys.stderr, fmt %args
    exit(exitcode)

def read_lines(filename):
    with open(filename) as f:
        for line in f:
            tmp = line.split()
            #yield int s, str n
            yield (int(tmp[0]), tmp[1])

def print_lcd_digit_line(digit_lcd, s, line):
    """
    digit_lcd is the lcd display of the digit
    s is the number of separators
    line is the line we want to print
    """

    if line in [0, s+1, 2*s+2]:
        offset = int(line/(s+1))*3
        return " %s " %(digit_lcd[offset]*s)
    else:
        offset = int(line/(s+1))*3 + 1
        return "%s%s%s" %(digit_lcd[offset], " "*s, digit_lcd[offset + 1])

def print_lcd(s, n):
    """
    n is the number we want to print, attention that it is a string.
    s is the number of separators
    """

    if s <= 0:
        error(2, "The number of separators must greater than 0")
    for line in range(2*s + 3):
        line_buffer = []
        for c in n:
            line_buffer.append(print_lcd_digit_line(LCD_DISPLAY_TABLE[int(c)], s, line))
        print("".join(line_buffer))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        error(1, "usage: %s inputfile", sys.argv[0])
    first = True
    for s, n in read_lines(sys.argv[1]):
        if not first:  print("")
        print_lcd(s, n)
        first = False

