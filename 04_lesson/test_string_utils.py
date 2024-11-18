from string_utils import StringUtils
import pytest

@pytest.mark.parametrize(
    'input_string, expected_output',
    [('think Different',  'Think different'),
     ('365 days', '365 days'),
     ('CAPITAL', 'Capital')],
      )
def test_positive_capitalize(input_string,expected_output):
    res = StringUtils()
    assert res.capitalize(input_string) == expected_output

@pytest.mark.parametrize(
    'input_string, expected_output',
    [('      repository', 'repository'),
     ('     365 days', '365 days'),
     ('   Capital', 'Capital')],
      )
def test_positive_trim(input_string, expected_output):
    res = StringUtils()
    assert res.trim(input_string) == expected_output

@pytest.mark.parametrize(
    'input_string, expected_output',
    [('B,c,d', ['B', 'c', 'd']),
    #  ('12~23~35',sep == '~', ['12', '23', '35']),
     ('', [])],
      )
def test_positive_to_list(input_string, expected_output):
    res = StringUtils()
    assert res.to_list(input_string) == expected_output

@pytest.mark.parametrize(
    'input_string, symbol,expected_output',
    [('repository', 'r', True),
     ('365 days', '6', True),
     ('long-term', '-', True)],
      )
def test_positive_contains(input_string, symbol, expected_output):
    res = StringUtils()
    assert res.contains(input_string,symbol) == True

@pytest.mark.parametrize(
    'input_string, symbol, expected_output',
    [('repository', 'r', 'epositoy')],
    )
def test_positive_delete_symbol(input_string, symbol, expected_output):
    res = StringUtils().delete_symbol(input_string, symbol)
    assert res == expected_output

@pytest.mark.parametrize(
    'input_string, symbol, expected_output',
    [('repository', 'r', True),
     ('365 days', '3', True),
     ('longterm', 'l', True)],
      )
def test_positive_starts_with(input_string, symbol, expected_output):
    res = StringUtils()
    assert res.starts_with(input_string, symbol) == True

@pytest.mark.parametrize(
    'input_string, symbol, expected_output',
    [('repository', 'y', True),
     ('NATO', 'O', True),
     ('switch to 15', '5', True)],
      )
def test_positive_end_with(input_string, symbol,expected_output):
    res = StringUtils()
    assert res.end_with(input_string, symbol) == True


@pytest.mark.parametrize(
    'input_string, expected_output',
    [('', True),
     (' ', True),
     ('            ', True)],
      )
def test_positive_is_empty(input_string,expected_output):
    res = StringUtils()
    assert res.is_empty(input_string) == expected_output

@pytest.mark.parametrize(
    'list, joiner, expected_output',
    [([1, 2, 3, 4], ',', '1,2,3,4'),
     (['stick', 'in', 'the', 'mud' ], '-', 'stick-in-the-mud'),
     (['long', 'life'], ':', 'long:life')],
      )
def test_positive_list_to_string(list, joiner, expected_output):
    res = StringUtils().list_to_string(list, joiner)
    assert res == expected_output



@pytest.mark.parametrize(
    'input_string, expected_output',
    [(None,  AttributeError),],
      )
def test_negative_capitalize(input_string,expected_output):
    res = StringUtils()
    assert res.capitalize(input_string) == expected_output

@pytest.mark.parametrize(
    'input_string, expected_output',
    [(None, AttributeError),
     ('', ''),],
      )
def test_negative_trim(input_string, expected_output):
    res = StringUtils()
    assert res.trim(input_string) == expected_output

@pytest.mark.parametrize(
    'input_string, expected_output',
    [(None, AttributeError),
    ((12, 33, 56), AttributeError)],
      )
def test_negative_to_list(input_string, expected_output):
    res = StringUtils()
    assert res.to_list(input_string) == expected_output

@pytest.mark.parametrize(
    'input_string, symbol,expected_output',
    [(None, 'r', AttributeError),
     ((17, 66, 77), '-', AssertionError)],
      )
def test_negative_contains(input_string, symbol, expected_output):
    res = StringUtils()
    assert res.contains(input_string,symbol) == True

@pytest.mark.parametrize(
    'input_string, symbol, expected_output',
    [(None, 'r', AttributeError),
     ('', 'o', AssertionError)],
    )
def test_negative_delete_symbol(input_string, symbol, expected_output):
    res = StringUtils().delete_symbol(input_string, symbol)
    assert res == expected_output

@pytest.mark.parametrize(
    'input_string, symbol, expected_output',
    [('', 'r', AssertionError),
     (None, '3', AttributeError),
     ((33, 44,55), '33', AttributeError)],
      )
def test_negative_starts_with(input_string, symbol, expected_output):
    res = StringUtils()
    assert res.starts_with(input_string, symbol) == True


@pytest.mark.parametrize(
    'input_string, symbol, expected_output',
    [('', 'y', AssertionError),
     (None, 'O', AttributeError),
     ((45, 56,67), '7', AttributeError)],
      )
def test_negative_end_with(input_string, symbol,expected_output):
    res = StringUtils()
    assert res.end_with(input_string, symbol) == True

@pytest.mark.parametrize(
    'input_string, expected_output',
    [(None, AttributeError),
     (23456, AttributeError),],
      )
def test_negative_is_empty(input_string,expected_output):
    res = StringUtils()
    assert res.is_empty(input_string) == expected_output

@pytest.mark.parametrize(
    'list, joiner, expected_output',
    [(None, ',', AttributeError),
     ({1:'One', 2:'Two'}, '-', AttributeError)],
      )
def test_negative_list_to_string(list, joiner, expected_output):
    res = StringUtils.list_to_string(list, joiner)
    assert res == expected_output