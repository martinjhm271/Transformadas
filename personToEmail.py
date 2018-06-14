#!/usr/bin/env python
# -*- coding: cp1252 -*-
from Maltego import *
from MaltegoTransform import *
import pandas as pd
from sodapy import Socrata

def PersonToEmail(m):

    TRX = MaltegoTransform()
    #m.parseArguments(sys.argv)
    #nombre=sys.argv[1]
    nombre=m.Value
    try:
        client = Socrata("www.datos.gov.co", None)
        r = client.get("3ard-sj8g", limit=2000)

        #for key, value in data.items():
            #print key, value
        for i in range(len(r)):
            if ( r[i]['nombre_prestador'] ==  nombre) :
                email=r[i]['email']
                break

        ent = TRX.addEntity('maltego.EmailAddress', email)



    except Exception as e:
        TRX.addUIMessage("Cedula no encontrada en la base de datos")

    TRX.returnOutput()


