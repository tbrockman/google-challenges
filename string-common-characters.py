# Write a function f(a, b) which takes two character string arguments and returns
# a string containing only the characters found in both strings in the order of a.
# Write a version which is order N-squared and one which is order N.

def f_n2(a,b):

    string = ""

    for letter_a in a:
        for letter_b in b:
            if letter_a == letter_b and letter_a not in string:
                string += letter_a
                break

    return string


def f_n(a, b):

    string = ""
    dict_b = {}

    for letter in b:
        if not letter in dict_b:
            dict_b[letter] = 1

    for letter in a:

        if letter in dict_b:
            string += letter
            dict_b.pop(letter)

    return string

if __name__ == "__main__":
    a = input("First string: ")
    b = input("Second string: ")
    print(f_n(a, b))
    print(f_n2(a, b))
