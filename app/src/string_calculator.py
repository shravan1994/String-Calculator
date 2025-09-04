class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        
        numbers_list = numbers.replace('\n', ',').split(',')
        numbers_list = list(map(lambda x: int(x), numbers_list))
        result = sum(numbers_list)
        return result