from unittest.mock import Mock

import tmdb_client


def test_get_poster_url_uses_default_size():
    poster_api_path = "some-poster-path"
    expected_default_size = 'w342'
    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
    assert expected_default_size in poster_url


def test_get_movies_list_type_popular():
    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list is not None


def test_get_movies_list(monkeypatch):
    mock_movies_list = ['Movie 1', 'Movie 2']

    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list == mock_movies_list


def test_get_single_movie(monkeypatch):
    mock_movie = {'id': 872585}

    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movie
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movie = tmdb_client.get_single_movie(movie_id=872585)
    assert movie == mock_movie


def test_get_poster_url(monkeypatch):
    mock_poster = 'https://image.tmdb.org/t/p/w342//w780//fm6KqXpk3M2HVveHwCrBSSBaO0V.jpg'

    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_poster
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    poster = tmdb_client.get_poster_url(poster_api_path='/w780//fm6KqXpk3M2HVveHwCrBSSBaO0V.jpg')
    print(poster)
    assert poster == mock_poster


def test_get_single_movie_cast(monkeypatch):
    mock_cast_list = {"cast": ["actor1", "actor2"]}

    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_cast_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    cast_list = tmdb_client.get_single_movie_cast(movie_id=872585)
    assert cast_list == mock_cast_list['cast']
