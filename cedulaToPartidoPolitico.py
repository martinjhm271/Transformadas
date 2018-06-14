#!/usr/bin/env python
# -*- coding: cp1252 -*-



from Maltego import *
from MaltegoTransform import *
import pandas as pd
from sodapy import Socrata



def CedulaToPartidoPolitico(m):
    TRX = MaltegoTransform()
    #m.parseArguments(sys.argv)
    #cedula=sys.argv[1]
    cedula=m.Value
    partido=""
    try:
        client = Socrata("www.datos.gov.co", None)
        r = client.get("gnvi-fbsz", limit=2000)
        #for key, value in data.items():
            #print key, value
        for i in range(len(r)):
            if ( r[i]['cc'] ==  cedula) :
                partido = r[i]['partido_politico']
                break
        ent=TRX.addEntity('eciescuelaing.PartidoPolitico', partido)

    except Exception as e:
        TRX.addUIMessage("Cedula no encontrada en la base de datos")

    TRX.returnOutput()


