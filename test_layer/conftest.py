import pytest

from logic_layer.songs_logic import delete_db_songs_data
from logic_layer.users_logic import delete_db_users_data


@pytest.fixture
def set_up_data_base():
    delete_db_users_data()
    delete_db_songs_data()
