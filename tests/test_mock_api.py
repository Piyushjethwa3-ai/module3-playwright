from unittest.mock import patch
import requests

@patch('requests.get')
def test_mock_api(mock_get):
    # Mock the API response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{"id":1, "name":"Mock User"}]
    # Call the API
    response = requests.get("https://fake-api.com/users")

    # Assertions
    assert response.status_code == 200
    assert response.json()[0]['name'] == "Mock User"