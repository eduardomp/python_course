from script import print_hello_world, print_hello_name


def test_hello_world(capsys):
    print_hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello World\n"


def test_hello_name(capsys):
    print_hello_name()
    captured = capsys.readouterr()
    assert captured.out != "Hello YOURNAMEHERE\n"
    assert "Hello " in captured.out
