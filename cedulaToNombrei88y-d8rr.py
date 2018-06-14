#!/usr/bin/env python
# -*- coding: cp1252 -*-
from Maltego import *
from MaltegoTransform import *
import pandas as pd
from sodapy import Socrata



def CedulaToNombrei88y_d8rr(m):
    TRX = MaltegoTransform()
    #m.parseArguments(sys.argv)
    #cedula=sys.argv[1]
    cedula=m.Value
    try:
        client = Socrata("www.datos.gov.co", None)
        r = client.get("i88y-d8rr", limit=2000)

        #for key, value in data.items():
            #print key, value
        for i in range(len(r)):
            if ( r[i]['cedula'] == cedula) :
                nombres=r[i]['nombre']
                apellidos=r[i]['apellidos']
                full=nombres+" "+apellidos
                break



        ent = TRX.addEntity('maltego.Person', full)
        ent.addAdditionalFields("person.firtsnames", "Firts Names", True, nombres)
        ent.addAdditionalFields("person.lastname", "Surname", True, apellidos)


    except Exception as e:
        TRX.addUIMessage("Cedula no encontrada en la base de datos")

    TRX.returnOutput()


