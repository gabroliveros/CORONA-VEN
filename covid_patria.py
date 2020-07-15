#!/usr/bin/env python 3.8
# -*- coding: utf-8 -*-
#          **
#         //\\
#   o==[=//==\\====>
#       **    **
#+++++++++++o++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#       *CORONA-VEN*
#
# Autor:_<<Gabriel Oliveros>>_
#
# Rasca el blog de Patria Covid-19 (Venezuela) y muestra las cifras actualizadas.
# Los resultados se imprimen en pantalla y la línea de tiempo en un '.csv'
#+++++++++++o++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import json
import requests
import csv

# IMPRESIÓN DE DATOS
def principales():
    c=int(info['Confirmed']['Count'])
    print('CIFRAS TOTALES')
    print('Confirmados', info['Confirmed']['Count'])
    p_recup=int(info['Recovered']['Count'])*100/c
    print('Recuperados', info['Recovered']['Count'],'('+str('{:.1f}'.format(p_recup))+'%'+')')
    p_fall=int(info['Deaths']['Count'])*100/c
    print('Fallecidos', info['Deaths']['Count'],'('+str('{:.1f}'.format(p_fall))+'%'+')')
    p_act=int(info['Active']['Count'])*100/c
    print('Activos', info['Active']['Count'],'('+str('{:.1f}'.format(p_act))+'%'+')','\n')

def edad():
    c=int(info['Confirmed']['Count'])
    print('CASOS POR GRUPO DE EDAD')
    p_09=int(info['Confirmed']['ByAgeRange']['0-9'])*100/c
    print('0-9   años:', info['Confirmed']['ByAgeRange']['0-9'],'('+str('{:.1f}'.format(p_09))+'%'+')')
    p_1019=int(info['Confirmed']['ByAgeRange']['10-19'])*100/c
    print('10-19 años:', info['Confirmed']['ByAgeRange']['10-19'],'('+str('{:.1f}'.format(p_1019))+'%'+')')
    p_2029=int(info['Confirmed']['ByAgeRange']['20-29'])*100/c
    print('20-29 años:', info['Confirmed']['ByAgeRange']['20-29'],'('+str('{:.1f}'.format(p_2029))+'%'+')')
    p_3039=int(info['Confirmed']['ByAgeRange']['30-39'])*100/c
    print('30-39 años:', info['Confirmed']['ByAgeRange']['30-39'],'('+str('{:.1f}'.format(p_3039))+'%'+')')
    p_4049=int(info['Confirmed']['ByAgeRange']['40-49'])*100/c
    print('40-49 años:', info['Confirmed']['ByAgeRange']['40-49'],'('+str('{:.1f}'.format(p_4049))+'%'+')')
    p_5059=int(info['Confirmed']['ByAgeRange']['50-59'])*100/c
    print('50-59 años:', info['Confirmed']['ByAgeRange']['50-59'],'('+str('{:.1f}'.format(p_5059))+'%'+')')
    p_6069=int(info['Confirmed']['ByAgeRange']['60-69'])*100/c
    print('60-69 años:', info['Confirmed']['ByAgeRange']['60-69'],'('+str('{:.1f}'.format(p_6069))+'%'+')')
    p_7079=int(info['Confirmed']['ByAgeRange']['70-79'])*100/c
    print('70-79 años:', info['Confirmed']['ByAgeRange']['70-79'],'('+str('{:.1f}'.format(p_7079))+'%'+')')
    p_8089=int(info['Confirmed']['ByAgeRange']['80-89'])*100/c
    print('80-89 años:', info['Confirmed']['ByAgeRange']['80-89'],'('+str('{:.1f}'.format(p_8089))+'%'+')')
    p_9099=int(info['Confirmed']['ByAgeRange']['90-99'])*100/c
    print('90-99 años:', info['Confirmed']['ByAgeRange']['90-99'],'('+str('{:.1f}'.format(p_9099))+'%'+')','\n')

def sexo():
    c=int(info['Confirmed']['Count'])
    print('CASOS POR SEXO')
    p_mas=int(info['Confirmed']['ByGender']['male'])*100/c
    print('Hombres:', info['Confirmed']['ByGender']['male'],'('+str('{:.1f}'.format(p_mas))+'%'+')')
    p_fem=int(info['Confirmed']['ByGender']['female'])*100/c
    print('Mujeres:', info['Confirmed']['ByGender']['female'],'('+str('{:.1f}'.format(p_fem))+'%'+')','\n')

