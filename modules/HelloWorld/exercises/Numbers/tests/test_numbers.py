import datetime

def test_integers():
    """
    Test that the correct integers have been assigned
    """
    from ..exercise import main
    
    actual_year = datetime.now().year
    assert actual_year == current_year
    assert hours_in_a_day == 24
    assert days_in_a_week == 7

def test_floats():
    """
    Test that the correct floats have been assigned
    """
    from ..exercise import main

    assert pi_to_three_places == 3.142
    assert chance_of_heads_in_coin_flip = 0.5

def test_print_year(capsys):
    """
    Test that the correct floats have been assigned
    """
    from ..exercise import main

    out, err = capsys.readouterr()
    actual_year = datetime.now().year
    assert out.strip() == str(actual_year)