# https://techdevguide.withgoogle.com/paths/advanced/compress-decompression/#code-challenge

def decompress(compressed, start):
    i = start
    num = 0
    decompressed = ""
    while (i < len(compressed)-1):

        while(compressed[i].isdigit()):
            num = num * 10 + int(compressed[i]);
            i += 1

        if (compressed[i].isalpha()):
            decompressed += compressed[i]

        else:
            if (compressed[i] == '['):
                decomp, end = decompress(compressed, i+1)
                decompressed += (int(num) * decomp)
                i = end

            elif (compressed[i] == ']'):
                return decompressed, i

        i += 1

    return decompressed, i

if __name__ == "__main__":
    compressed = input("Compressed compressed: ")
    decompressed, _ = decompress(compressed, 0)
    print(decompressed)
