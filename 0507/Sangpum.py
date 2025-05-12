class Sangpum:
    def __init__(self):
        self.code = None
        self.name = None
        self.count = 0
        self.price = 0
        self.kumack = 0

    def get_code(self):
        return self._code

    def set_code(self, code):
        self._code = code

    code = property(get_code, set_code)


    def input_data(self):
        self.code = input("상품코드를 입력하세요 : ")
        self.name = input("상품명을 입력하세요 : ")
        self.input_cnt_price()

    def input_cnt_price(self):
        try:
            self.count = int(input("수량을 입력하세요 : "))
            self.price = int(input("단가를 입력하세요 : "))
        except ValueError:
            print("\n입력이 올바르지 않습니다.\n")
        else:
            self.proc_kumack()

    def proc_kumack(self):
        self.kumack = self.count * self.price

    def output_data(self):
        print("\t\t\t *** 상품정보 ***    ")
        print("=" * 40)
        print("%5s %3s %3s %4s %4s"
              % ("제품코드", "제품명", "수량", "단가", "판매금액"))
        print("=" * 40)
        print("%5s %5s %3d %8d %8d"
              % (self.code, self.name, self.count, self.price, self.kumack))
        print("=" * 40)




