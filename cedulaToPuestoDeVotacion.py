#!/usr/bin/env python
# -*- coding: cp1252 -*-

# Maltego transform for getting the robots.txt file from websites

from Maltego import *
from MaltegoTransform import *
import requests
from bs4 import BeautifulSoup


def CedulaToPuestoDeVotacion(m):

    TRX = MaltegoTransform()
    #TRX.parseArguments(sys.argv)
    #cedula=sys.argv[1]
    cedula=m.Value
    #cedula='1026585665'
    website = 'wsp.registraduria.gov.co/estadodocs/resultadobusqueda.php?cedula='
    #port = m.getVar('ports')
    #port = port.split(',')
    #ssl = m.getVar('website.ssl-enabled')


    try:
        url = 'https://' + website + cedula;
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        #print r.text.encode('utf-8')
        res = soup.findAll("table", {"class": "tabla_solicitud"})
        lista=[]
        for i in res:
            lista=i.find_all('b')
        direccion=str(lista[1])
        departamento=str(lista[2])
        direccion=direccion.replace("<b>","").replace("</b>","")
        departamento=departamento.replace("<b>","").replace("</b>","")


        ent=TRX.addEntity('eci.LugarExpedicion', direccion)
        ent.addAdditionalFields("properity.eci.departamento", "Departamento", True, departamento)

    except Exception as e:
        TRX.addUIMessage("Cedula no encontrada en la base de datos")

    TRX.returnOutput()


