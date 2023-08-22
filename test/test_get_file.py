from scr.get_file import file_open


def test_file_open():
    data = file_open()
    assert isinstance(data, list)


