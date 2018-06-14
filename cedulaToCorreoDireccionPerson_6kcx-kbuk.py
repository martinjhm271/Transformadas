#!/usr/bin/env python
# -*- coding: cp1252 -*-
from Maltego import *
from MaltegoTransform import *
import pandas as pd
from sodapy import Socrata


def CedulaToCorreoDireccionPerson_6kcx_kbuk(m):
    TRX = MaltegoTransform()
    #m.parseArguments(sys.argv)
    cedula=m.Value
    try:
        client = Socrata("www.datos.gov.co", None)
        r = client.get("6kcx-kbuk", limit=2000)

        #for key, value in data.items():
            #print key, value
        for i in range(len(r)):
            if ( r[i]['doc_identidad'] == cedula) :
                celular=r[i]['celular']
                nombre=r[i]['nombre_concejal']
                partido=r[i]['partido_politico']
                correo_electronico= r[i]['correo_electronico']
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
        ent2 = TRX.addEntity('eciescuelaing.PartidoPolitico', partido)
        ent3 = TRX.addEntity('maltego.PhoneNumber', celular)
        ent3.addAdditionalFields("phonenumber.countrycode", "Country Code", True, "57")





    except Exception as e:
        TRX.addUIMessage("Cedula no encontrada en la base de datos")

    TRX.returnOutput()


