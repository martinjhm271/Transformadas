#!/usr/bin/env python
# -*- coding: cp1252 -*-
from Maltego import *
from MaltegoTransform import *
import pandas as pd
from sodapy import Socrata



def CedulaToLocationConsejal(m):
    TRX = MaltegoTransform()
    #m.parseArguments(sys.argv)
    #cedula=sys.argv[1]
    cedula=m.Value
    try:
        client = Socrata("www.datos.gov.co", None)
        r = client.get("gnvi-fbsz", limit=2000)
        #for key, value in data.items():
            #print key, value
        for i in range(len(r)):
            if ( r[i]['cc'] ==  cedula) :
                municipio=r[i]['municipio']
                break


        ent=TRX.addEntity('maltego.Location', municipio)
        ent.addAdditionalFields("country", "Country", True, "Colombia")
        ent.addAdditionalFields("area", "Area", True, municipio)

    except Exception as e:
        TRX.addUIMessage("Cedula no encontrada en la base de datos")

    TRX.returnOutput()


