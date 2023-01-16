def reverseBits(self, n):
    bin_n = bin(n)[2:].zfill(32)
    reversed_bin = bin_n[::-1]
    return int(reversed_bin, 2)

if __name__ =="__main__":
    print(reverseBits('10100101000001111010011100'))