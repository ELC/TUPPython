from hypothesis import given
import hypothesis.strategies as st


# Ejercicio 1

from ejercicio_01 import maximo_basico, maximo_libreria, maximo_ternario


def test_asserts_ejercicio_01():
    import ejercicio_01


@given(st.floats(allow_nan=False, allow_infinity=False), st.floats(allow_nan=False, allow_infinity=False))
def test_ejercicio_01_commutative(x, y):
    assert maximo_basico(x, y) == maximo_basico(y, x)
    assert maximo_libreria(x, y) == maximo_libreria(y, x)
    assert maximo_ternario(x, y) == maximo_ternario(y, x)


@given(st.floats(allow_nan=False, allow_infinity=False), st.floats(allow_nan=False, allow_infinity=False))
def test_ejercicio_01_idempotent(x, y):
    assert maximo_basico(maximo_basico(x, y), maximo_basico(y, x)) == maximo_basico(y, x)
    assert maximo_libreria(maximo_libreria(x, y), maximo_libreria(y, x)) == maximo_libreria(y, x)
    assert maximo_ternario(maximo_ternario(x, y), maximo_ternario(y, x)) == maximo_ternario(y, x)


@given(st.floats(allow_nan=False, allow_infinity=False, max_value=0, exclude_max=True),
       st.floats(allow_nan=False, allow_infinity=False, min_value=0, exclude_min=True))
def test_ejercicio_01_positives_negatives(x, y):
    assert maximo_basico(x, y) == y
    assert maximo_libreria(x, y) == y
    assert maximo_ternario(x, y) == y


@given(st.floats(allow_nan=False, allow_infinity=False, max_value=0, exclude_max=True), st.just(0))
def test_ejercicio_01_negatives(x, y):
    assert maximo_basico(x, y) == y
    assert maximo_libreria(x, y) == y
    assert maximo_ternario(x, y) == y


@given(st.floats(allow_nan=False, allow_infinity=False, min_value=0, exclude_min=True), st.just(0))
def test_ejercicio_01_positives(x, y):
    assert maximo_basico(x, y) == x
    assert maximo_libreria(x, y) == x
    assert maximo_ternario(x, y) == x


# Ejercicio 2

def test_asserts_ejercicio_02():
    import ejercicio_02


def test_asserts_ejercicio_03():
    import ejercicio_03


def test_asserts_ejercicio_04():
    import ejercicio_04


def test_asserts_ejercicio_05():
    import ejercicio_05


def test_asserts_ejercicio_06():
    import ejercicio_06


def test_asserts_ejercicio_07():
    import ejercicio_07


def test_asserts_ejercicio_09():
    import ejercicio_09


def test_asserts_ejercicio_10():
    import ejercicio_10


def test_asserts_ejercicio_11():
    import ejercicio_11


def test_asserts_ejercicio_12():
    import ejercicio_12


def test_asserts_ejercicio_13():
    import ejercicio_13


def test_asserts_ejercicio_14():
    import ejercicio_14


def test_asserts_ejercicio_15():
    import ejercicio_15


def test_asserts_ejercicio_16():
    import ejercicio_16


def test_asserts_ejercicio_17():
    import ejercicio_17
