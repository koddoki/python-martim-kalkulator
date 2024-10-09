# main.py
import pytest
from main import addiere, subtrahiere, multipliziere, dividiere


def test_addiere():
    assert addiere(2, 3) == 5
    assert addiere(-1, 1) == 0
    assert addiere(0, 0) == 0
    assert addiere(-1, -1) == -2


def test_subtrahiere():
    assert subtrahiere(5, 3) == 2
    assert subtrahiere(-1, -1) == 0
    assert subtrahiere(0, 1) == -1
    assert subtrahiere(1, 0) == 1


def test_multipliziere():
    assert multipliziere(2, 3) == 6
    assert multipliziere(-1, 1) == -1
    assert multipliziere(0, 5) == 0
    assert multipliziere(-1, -1) == 1


def test_dividiere():
    assert dividiere(6, 3) == 2
    assert dividiere(-1, 1) == -1
    assert dividiere(0, 1) == 0
    assert dividiere(5, 0) == "Fehler: Division durch Null!"


# Wenn du die Tests automatisch ausführen möchtest, wenn diese Datei ausgeführt wird
if __name__ == "__main__":
    pytest.main()
