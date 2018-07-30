#https://techdevguide.withgoogle.com/paths/advanced/working-in-multiple-languages-palindrome-permutation-2/#!

def permute_palindromes(string):
    palindromes = []
    counts = count_letters(string)

    if (can_make_palindrome(string, counts)):
        initial = ""

        for k, v in counts.items():

            if (k != 'odd'):
                initial += (counts[k] // 2) * k

        # convert string to list to simplify swapping
        permute(list(initial), 0, palindromes, counts['odd'])

def swap(string, x, y):
    temp = string[x]
    string[x] = string[y]
    string[y] = temp
    return string

def permute(string_list, start, palindromes, separator=''):
    # reverse string and attach to itself with separator if present
    palindrome = "".join(string_list) + separator + "".join(string_list[::-1])
    palindromes.append(palindrome)

    i = start

    for i in range(start, len(string_list)):
        # prevent duplicates
        if (string_list[start] != string_list[i]):
            # perform swap
            swap(string_list, start, i)
            # move on to next letter with swapped string
            permute(string_list, i+1, palindromes, separator)
            # undo swap
            swap(string_list, start, i)

def count_letters(string):
    counts = {'odd': ''}
    i = 0

    while (i < len(string)):

        if (string[i] in counts):
            counts[string[i]] += 1
        else:
            counts[string[i]] = 1
        i += 1

    return counts

def can_make_palindrome(string, counts):
    # can't create a palindrome if multiple characters have odd repetition
    # count character occurences, break and return early if odd > 1

    odd = 0

    for k, v in counts.items():
        if (k != 'odd' and counts[k] & 1):
            odd += 1
            counts['odd'] = k
            if (odd > 1) break

    # if string length is odd
    if (len(string) & 1):
        return odd == 1
    else:
        return odd == 0

if __name__ == "__main__":
    string = input("String to create permuted palindromes: ")
    palindromes = permute_palindromes(string)
    print(palindromes)
