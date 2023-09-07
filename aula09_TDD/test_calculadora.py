from calculadora import Calculadora


def teste_01_soma_0_0():
    calc = Calculadora()
    assert calc.soma(0, 0) == 0


def teste_01_soma_0():
    calc = Calculadora()
    assert calc.soma(0, 10) == 10
    assert calc.soma(10, 0) == 10


def teste_01_soma_3_5():
    calc = Calculadora()
    assert calc.soma(3, 5) == 8
    assert calc.soma(5, 3) == 8


def teste_subtrai_10_2():
    calc = Calculadora()
    assert calc.subtrai(10, 2) == 8


def teste_subtrai_2_10():
    calc = Calculadora()
    assert calc.subtrai(2, 10) == -8