def estado():
    c=int(info['Confirmed']['Count'])
    print('CASOS POR ESTADO')
    p_ama=int(info['Confirmed']['ByState']['Amazonas'])*100/c
    print('Amazonas:', info['Confirmed']['ByState']['Amazonas'],'('+str('{:.1f}'.format(p_ama))+'%'+')')
    p_anz=int(info['Confirmed']['ByState']['Anzoátegui'])*100/c
    print('Anzoátegui:', info['Confirmed']['ByState']['Anzoátegui'],'('+str('{:.1f}'.format(p_anz))+'%'+')')
    p_apu=int(info['Confirmed']['ByState']['Apure'])*100/c
    print('Apure:', info['Confirmed']['ByState']['Apure'],'('+str('{:.1f}'.format(p_apu))+'%'+')')
    p_ara=int(info['Confirmed']['ByState']['Aragua'])*100/c
    print('Aragua:', info['Confirmed']['ByState']['Aragua'],'('+str('{:.1f}'.format(p_ara))+'%'+')')
    p_bar=int(info['Confirmed']['ByState']['Barinas'])*100/c
    print('Barinas:', info['Confirmed']['ByState']['Barinas'],'('+str('{:.1f}'.format(p_bar))+'%'+')')
    p_bol=int(info['Confirmed']['ByState']['Bolívar'])*100/c
    print('Bolívar:', info['Confirmed']['ByState']['Bolívar'],'('+str('{:.1f}'.format(p_bol))+'%'+')')
    p_car=int(info['Confirmed']['ByState']['Carabobo'])*100/c
    print('Carabobo:', info['Confirmed']['ByState']['Carabobo'],'('+str('{:.1f}'.format(p_car))+'%'+')')
    p_coj=int(info['Confirmed']['ByState']['Cojedes'])*100/c
    print('Cojedes:', info['Confirmed']['ByState']['Cojedes'],'('+str('{:.1f}'.format(p_coj))+'%'+')')
    p_del=int(info['Confirmed']['ByState']['Delta Amacuro'])*100/c
    print('Delta Amacuro:', info['Confirmed']['ByState']['Delta Amacuro'],'('+str('{:.1f}'.format(p_del))+'%'+')')
    p_dc=int(info['Confirmed']['ByState']['Distrito Capital'])*100/c
    print('Distrito Capital:', info['Confirmed']['ByState']['Distrito Capital'],'('+str('{:.1f}'.format(p_dc))+'%'+')')
    p_fal=int(info['Confirmed']['ByState']['Falcón'])*100/c
    print('Falcón:', info['Confirmed']['ByState']['Falcón'],'('+str('{:.1f}'.format(p_fal))+'%'+')')
    p_gua=int(info['Confirmed']['ByState']['Guárico'])*100/c
    print('Guárico:', info['Confirmed']['ByState']['Guárico'],'('+str('{:.1f}'.format(p_gua))+'%'+')')
    p_lar=int(info['Confirmed']['ByState']['Lara'])*100/c
    print('Lara:', info['Confirmed']['ByState']['Lara'],'('+str('{:.1f}'.format(p_lar))+'%'+')')
    p_lr=int(info['Confirmed']['ByState']['Los Roques'])*100/c
    print('Los Roques:', info['Confirmed']['ByState']['Los Roques'],'('+str('{:.1f}'.format(p_lr))+'%'+')')
    p_mer=int(info['Confirmed']['ByState']['Mérida'])*100/c
    print('Mérida:', info['Confirmed']['ByState']['Mérida'],'('+str('{:.1f}'.format(p_mer))+'%'+')')
    p_mir=int(info['Confirmed']['ByState']['Miranda'])*100/c
    print('Miranda:', info['Confirmed']['ByState']['Miranda'],'('+str('{:.1f}'.format(p_mir))+'%'+')')
    p_mon=int(info['Confirmed']['ByState']['Monagas'])*100/c
    print('Monagas:', info['Confirmed']['ByState']['Monagas'],'('+str('{:.1f}'.format(p_mon))+'%'+')')
    p_ne=int(info['Confirmed']['ByState']['Nueva Esparta'])*100/c
    print('Nueva Esparta:', info['Confirmed']['ByState']['Nueva Esparta'],'('+str('{:.1f}'.format(p_ne))+'%'+')')
    p_por=int(info['Confirmed']['ByState']['Portuguesa'])*100/c
    print('Portuguesa:', info['Confirmed']['ByState']['Portuguesa'],'('+str('{:.1f}'.format(p_por))+'%'+')')
    p_suc=int(info['Confirmed']['ByState']['Sucre'])*100/c
    print('Sucre:', info['Confirmed']['ByState']['Sucre'],'('+str('{:.1f}'.format(p_suc))+'%'+')')
    p_tac=int(info['Confirmed']['ByState']['Táchira'])*100/c
    print('Táchira:', info['Confirmed']['ByState']['Táchira'],'('+str('{:.1f}'.format(p_tac))+'%'+')')
    p_tru=int(info['Confirmed']['ByState']['Trujillo'])*100/c
    print('Trujillo:', info['Confirmed']['ByState']['Trujillo'],'('+str('{:.1f}'.format(p_tru))+'%'+')')
    p_var=int(info['Confirmed']['ByState']['La Guaira'])*100/c
    print('Vargas:', info['Confirmed']['ByState']['La Guaira'],'('+str('{:.1f}'.format(p_var))+'%'+')')
    p_yar=int(info['Confirmed']['ByState']['Yaracuy'])*100/c
    print('Yaracuy:', info['Confirmed']['ByState']['Yaracuy'],'('+str('{:.1f}'.format(p_yar))+'%'+')')
    p_zul=int(info['Confirmed']['ByState']['Zulia'])*100/c
    print('Zulia:', info['Confirmed']['ByState']['Zulia'],'('+str('{:.1f}'.format(p_zul))+'%'+')','\n')

