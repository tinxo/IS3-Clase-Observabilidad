"""
Ejemplo un poco mas elaborado
para llegar a tests de integración
""" 

class Liquidacion():

    def __init__(self, 
                    p_valor_hora = 5000, 
                    p_pct_bonificacion = 8, 
                    p_pct_retenciones = 11, 
                    p_pct_obra_social = 3):
        self.valor_hora = p_valor_hora
        self.pct_bonificacion = p_pct_bonificacion
        self.pct_retenciones = p_pct_retenciones
        self.pct_obraSocial = p_pct_obra_social


    def calcular_sueldo_basico(self, hs_trabajadas):
        # Basico = horas trabajadas * valor hora
        basico = int(hs_trabajadas) * self.valor_hora
        return round(basico,2)

    def calcular_sueldo_bruto(self, basico, antiguedad):
        # Bruto = basico + bonificaciones + antiguedad
        basico = float(basico)
        bruto = basico + (basico * (self.pct_bonificacion * 0.01))
        if (antiguedad < 5):
            bruto = bruto + (basico * 0.1) # 10%
        elif (antiguedad < 10):
            bruto = bruto + (basico * 0.2) # 20%
        elif (antiguedad < 20):
            bruto = bruto + (basico * 0.3) # 30%
        else:
            bruto = bruto + (basico * 0.4) # 40%
        return round(bruto,2)

    def calcular_sueldo_neto(self, bruto):
        # Neto = bruto - retenciones - obra social
        neto = bruto - (bruto * (self.pct_retenciones * 0.01)) - (bruto * (self.pct_obraSocial * 0.01))
        return round(neto,2)

    def calcular_sueldo_empleado(self, cant_hs_trabajadas, antiguedad_empleado):
        sueldo_basico = self.calcular_sueldo_basico(cant_hs_trabajadas)
        sueldo_bruto = self.calcular_sueldo_bruto(sueldo_basico, antiguedad_empleado)
        sueldo_neto = self.calcular_sueldo_neto(sueldo_bruto)
        return round(sueldo_neto,2)