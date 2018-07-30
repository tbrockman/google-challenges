# https://techdevguide.withgoogle.com/paths/advanced/compress-decompression/#code-challenge

def decompress(string, start):
    i = start
    num = 0
    token = ""
    while (i < len(string)-1):

        while(string[i].isdigit()):
            num = num * 10 + int(string[i]);
            i += 1

        if (string[i].isalpha()):
            token += string[i]

        else:
            if (string[i] == '['):
                decomp, end = decompress(string, i+1)
                token += (int(num) * decomp)
                i = end

            elif (string[i] == ']'):
                return token, i

        i += 1

    return token, i

if __name__ == "__main__":
    compressed = input("Compressed string: ")
    decompressed, _ = decompress(compressed, 0)
    print(decompressed)
