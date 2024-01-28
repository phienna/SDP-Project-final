import pytest

from flaskr.view.disk import disk_usage


@pytest.mark.unit
def test_disk_usage(mocker):
    mocker.patch('flaskr.view.disk.Hardware.get_disk_usage',
                 return_value=25)
    diskUsage= disk_usage()

    assert '25' == diskUsage


@pytest.mark.api
def test_disk_usage_api(mocker, client):
    mocker.patch('flaskr.view.disk.Hardware.get_disk_usage',
                 return_value=25)
    response = client.get('/disk/usage')

    assert b'25' == response.data