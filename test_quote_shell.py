from project import Word, request_data, filter_data, quote_filter
import pytest
import responses

@pytest.mark.parametrize("x", [
    ("asdj"),
    ("ASDJ"),
    ("plki"),
    (1234),
    (987),
    (1),
    ("b"),
    ("r"),
    (""),
    (" "),
    ("."),
    ("!"),
    ("?"),
    ("ASDJ"),
    ("plki"),
])


def test_raises_ValueError(x):
    with pytest.raises(ValueError):
        word = Word(x)

@pytest.mark.parametrize("letters", [
    ("man"),
    ("happy"),
    ("sad"),
    ("top"),
])

def test_init_correct(letters):
    try:
        assert Word(letters)._user_word == letters
    except ValueError:
        pytest.fail("ValueError raised unexpectedly")

@pytest.fixture
def mock_word():
    return "pretend_word"

@pytest.fixture
def mock_data(mock_word):
#dynamically generate mock data based on the value of mock_word
    return [
    {'q': 'quote1',
    'a': 'author1'},
    {'q': f'quote2 {mock_word}',
    'a': 'author2'},
    {'q': f'quote3 {mock_word}',
    'a': 'author3'},
    ]

@pytest.fixture
def mock_list(mock_word):
    return [
        (f"quote2 {mock_word}","author2"),
        (f"quote3 {mock_word}","author3"),
    ]

@pytest.fixture
def mock_saying(mock_word):
    return (f"quote2 {mock_word}","author2")

@pytest.fixture
def setup_responses():
    responses.start()
    yield
    responses.stop()
    responses.reset()

def test_success_request_data(setup_responses, mock_data):
    responses.add(
        responses.GET,
        "https://zenquotes.io/api/quotes/",
        json=mock_data,
        status=200,
    )

    assert request_data() == mock_data

def test_fail_request_data(setup_responses, mock_data):
    responses.add(
        responses.GET,
        "https://zenquotes.io/api/quotes/",
        json=mock_data,
        status=404,
    )

    with pytest.raises(SystemExit):
        request_data()

def test_success_filter_data(mock_word, mock_data, mock_list):
   assert filter_data(mock_data, mock_word) == mock_list

def test_filter_data_raises_sysexit(mock_data, mock_word):

    for i in mock_data:
        if mock_word in i["q"]:
            del i["q"]

    with pytest.raises(SystemExit):
        filter_data(mock_data, mock_word)

def test_success_quote_filter(mock_list, mock_word, mock_saying):
    assert quote_filter(mock_list, mock_word) == mock_saying

def test_quote_filter_non_matching(mock_list):
    broken_mock_word = "non-existant"
    assert quote_filter(mock_list, broken_mock_word) == "Try again; no quote found matching the exact Word/Mood"

def test_quote_filter_raises_sysexit(mock_list, mock_word):
    empty_tuple = ()
    mock_list.insert(0, empty_tuple)
    with pytest.raises(SystemExit):
        quote_filter(mock_list, mock_word)
