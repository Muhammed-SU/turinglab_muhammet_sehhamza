import pytest
# Motor kodunuzu turinglab paketi altından çağırıyoruz
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Sizin mevcut kodlarınız buradan aşağıya devam edecek:
import pytest
from turinglab.tm_engine import SingleTapeTM
# ... kalan kodlar ...
from turinglab.tm_engine import SingleTapeTM

# Örnek bir makine sözlüğü (Testlerde simüle etmek için)
dummy_config = {
    "name": "test_machine",
    "states": ["q0", "q_accept", "q_reject"],
    "blank": "B",
    "start_state": "q0",
    "accept_states": ["q_accept"],
    "reject_states": ["q_reject"],
    "transitions": [
        {"state": "q0", "read": "1", "next": "q_accept", "write": "1", "move": "R"},
        {"state": "q0", "read": "0", "next": "q_reject", "write": "0", "move": "R"}
    ]
}

# Fonksiyon isimlerinin "test_" ile başlaması ZORUNLUDUR
def test_machine_acceptance():
    tm = SingleTapeTM(dummy_config)
    result = tm.run("1")
    assert result.accepted is True
    assert result.reason == "accept"

def test_machine_rejection():
    tm = SingleTapeTM(dummy_config)
    result = tm.run("0")
    assert result.accepted is False
    assert result.reason == "reject"

def test_no_transition():
    tm = SingleTapeTM(dummy_config)
    result = tm.run("X")  # X karakteri için kural yok
    assert result.accepted is False
    assert result.reason == "no_transition"

def test_timeout():
    tm = SingleTapeTM(dummy_config)
    # max_steps'i 0 vererek anında timeout'a düşmesini test ediyoruz
    result = tm.run("1", max_steps=0)
    assert result.accepted is False
    assert result.reason == "timeout"

def test_invalid_yaml_raise():
    # Olmayan bir dosya okutulduğunda ValueError fırlatılıp fırlatılmadığı testi
    with pytest.raises(ValueError):
        SingleTapeTM.from_yaml("non_existing_file.yaml")