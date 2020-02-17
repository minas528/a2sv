class ProductOfNumbers:

    def __init__(self):
        self.lst = [1]

    def add(self, num: int) -> None:
        if num:
            if self.lst[-1] == 0:
                self.lst.append(num)
            else:
                self.lst.append(self.lst[-1]*num)
        else:
            self.lst.append(0)

    def getProduct(self, k: int) -> int:
        if 0 in self.lst[len(self.lst)-k:]:
            return 0
        else:
            if self.lst[len(self.lst)-k-1] == 0:
                return self.lst[-1]
            return self.lst[-1]//self.lst[len(self.lst)-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

if __name__ == '__main__':
    product_of_numbers = ProductOfNumbers()
    product_of_numbers.add(3)
    product_of_numbers.add(2)
    product_of_numbers.add(8)
    product_of_numbers.getProduct(2)