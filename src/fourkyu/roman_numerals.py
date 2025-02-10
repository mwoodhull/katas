class RomanNumerals:
    @staticmethod
    def to_roman(val : int) -> str:
        numeral_units = {1: 'I',
                    2: 'II',
                    3: 'III',
                    4: 'IV',
                    5: 'V',
                    6: 'VI',
                    7: 'VII',
                    8: 'VIII',
                    9: 'IX'}
        
        numeral_tens = {10: 'X',
                        100: 'C'
                        1000: 'M'}
        
        numeral_fives = {50: 'L',
                         500: 'D'}
        
        

        return numerals[val]

    @staticmethod
    def from_roman(roman_num : str) -> int:
        nums =      {'I': 1,
                    'II': 2,
                    'III': 3,
                    'IV': 4,
                    'V': 5,
                    'VI': 6,
                    'VII': 7,
                    'VIII': 8,
                    'IX': 9,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000}
        return nums[roman_num]