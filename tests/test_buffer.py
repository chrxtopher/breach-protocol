import pytest

from engine.buffer import Buffer, BufferFullError


def test_new_buffer_is_empty() -> None:
    """Test new buffer contents is empty"""
    buffer = Buffer(3)
    assert buffer.get_contents() == []


def test_add_code_to_buffer() -> None:
    """Test buffer contents length after adding codes"""
    buffer = Buffer(2)
    buffer.add("1A")
    assert len(buffer.get_contents()) == 1
    buffer.add("2A")
    assert len(buffer.get_contents()) == 2


def test_order_of_contents() -> None:
    """Test buffer contents order after adding codes"""
    buffer = Buffer(3)
    buffer.add("1A")
    buffer.add("2A")
    buffer.add("3A")
    assert buffer.get_contents() == ["1A", "2A", "3A"]


def test_buffer_is_full() -> None:
    """Test buffer.is_full() returns False if there is room in contents, True if full"""
    buffer = Buffer(3)
    buffer.add("1A")
    buffer.add("2A")
    assert not buffer.is_full()
    buffer.add("3A")
    assert buffer.is_full()


def test_buffer_empty_slot_count() -> None:
    """Test buffer.empty_slot_count() goes down as codes are added to buffer contents"""
    buffer = Buffer(3)
    assert buffer.empty_slot_count() == 3
    buffer.add("1A")
    assert buffer.empty_slot_count() == 2
    buffer.add("2A")
    buffer.add("3A")
    assert buffer.empty_slot_count() == 0


def test_error_when_adding_to_full_buffer() -> None:
    """Test buffer raises error when adding codes to full buffer — buffer contents should persist"""
    buffer = Buffer(1)
    buffer.add("1A")
    with pytest.raises(BufferFullError):
        buffer.add("2A")
    assert buffer.get_contents() == ["1A"]
