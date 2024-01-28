import pytest

from flaskr.view.config import config_int


@pytest.mark.unit
def test_config_int(mocker):
    mocker.patch('flaskr.view.config.Hardware.get_config_int',
                 return_value=42)
    config = config_int()

    assert '42' == config


@pytest.mark.api
def test_config_int_api(mocker, client):
    mocker.patch('flaskr.view.config.Hardware.get_config_int',
                 return_value=42)
    response = client.get('/config/int')

    assert b'42' == response.data
