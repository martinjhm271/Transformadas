#!/usr/bin/env python
# -*- coding: cp1252 -*-
from Maltego import *
from MaltegoTransform import *
import pandas as pd
from sodapy import Socrata


def CedulaToPersonConsejal(m):
    TRX = MaltegoTransform()
    #TRX.parseArguments(sys.argv)
    #cedula=sys.argv[1]
    cedula = m.Value

    try:
        client = Socrata("www.datos.gov.co", None)
        r = client.get("gnvi-fbsz", limit=2000)
        #for key, value in data.items():
            #print key, value
        for i in range(len(r)):
            if ( r[i]['cc'] ==  cedula) :
                nombre=r[i]['nombre_concejal']
                break

        nombre=nombre.split(" ")
        if(len(nombre)==4):
            firts=nombre[0]+" "+nombre[1]
            last=nombre[2]+" "+nombre[3]
            full=nombre[0]+" "+nombre[1] + " "+nombre[2]+" "+nombre[3]
        else:
            firts = nombre[0]
            last = nombre[1] + " " + nombre[2]
            full = nombre[0] + " " + nombre[1] + " " + nombre[2]
        ent=TRX.addEntity('maltego.Person', full)
        ent.addAdditionalFields("person.firtsnames", "Firts Names", True,firts )
        ent.addAdditionalFields("person.lastname", "Surname", True, last)


    except Exception as e:
        TRX.addUIMessage("Cedula no encontrada en la base de datos")

    TRX.returnOutput()


