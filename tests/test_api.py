import pytest

from jsonschema import validate

from schemas import schema


@pytest.mark.parametrize(["status", "code"],
                         [("available", 200), ("pending", 200), ("sold", 200)])
def test_get_pet_by_status(api_client, status, code):
    query = {"status": status}
    response = api_client.get_pets_by_status(query)
    json_response = response.json()
    assert response.status_code == code
    assert json_response
    validate(instance=json_response[0], schema=schema)
