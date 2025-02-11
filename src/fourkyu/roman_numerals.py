class RomanNumerals:
    @staticmethod
    def to_roman(val: int) -> str:
        numeral_units = {
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
        }

        numeral_tens = {
            10: "X",
            20: "XX",
            30: "XXX",
            40: "XL",
            50: "L",
            60: "LX",
            70: "LXX",
            80: "LXXX",
            90: "XC",
        }

        numeral_hunds = {
            100: "C",
            200: "CC",
            300: "CCC",
            400: "CD",
            500: "D",
            600: "DC",
            700: "DCC",
            800: "DCCC",
            900: "CM",
        }

        numeral_thous = {1000: "M", 2000: "MM", 3000: "MMM"}

        num_lst = list(map(int, str(val)))
        new_lst = []
        multi = 1
        numerals_lst = []

        for i in range(len(num_lst) - 1, -1, -1):
            if num_lst[i] != 0:
                new_lst.insert(0, num_lst[i] * multi)
                multi *= 10
            else:
                multi *= 10

        for num in new_lst:
            if num in numeral_units:
                numerals_lst.append(numeral_units[num])

            elif num in numeral_tens:
                numerals_lst.append(numeral_tens[num])

            elif num in numeral_hunds:
                numerals_lst.append(numeral_hunds[num])

            elif num in numeral_thous:
                numerals_lst.append(numeral_thous[num])

        return "".join(numerals_lst)

    @staticmethod
    def from_roman(roman_num: str) -> int:
        numeral_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        numeral_list = list(roman_num)
        integer_list = []
        total = 0

        for rom_num in numeral_list:
            integer_list.append(numeral_dict[rom_num])

        for i in range(len(integer_list) - 1):
            if integer_list[i] < integer_list[i + 1]:
                total -= integer_list[i]

            else:
                total += integer_list[i]

        total += integer_list[-1]
        return total
