class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        
        result = 0
        numbers_list = numbers.split(',')
        numbers_list = list(map(lambda x: int(x), numbers_list))
        for num in numbers_list:
            result += num

        return result