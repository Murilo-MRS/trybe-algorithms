import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message("message", "key")

    assert encrypt_message("message", 1) == "m_egasse"
    assert encrypt_message("message", 2) == "egass_em"
    assert encrypt_message("message", 3) == "sem_egas"
    assert encrypt_message("message", 4) == "ega_ssem"

    assert encrypt_message("message", 8) == "egassem"
    assert encrypt_message("message", -1) == "egassem"
