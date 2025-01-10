from src.fivekyu.the_baker import cakes

def test_check_returns_zero_when_no_ingredients_available():

    insert_recipe = {'flour': 500, 'sugar': 200, 'eggs': 1}
    insert_avail = {}

    output = cakes(insert_recipe, insert_avail)

    assert output == 0
    
def test_check_returns_1_when_ingredients_are_exact():

    insert_recipe = {'flour': 500, 'sugar': 200, 'eggs': 1}
    insert_avail = {'flour': 500, 'sugar': 200, 'eggs': 1}

    output = cakes(insert_recipe, insert_avail)

    assert output == 1

def test_check_returns_correct_response_where_1_ingredient_in_recipe():

    insert_recipe = {'flour': 500}
    insert_avail = {'flour': 500}

    output = cakes(insert_recipe, insert_avail)

    assert output == 1

    insert_recipe = {'flour': 500}
    insert_avail = {'flour': 400}

    output = cakes(insert_recipe, insert_avail)

    assert output == 0

    insert_recipe = {'flour': 500}
    insert_avail = {'flour': 1100}

    output = cakes(insert_recipe, insert_avail)

    assert output == 2

def test_can_return_correct_response_where_multiple_ingredients():

    insert_recipe = {'flour': 500, 'egg': 2, 'milk': 200}
    insert_avail = {'flour': 1600, 'milk': 600, 'egg': 4}

    output = cakes(insert_recipe, insert_avail)

    assert output == 2

def test_check_returns_zero_where_missing_ingredient():

    insert_recipe = {'flour': 500, 'sugar': 200, 'eggs': 1}
    insert_avail = {'flour': 500, 'sugar': 200}

    output = cakes(insert_recipe, insert_avail)

    assert output == 0

def test_checks_no_problem_with_additional_ingredients_not_required():

    insert_recipe = {'flour': 500, 'sugar': 200}
    insert_avail = {'flour': 500, 'sugar': 200, 'ham': 100}

    output = cakes(insert_recipe, insert_avail)

    assert output == 1