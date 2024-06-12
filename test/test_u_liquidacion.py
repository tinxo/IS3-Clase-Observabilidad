import pytest
import operaciones.sueldos as ops

def setup():
    instancia = ops.Liquidacion()
    return instancia

def test_instancia_basica():
    un_empleado = setup()
    assert un_empleado.valor_hora == 5000
    assert un_empleado.pct_bonificacion == 8
    assert un_empleado.pct_retenciones == 11
    assert un_empleado.pct_obraSocial == 3

def test_calcular_sueldo_basico():
    un_empleado = setup()
    hs_trabajadas = 40
    assert un_empleado.calcular_sueldo_basico(hs_trabajadas) == 200000.00

@pytest.mark.parametrize(
    "valor_a, valor_b, resultado",
    [
        (22000, 3, 25960.00),
        (22000, 6, 28160.00),
    ]
)
def test_calcular_sueldo_bruto(valor_a, valor_b, resultado):
    un_empleado = setup()
    assert un_empleado.calcular_sueldo_bruto(valor_a, valor_b) == resultado

def test_calcular_sueldo_neto():
    un_empleado = setup()
    bruto = 25960
    assert un_empleado.calcular_sueldo_neto(bruto) == 22325.60

def test_calcular_sueldo_empleado():
    un_empleado = setup()
    hs_trabajadas = 40
    antiguedad = 3
    assert un_empleado.calcular_sueldo_empleado(hs_trabajadas, antiguedad) == 202960.00