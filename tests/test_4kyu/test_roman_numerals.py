from src.fourkyu.roman_numerals import RomanNumerals

def test_one_returns_I():

    assert RomanNumerals.to_roman(1) == 'I'

    assert RomanNumerals.from_roman('I') == 1

    assert RomanNumerals.to_roman(7) == 'VII'



def test_tens_returns_correct_response():

    assert RomanNumerals.to_roman(30) == 'XXX'

    assert RomanNumerals.to_roman(21) == 'XXI'

    assert RomanNumerals.to_roman(17) == 'XVII'

    assert RomanNumerals.to_roman(49) == 'XLIX'

    assert RomanNumerals.to_roman(85) == 'LXXXV'

def test_hundreds_returns_correct_response():

    assert RomanNumerals.to_roman(300) == 'CCC'

    assert RomanNumerals.to_roman(211) == 'CCXI'

    assert RomanNumerals.to_roman(917) == 'CMXVII'

    assert RomanNumerals.to_roman(449) == 'CDXLIX'

    assert RomanNumerals.to_roman(585) == 'DLXXXV'

def test_thousands_returns_correct_response():

    assert RomanNumerals.to_roman(1300) == 'MCCC'

    assert RomanNumerals.to_roman(2211) == 'MMCCXI'

    assert RomanNumerals.to_roman(3917) == 'MMMCMXVII'

#     3856

#     6
#     50
#     800
#     3000

#     VI
#     LVI
#     DCCCLVI
#     MMMDCCCLVI
