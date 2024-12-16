def test_comment(capsys):
    """
    Tests a print statement is commented out and has not just been deleted
    """
    from exercise import main
    captured = capsys.readouterr()
    assert captured.out == ""

    with open("main.py", "r") as file:
        content = file.read()
        assert "print(" in content