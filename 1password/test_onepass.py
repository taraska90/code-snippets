import subprocess
from onepass import get_auth_data
import pytest

@pytest.fixture
def sample_request():
    return get_auth_data("test_vdx")


def test_should_return_no_flag_when_flag_not_known():
    output = get_auth_data("no_item", auth_flag="no_flag")
    assert output == "no auth flag found"

def test_should_return_dictionary_type(sample_request):
    assert isinstance(sample_request, dict)

def test_is_one_pass_enable_in_cli_mode():
    pass