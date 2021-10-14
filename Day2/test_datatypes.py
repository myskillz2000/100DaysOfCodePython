import datatypes

def test_add():
    assert datatypes.add(3,7) == 10

def test_input_then_add(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "39")
    assert datatypes.input_then_add() == 12
    
