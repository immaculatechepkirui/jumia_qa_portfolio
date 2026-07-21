import pytest

BASE_URL = "https://www.jumia.co.ke"

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: mark test as smoke test"
    )

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL