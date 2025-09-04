class StringCalculator:
    SUPPORTED_DELIMITERS = ['\n']

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        
        numbers = self._normalize_delimiters(numbers)
        
        numbers_list = numbers.strip().split(',')
        numbers_list = list(map(lambda x: int(x), numbers_list))
        negative_nums = list(filter(lambda x: x < 0, numbers_list))
        if negative_nums:
            raise ValueError(
                f'negative numbers not allowed {','.join(map(str, negative_nums))}')

        result = sum(numbers_list)
        return result
    
    def _normalize_delimiters(self, numbers: str) -> str:
        if numbers.startswith('//'):
            newline_index = numbers.find("\n")
            custom_delimiter = numbers[2:newline_index]
            numbers = numbers[newline_index+1:]
            numbers = numbers.replace(custom_delimiter, ',')
            return numbers
        else:
            # in case of specified custom delimeter do not use,
            # existing set of delimeters like ',' and '\n'
            for delimiter in self.SUPPORTED_DELIMITERS:
                numbers = numbers.replace(delimiter, ',')

        return numbers