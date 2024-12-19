def test_hello_world(capsys):
    """
    Test main prints "Hello World!"
    """
    from ..exercise import main

    out, err = capsys.readouterr()
    assert "Hello World!" in out.strip()


