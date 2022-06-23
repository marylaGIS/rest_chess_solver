import pytest
import chess


def test_king_moves():
    k0 = chess.King("a", 15)
    assert k0.list_available_moves() == ["Field does not exist"]

    k1 = chess.King("a", 1)
    assert sorted(k1.list_available_moves()) == sorted(["b1", "a2", "b2"])

    k2 = chess.King("b", 1)
    k3 = chess.King("d", 1)
    assert sorted(k2.list_available_moves()) == sorted(
        ["g1", "f1", "b1", "d1", "e1", "c1"]
    )
    assert sorted(k3.list_available_moves()) == sorted(
        ["g1", "f1", "b1", "d1", "e1", "c1"]
    )
