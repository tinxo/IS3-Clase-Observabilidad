import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Vista de Empleados' in rv.data

def test_calculate_salary(client):
    rv = client.post('/calculate_salary', data={
        'apellido': 'García',
        'nombre': 'Juan',
        'nro_documento': '12345678',
        'antiguedad': 5,
        'horas_trabajadas': 40
    })
    assert rv.status_code == 200
    assert b'Sueldo Neto' in rv.data
    assert b'220160.0' in rv.data