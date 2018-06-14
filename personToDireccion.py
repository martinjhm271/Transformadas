#!/usr/bin/env python
# -*- coding: cp1252 -*-
from Maltego import *
from MaltegoTransform import *
import pandas as pd
from sodapy import Socrata

def PersonToDireccion(m):

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
                dir=r[i]['nombre_concejal']
                barrio=r[i]['barrio']
                l=r[i]['localizacion']['coordinates']
                break

        ent = TRX.addEntity('maltego.Location', dir)
        ent.addAdditionalFields("country", "Country", True, "Colombia")
        ent.addAdditionalFields("location.area", "Area", True, barrio)
        ent.addAdditionalFields("streetaddress", "Street Address", True, dir)
        ent.addAdditionalFields("longitude", "Longitude", True, l[0])
        ent.addAdditionalFields("latitude", "Latituded", True, l[1])


    except Exception as e:
        TRX.addUIMessage("Cedula no encontrada en la base de datos")

    TRX.returnOutput()