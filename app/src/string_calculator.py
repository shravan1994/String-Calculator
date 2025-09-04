from typing import List

class StringCalculator:
    SUPPORTED_DELIMITERS = ['\n']
    MAX_ALLOWED_NUMBER = 1000

    def add(self, numbers: str) -> int:
        if not numbers.strip():
            return 0
        
        numbers = self._normalize_delimiters(numbers)
        if not numbers:
            return 0

        numbers_list = self._parse_numbers(numbers)
        return sum(numbers_list)
        
    def _parse_numbers(self, numbers: str) -> List[int]:
        numbers_list = numbers.strip().split(',')
        numbers_list = [int(x) for x in numbers_list if x]

        negative_nums = [x for x in numbers_list if x < 0]
        if negative_nums:
            raise ValueError(
                f"negative numbers not allowed {','.join(map(str, negative_nums))}")
        
        numbers_list = [x for x in numbers_list if x <= self.MAX_ALLOWED_NUMBER]

        return numbers_list
    
    def _normalize_delimiters(self, numbers: str) -> str:
        if numbers.startswith('//'):
            newline_index = numbers.find("\n")
            custom_delimiter = numbers[2:newline_index]
            numbers = numbers[newline_index+1:]
            numbers = numbers.replace(custom_delimiter, ',')
            return numbers
        else:
            for delimiter in self.SUPPORTED_DELIMITERS:
                numbers = numbers.replace(delimiter, ',')

        return numbers