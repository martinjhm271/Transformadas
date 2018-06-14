#!/usr/bin/env python
# -*- coding: cp1252 -*-
from Maltego import *
from MaltegoTransform import *
import pandas as pd
from sodapy import Socrata


def CorreoToPersonDireccionTelefono_mk5f_bdwx(m):
    TRX = MaltegoTransform()
    #m.parseArguments(sys.argv)
    #email=sys.argv[1]
    email=m.Value
    try:
        client = Socrata("www.datos.gov.co", None)
        r = client.get("u5mc-hpr6", limit=2000)

        #for key, value in data.items():
            #print key, value
        for i in range(len(r)):
            if ( r[i]['correo_electronico'] == email) :
                celular= r[i]['celular']
                direccion=r[i]['direccion']
                celular2=r[i]['telefonos']
                barrio=r[i]['municipio']
                nombre = r[i]['nombre']
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
        ent2 = TRX.addEntity('maltego.PhoneNumber', celular)
        ent2.addAdditionalFields("phonenumber.countrycode", "Country Code", True, "57")
        ent3 = TRX.addEntity('maltego.PhoneNumber', celular2)
        ent3.addAdditionalFields("phonenumber.countrycode", "Country Code", True, "57")
        ent4 = TRX.addEntity('maltego.Location', direccion)
        ent4.addAdditionalFields("country", "Country", True, "Colombia")
        ent4.addAdditionalFields("location.area", "Area", True, barrio)
        ent4.addAdditionalFields("streetaddress", "Street Address", True, direccion)



    except Exception as e:
        TRX.addUIMessage("Cedula no encontrada en la base de datos")

    TRX.returnOutput()


