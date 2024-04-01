import pytest

from jsonschema import validate

from main import pairwised_result
from schemas import schema

from file_helpers.csv_helper import read_lines_from_csv

from pydantic import BaseModel, field_validator, Field

from typing import Optional


class PetStoreBaseModel(BaseModel):
    id: int
    name: str


class CategoryModel(PetStoreBaseModel):
    pass


class TagModel(PetStoreBaseModel):
    pass


class PetModel(PetStoreBaseModel):
    category: Optional[CategoryModel] = None
    name: Optional[str] = ""
    photoUrls: list
    tags: list[TagModel]
    status: str

    @field_validator("name")
    @classmethod
    def status_validator(cls, name):
        assert type(name) == int


class UserModel(PetStoreBaseModel):
    username: str
    firstName: str = Field(alias="name")
    lastName: str = Field(alias="last_name")
    email: str
    password: str
    phone: str
    userStatus: int = Field(alias="user_status")


# @pytest.mark.parametrize(["status", "code"],
#                          [("available", 200), ("pending", 200), ("sold", 200)])
def test_get_pet_by_status(api_client):
    query = {"status": "available"}
    response = api_client.get_pets_by_status(query)
    json_response = response.json()
    pets = [PetModel.parse_obj(obj) for obj in json_response]
    assert response.status_code == 200
    assert pets[0].category.id >= 0
    for pet in pets:
        assert pet.status == "available"


# @pytest.mark.parametrize("data", read_lines_from_csv())
def test_create_user(api_client):
    data = UserModel(id=1, username="i", name="Irina", last_name="Popova",
                     email="email", password="Pass", phone="790000000", user_status=1)
    print(data.dict())
    response = api_client.create_user(data=data.dict())
    assert response.status_code == 200


@pytest.mark.parametrize("computers", pairwised_result)
def test_computers(computers):
    print(computers)
