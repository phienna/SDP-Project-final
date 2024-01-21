import pytest

from flaskr.view.cpu import cpu_temp


@pytest.mark.unit
def test_cpu_temp(mocker):
    mocker.patch('flaskr.view.cpu.Hardware.get_cpu_temp',
                 return_value=33.0)
    temperature = cpu_temp()

    assert '33.0' == temperature


@pytest.mark.api
def test_cpu_temp_api(mocker, client):
    mocker.patch('flaskr.view.cpu.Hardware.get_cpu_temp',
                 return_value=33.0)
    response = client.get('/cpu/temp')

    assert b'33.0' == response.data
