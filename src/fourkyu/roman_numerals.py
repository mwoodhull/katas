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
                        20: 'XX',
                        30: 'XXX',
                        40: 'XL',
                        50: 'L',
                        60: 'LX',
                        70: 'LXX',
                        80: 'LXXX',
                        90: 'XC'}
        
        numeral_hunds = {100: 'C',
                        200: 'CC',
                        300: 'CCC',
                        400: 'CD',
                        500: 'D',
                        600: 'DC',
                        700: 'DCC',
                        800: 'DCCC',
                        900: 'CM'}
        
        numeral_thous = {1000: 'M',
                        2000: 'MM',
                        3000: 'MMM'}

        num_lst = list(map(int, str(val)))
        multi = 1
        numerals_lst = []

        for i in range(len(num_lst) -1, -1, -1):
            num_lst[i] *= multi
            multi *= 10
            
        for num in num_lst:
            if num in numeral_units:
                numerals_lst.append(numeral_units[num])

            if num in numeral_tens:
                numerals_lst.append(numeral_tens[num])

            if num in numeral_hunds:
                numerals_lst.append(numeral_hunds[num])

            if num in numeral_thous:
                numerals_lst.append(numeral_thous[num])

        return "".join(numerals_lst)

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