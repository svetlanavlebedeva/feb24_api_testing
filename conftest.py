import pytest

from petstore_api_client.petstore_api_client import PetstoreApiClient


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://petstore.swagger.io/v2",
        choices=["https://petstore.swagger.io/v2", "https://petstore.swagger.io/v1"],
        help="This is request url"
    )

    parser.addoption(
        "--token",
        help="token to authorize",

    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def token(request):
    return request.config.getoption("--token")


@pytest.fixture(scope="function")
def api_client(base_url, token):
    client = PetstoreApiClient(base_url=base_url,
                               auth_token=token)
    return client
