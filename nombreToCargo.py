#!/usr/bin/env python
# -*- coding: cp1252 -*-



from Maltego import *
from MaltegoTransform import *
import pandas as pd
from sodapy import Socrata



def NombreToCargo(m):
    TRX = MaltegoTransform()
    #m.parseArguments(sys.argv)
    #nombre=sys.argv[1]
    nombre=m.Value
    try:
        client = Socrata("www.datos.gov.co", None)
        r = client.get("2gvv-khi3", limit=2000)
        #for key, value in data.items():
            #print key, value
        for i in range(len(r)):
            if ( r[i]['nombre'] ==  nombre.upper()) :
                cargo=r[i]['cargo']
                direccion = r[i]['direccion']
                email=r[i]['email']
                telefono=r[i]['telefono']
                break


        ent=TRX.addEntity('eci.Cargo', cargo)
        ent.addAdditionalFields("properity.direccion", "Direccion", True, direccion)
        ent.addAdditionalFields("properity.email", "Email", True, email)
        ent.addAdditionalFields("properity.telefono", "Telefono", True, telefono)

    except Exception as e:
        TRX.addUIMessage("Nombre no encontrado en la base de datos")

    TRX.returnOutput()


