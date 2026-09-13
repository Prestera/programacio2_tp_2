from datetime import date

def validar_campo_vacio(valor):
    if valor is None or str(valor).strip() == "":
        raise ValueError("El campo no puede estar vacío")
    
def validar_num(valor):    
    try:
        float(valor)
    except (TypeError, ValueError):
        raise ValueError("El valor debe ser numérico")
    
def validar_num_positivo(valor):        
    validar_num(valor)
    
    if float(valor) <= 0:
        raise ValueError("El valor debe ser mayor que cero")

def validar_fecha(fecha_ingresada):
    if not isinstance(fecha_ingresada, date):
        raise ValueError("La fecha no es válida")

def validar_fecha_futura(fecha_ingresada):
    validar_fecha(fecha_ingresada)
    
    if fecha_ingresada > date.today():
        raise ValueError("La fecha no puede ser futura")
    
def validar_fecha_no_futura(fecha):
    if fecha > date.today():
        raise ValueError("La fecha no puede ser futura.")    