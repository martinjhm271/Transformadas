#!/usr/bin/env python
# -*- coding: cp1252 -*-
from Maltego import *
from MaltegoTransform import *
import pandas as pd
from sodapy import Socrata

def TelefonoToCorreoDireccionPerson_mk5f_bdwx(m):
    TRX = MaltegoTransform()
    #m.parseArguments(sys.argv)
    #telefono=sys.argv[1]
    telefono=m.Value
    try:
        client = Socrata("www.datos.gov.co", None)
        r = client.get("u5mc-hpr6", limit=2000)

        #for key, value in data.items():
            #print key, value
        for i in range(len(r)):
            if ( r[i]['celular'] == telefono or  r[i]['telefonos'] == telefono) :
                nombre=r[i]['nombre']
                correo_electronico= r[i]['correo_electronico']
                direccion=r[i]['direccion']
                barrio=r[i]['municipio']
                break

        nombre = nombre.split(" ")
        if (len(nombre) == 4):
            firts = nombre[0] + " " + nombre[1]
            last = nombre[2] + " " + nombre[3]
            full = nombre[0] + " " + nombre[1] + " " + nombre[2] + " " + nombre[3]
        else:
            firts = nombre[0]
            last = nombre[1] + " " + nombre[2]
            full = nombre[0] + " " + nombre[1] + " " + nombre[2]

        ent = TRX.addEntity('maltego.Person', full)
        ent.addAdditionalFields("person.firtsnames", "Firts Names", True, firts)
        ent.addAdditionalFields("person.lastname", "Surname", True, last)
        ent1 = TRX.addEntity('maltego.EmailAddress', correo_electronico)
        ent4 = m.addEntity('maltego.Location', direccion)
        ent4.addAdditionalFields("country", "Country", True, "Colombia")
        ent4.addAdditionalFields("location.area", "Area", True, barrio)
        ent4.addAdditionalFields("streetaddress", "Street Address", True, direccion)



    except Exception as e:
        TRX.addUIMessage("Cedula no encontrada en la base de datos")

    TRX.returnOutput()


