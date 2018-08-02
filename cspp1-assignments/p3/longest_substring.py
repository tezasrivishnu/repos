'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in
which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest
that you move on to a different part of the course.
If you have time, come back to this problem after you've had a
break and cleared your head.'''

def main():
    """program that prints the longest substring of s
    in which the letters occur in alphabetical order"""
    s_str = input()
    c_s = 0
    mc_s = 0
    r_c = 0
    for char in range(len(s_str)-1):
        if s_str[char] <= s_str[char+1]:
            c_s += 1
            if c_s > mc_s:
                mc_s = c_s
                r_c = char + 1
    else:
        c_s = 0
    sp_s = r_c - mc_s
    print(s_str[sp_s:r_c+1])

if __name__ == "__main__":
    main()
