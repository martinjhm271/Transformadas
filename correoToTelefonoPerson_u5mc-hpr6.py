#!/usr/bin/env python
# -*- coding: cp1252 -*-
from Maltego import *
from MaltegoTransform import *
import pandas as pd
from sodapy import Socrata


def CorreoToTelefonoPerson_u5mc_hpr6(m):

    TRX = MaltegoTransform()
    #m.parseArguments(sys.argv)
    #correo=sys.argv[1]
    correo=m.Value
    try:
        client = Socrata("www.datos.gov.co", None)
        r = client.get("u5mc-hpr6", limit=2000)

        #for key, value in data.items():
            #print key, value
        for i in range(len(r)):
            if ( r[i]['correo_electr_nico'] == correo) :
                nombre= r[i]['nombre']
                telefono= r[i]['celular']
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
        ent2 = TRX.addEntity('maltego.PhoneNumber', telefono)
        ent2.addAdditionalFields("phonenumber.countrycode", "Country Code", True, "57")



    except Exception as e:
        TRX.addUIMessage("Cedula no encontrada en la base de datos")

    TRX.returnOutput()


