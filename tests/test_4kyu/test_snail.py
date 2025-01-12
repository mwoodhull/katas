from src.fourkyu.snail import snail


def test_single_nested_list_returns_unnested_list():

    insert = [[1]]

    output = snail(insert)

    assert output == [1]


def test_2_by_2_nested_lists_can_return_correct_response():

    insert = [[1, 2], [3, 4]]

    output = snail(insert)

    assert output == [1, 2, 4, 3]


def test_3_by_3_nested_lists_can_return_correct_response():

    insert = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    output = snail(insert)

    assert output == [1, 2, 3, 6, 9, 8, 7, 4, 5]


def test_bigger_than_3_by_3_list_can_return_correct_response():

    insert = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    output = snail(insert)

    assert output == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

    insert = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]

    output = snail(insert)

    assert output == [
        1,
        2,
        3,
        4,
        5,
        10,
        15,
        20,
        25,
        24,
        23,
        22,
        21,
        16,
        11,
        6,
        7,
        8,
        9,
        14,
        19,
        18,
        17,
        12,
        13,
    ]
