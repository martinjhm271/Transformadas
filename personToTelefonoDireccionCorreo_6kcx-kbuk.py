#!/usr/bin/env python
# -*- coding: cp1252 -*-
from Maltego import *
from MaltegoTransform import *
import pandas as pd
from sodapy import Socrata


def PersonToTelefonoDireccionCorreo_6kcx_kbuk(m):

    TRX = MaltegoTransform()
    #m.parseArguments(sys.argv)
    #nombre=sys.argv[1]
    nombre=m.Value
    try:
        client = Socrata("www.datos.gov.co", None)
        r = client.get("6kcx-kbuk", limit=2000)

        #for key, value in data.items():
            #print key, value
        for i in range(len(r)):
            if ( r[i]['nombre'] == nombre) :
                cc=r[i]['doc_identidad']
                partido=r[i]['partido_politico']
                celular= r[i]['celular']
                correo=r[i]['correo_electronico']
                break

        ent = TRX.addEntity('maltego.EmailAddress', correo)
        ent1 = TRX.addEntity('maltego.PhoneNumber', celular)
        ent1.addAdditionalFields("phonenumber.countrycode", "Country Code", True, "57")
        ent2 = TRX.addEntity('eciescuelaing.PartidoPolitico', partido)
        ent3 = TRX.addEntity('eci.Cedula', cc)





    except Exception as e:
        TRX.addUIMessage("Cedula no encontrada en la base de datos")

    TRX.returnOutput()


