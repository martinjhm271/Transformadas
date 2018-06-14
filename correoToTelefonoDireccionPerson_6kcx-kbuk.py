#!/usr/bin/env python
# -*- coding: cp1252 -*-
from Maltego import *
from MaltegoTransform import *
import pandas as pd
from sodapy import Socrata


def CorreoToTelefonoDireccionPerson_6kcx_kbuk(m):
    TRX = MaltegoTransform()
    #m.parseArguments(sys.argv)
    #email=sys.argv[1]
    email=m.Value
    try:
        client = Socrata("www.datos.gov.co", None)
        r = client.get("6kcx-kbuk", limit=2000)

        #for key, value in data.items():
            #print key, value
        for i in range(len(r)):
            if ( r[i]['correo_electronico'] == email) :
                cc=r[i]['doc_identidad']
                nombre=r[i]['nombre_concejal']
                partido=r[i]['partido_politico']
                celular= r[i]['celular']
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
        ent1 = TRX.addEntity('maltego.PhoneNumber', celular)
        ent1.addAdditionalFields("phonenumber.countrycode", "Country Code", True, "57")
        ent2 = TRX.addEntity('eciescuelaing.PartidoPolitico', partido)
        ent3 = TRX.addEntity('eci.Cedula', cc)





    except Exception as e:
        TRX.addUIMessage("Cedula no encontrada en la base de datos")

    TRX.returnOutput()