def linea_tiempo():
    with open('linea_tiempo_covid_ven.csv','w',encoding='utf-8',newline='') as csv_file:
        writer=csv.writer(csv_file)
        writer.writerow(['Fecha','Confirmados','Nuevos casos','Recuperados','Nuevos recuperados',
                         'Fallecidos','Nuevos fallecidos','Activos'])
        fecha=''
        confirmados=''
        nuevos_casos=''
        recuperados=''
        nuevos_recuperados=''
        fallecidos=''
        nuevos_fallecidos=''
        activos=''
        r=2
        for i in info:
            fecha=i['Date']
            confirmados=i['Confirmed']['Count']
            nuevos_casos=i['Confirmed']['New']
            recuperados=i['Recovered']['Count']
            nuevos_recuperados=i['Recovered']['New']
            fallecidos=i['Deaths']['Count']
            nuevos_fallecidos=i['Deaths']['New']
            activos=i['Active']['Count']
            writer.writerow([fecha,confirmados,nuevos_casos,recuperados,nuevos_recuperados,
                             fallecidos,nuevos_fallecidos,activos])
            print('Finalizado. Ya puede abrir "linea_tiempo_covid_ven.csv"') 

# CONSOLA            
while True:
    print('====================================')
    print('            *CORONA-VEN*            ')
    print('====================================')
    print('      _<by Gabriel Oliveros>_'  ,'\n')
    print('1. Obtener reporte general          ')
    print('2. Obtener datos principales        ')
    print('3. Obtener datos por grupo de edad  ')
    print('4. Obtener datos por sexo           ')
    print('5. Obtener datos por estado         ')
    print('6. Obtener la línea de tiempo       ')
    print('0. Salir                            ')
    print('====================================','\n')

    try:
        opcion=int(input('Indique el número de opción: '))
        print('')
    except ValueError:
        print('<<<Escriba una opción válida>>>',2*'\n')
        continue
        
    if opcion==1:
        url = requests.get('https://covid19.patria.org.ve/api/v1/summary')
        info = json.loads(url.content)
        principales()
        edad()
        sexo()
        estado()
    if opcion==2:
        url = requests.get('https://covid19.patria.org.ve/api/v1/summary')
        info = json.loads(url.content)
        principales()
    if opcion==3:
        url = requests.get('https://covid19.patria.org.ve/api/v1/summary')
        info = json.loads(url.content)
        edad()
    if opcion==4:
        url = requests.get('https://covid19.patria.org.ve/api/v1/summary')
        info = json.loads(url.content)
        sexo()
    if opcion==5:
        url = requests.get('https://covid19.patria.org.ve/api/v1/summary')
        info = json.loads(url.content)
        estado()
    if opcion==6:
        url = requests.get('https://covid19.patria.org.ve/api/v1/timeline')
        info = json.loads(url.content)
        linea_tiempo()
    if opcion==0:
        print('Hasta luego')
        break
    if opcion>6 or opcion==str:
        print('<<<Escriba una opción válida>>>',2*'\n')
    
