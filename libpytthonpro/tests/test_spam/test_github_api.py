from unittest.mock import Mock

import pytest
from pytest_mock import mocker

from libpytthonpro import github_api

@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars1.githubusercontent.com/u/69489292?v=4'
    resp_mock.json.return_value = {
        'login': 'rlemos37', 'id': 69489292,
        'avatar_url': url
    }
    get_mock = mocker.patch('libpytthonpro.github_api.requests.get')
    github_api.requests.get = Mock(return_value=resp_mock)
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('rlemos37')
    assert avatar_url == url



def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('lemos38')
    assert 'https://avatars3.githubusercontent.com/u/70118210?v=4' == url
