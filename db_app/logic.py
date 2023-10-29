from django.http import JsonResponse
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from difflib import SequenceMatcher

def determinar_credito(request, datos_formulario):
    
    dias_mora_credito = int(datos_formulario.get('dias_mora_credito'))
    integrantes_hogar = int(datos_formulario.get('integrantes_hogar'))
    antiguedad_laboral_anios = int(datos_formulario.get('antiguedad_laboral_anios'))
    saldo_creditos = int(datos_formulario.get('saldo_creditos'))
    saldo_ahorro = int(datos_formulario.get('saldo_ahorro'))
    nro_prestamos_recibidos = int(datos_formulario.get('nro_prestamos_recibidos'))
    edad_anios = int(datos_formulario.get('edad_anios'))

    nombre_ciudad_residencia = datos_formulario.get('nombre_ciudad_residencia')
    genero = datos_formulario.get('genero')
    
   
    # Determinar la viabilidad de dar un crédito
    valido = 1
    if dias_mora_credito == 0 and integrantes_hogar <= 1 and antiguedad_laboral_anios >= 2 and saldo_creditos < saldo_ahorro and nro_prestamos_recibidos >= 1 and ((edad_anios >= 22 and edad_anios <= 25) or edad_anios >= 74) and ((SequenceMatcher(None, 'CUCUTA', nombre_ciudad_residencia).ratio())>0.8 or (SequenceMatcher(None, 'MEDELLIN', nombre_ciudad_residencia).ratio())>0.8 or (SequenceMatcher(None, 'BOGOTA', nombre_ciudad_residencia).ratio())>0.8 or (SequenceMatcher(None, 'ALVARADO', nombre_ciudad_residencia).ratio())>0.8 ):
        valido = 1
    else:
        valido = 0

    if valido == 1:
        resultado = "Aprobado"
    else:
        resultado = "Rechazado"
        
        

    return resultado
