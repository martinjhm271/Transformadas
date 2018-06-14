#!/usr/bin/env python
# -*- coding: cp1252 -*-
from Maltego import *
from MaltegoTransform import *
import pandas as pd
from sodapy import Socrata


def PersonToTelefonoCorreo_u5cm_hpr6(m):
    TRX = MaltegoTransform()
    #m.parseArguments(sys.argv)
    #person=sys.argv[1]
    person=m.Value
    try:
        client = Socrata("www.datos.gov.co", None)
        r = client.get("u5mc-hpr6", limit=2000)

        #for key, value in data.items():
            #print key, value
        for i in range(len(r)):
            if ( r[i]['nombre'] == person) :
                celular= r[i]['celular']
                email= r[i]['correo_electr_nico']
                break

        ent = TRX.addEntity('maltego.PhoneNumber', celular)
        ent.addAdditionalFields("phonenumber.countrycode", "Country Code", True, "57")
        ent2 = TRX.addEntity('maltego.EmailAddress', email)


    except Exception as e:
        TRX.addUIMessage("Cedula no encontrada en la base de datos")

    TRX.returnOutput()


