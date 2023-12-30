from infrastructure_layer.api import get_endpoint

def test_can_call_endpoint():
    response = get_endpoint()
    assert response.status_code == 404, "Can`t connect to server"

