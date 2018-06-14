#!/usr/bin/env python
# -*- coding: cp1252 -*-

from Maltego import *
from MaltegoTransform import *
import pandas as pd
from sodapy import Socrata


def CedulaToConsejal(m):
    TRX = MaltegoTransform()
    #TRX.parseArguments(sys.argv)
    cedula=m.Value
    #cedula=sys.argv[1]
    #cedula = '91457340'
    try:
        client = Socrata("www.datos.gov.co", None)
        r = client.get("gnvi-fbsz", limit=2000)
        #for key, value in data.items():
            #print key, value
        for i in range(len(r)):
            if ( r[i]['cc'] ==  cedula) :
                genero=r[i]['genero']
                partido = r[i]['partido_politico']
                municipio=r[i]['municipio']
                nombre_concejal=r[i]['nombre_concejal']
                break


        ent=TRX.addEntity('eci.Consejal', nombre_concejal)
        ent.addAdditionalFields("properity.genero", "Genero", True, genero)
        ent.addAdditionalFields("properity.partido", "Partido", True, partido)
        ent.addAdditionalFields("properity.municipio", "Municipio", True, municipio)
        ent.addAdditionalFields("properity.cedula", "Cedula", True, cedula)

    except Exception as e:
        TRX.addUIMessage("Cedula no encontrada en la base de datos")

    return TRX.returnOutput()


