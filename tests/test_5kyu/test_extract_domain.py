from src.fivekyu.extract_domain import domain_name

def test_empty_string_returns_empty_string():

    insert = ''

    output = domain_name(insert)

    assert output == ''

def test_url_returns_domain_name():

    insert = 'http://github.com'

    output = domain_name(insert)

    assert output == 'github'