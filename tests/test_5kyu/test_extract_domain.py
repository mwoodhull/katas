from src.fivekyu.extract_domain import domain_name

def test_url_returns_domain_name_with_dotcom_at_end():

    insert = 'http://github.com'

    output = domain_name(insert)

    assert output == 'github'

def test_url_returns_domain_for_other_endings():

    insert = 'http://github.co.uk'

    output = domain_name(insert)

    assert output == 'github'

    insert = 'http://github.gov.uk'

    output = domain_name(insert)

    assert output == 'github'

    insert = 'http://github.org'

    output = domain_name(insert)

    assert output == 'github'

def test_url_returns_domain_when_there_are_other_characters():

    insert = 'http://git-hub1.co.uk'

    output = domain_name(insert)

    assert output == 'git-hub1'

def test_url_returns_domain_where_starts_wwwdot():

    insert = 'http://www.github.com'

    output = domain_name(insert)

    assert output == 'github'

def test_url_where_starts_with_domain():

    insert = 'github.com'

    output = domain_name(insert)

    assert output == 'github'