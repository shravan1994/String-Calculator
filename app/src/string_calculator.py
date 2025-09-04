class StringCalculator:
    SUPPORTED_DELIMITERS = ['\n']

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        
        numbers = self._normalize_delimiters(numbers)
        
        numbers_list = numbers.split(',')
        numbers_list = list(map(lambda x: int(x), numbers_list))

        result = sum(numbers_list)
        return result
    
    def _normalize_delimiters(self, numbers: str) -> str:
        for delimiter in self.SUPPORTED_DELIMITERS:
            numbers = numbers.replace(delimiter, ',')

        return numbers