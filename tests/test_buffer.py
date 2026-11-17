from engine.buffer import Buffer

def test_new_buffer_is_empty() -> None:
    buffer = Buffer(3)
    assert buffer.get_contents() == []