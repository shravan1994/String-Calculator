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
        if numbers.startswith('//'):
            newline_index = numbers.find("\n")
            custom_delimiter = numbers[2:newline_index]
            numbers = numbers[newline_index+1:]
            numbers = numbers.replace(custom_delimiter, ',')
            return numbers

        for delimiter in self.SUPPORTED_DELIMITERS:
            numbers = numbers.replace(delimiter, ',')

        return numbers