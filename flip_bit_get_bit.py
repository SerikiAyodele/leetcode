# Implement a data structure that supports the operations flipBits(ith bit, # of bits) and getBit(ith bit), billions of possible bits, <= O(n log n) preferably
                                                                 
class BitArray:
    def __init__(self, size):
        self.bit_array = [0] * size

    def flipBits(self, start, length):
        for i in range(start, start + length):
            self.bit_array[i]= 1-self.bit_array[i]

    def getBit(self, index):
        return self.bit_array[index]


my_bit_array = BitArray(7)

print(my_bit_array.bit_array)  

my_bit_array.flipBits(2, 4)
print(my_bit_array.bit_array)

bit_value = my_bit_array.getBit(4)
print(bit_value) 