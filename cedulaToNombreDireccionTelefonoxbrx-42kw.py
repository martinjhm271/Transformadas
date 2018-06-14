#!/usr/bin/env python
# -*- coding: cp1252 -*-
from Maltego import *
from MaltegoTransform import *
import pandas as pd
from sodapy import Socrata




def CedulaToNombreDireccionTelefonoxbrx_42kw(m):

    TRX = MaltegoTransform()
    #TRX.parseArguments(sys.argv)
    #cedula=sys.argv[1]
    cedula=m.Value
    try:
        client = Socrata("www.datos.gov.co", None)
        r = client.get("xbrx-42kw", limit=2000)
        #for key, value in data.items():
            #print key, value
        for i in range(len(r)):
            if ( r[i]['documento_de_identidad'] ==  cedula) :
                barrio=r[i]['barrio']
                direccion=r[i]['direcci_n']
                nombre = r[i]['nombres']
                telefono = r[i]['tel_fono']
                break

        ent = TRX.addEntity('maltego.Person', nombre)
        ent.addAdditionalFields("person.firtsnames", "Firts Names", True, nombre)
        ent.addAdditionalFields("person.lastname", "Surname", True, "")

        ent2 = TRX.addEntity('maltego.PhoneNumber', telefono)
        ent2.addAdditionalFields("phonenumber.countrycode", "Country Code", True, "57")

        ent4 = TRX.addEntity('maltego.Location', direccion)
        ent4.addAdditionalFields("country", "Country", True, "Colombia")
        ent4.addAdditionalFields("location.area", "Area", True, barrio)
        ent4.addAdditionalFields("streetaddress", "Street Address", True, direccion)

    except Exception as e:
        TRX.addUIMessage("Cedula no encontrada en la base de datos")

    TRX.returnOutput()


