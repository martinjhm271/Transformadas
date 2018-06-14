#!/usr/bin/env python
# -*- coding: cp1252 -*-
from Maltego import *
from MaltegoTransform import *
import pandas as pd
from sodapy import Socrata


def EmailToTelefonoDirection_6hgq_bdxw(m):
    TRX = MaltegoTransform()
    #m.parseArguments(sys.argv)
    #email=sys.argv[1]
    email=m.Value
    try:
        client = Socrata("www.datos.gov.co", None)
        r = client.get("6hgq-bdxw", limit=2000)

        #for key, value in data.items():
            #print key, value
        for i in range(len(r)):
            correos=r[i]['correo_electronico']
            correos=correos.split(";")
            if ( email in correos) :
                telefono=r[i]['telefonos']
                dir=r[i]['direccion']
                break

        ent = TRX.addEntity('maltego.PhoneNumber', telefono)
        ent.addAdditionalFields("phonenumber.countrycode", "Country Code", True, "57")
        ent2 = TRX.addEntity('maltego.Location', dir)
        ent2.addAdditionalFields("country", "Country", True, "Colombia")
        ent2.addAdditionalFields("streetaddress", "Street Address", True, dir)


    except Exception as e:
        TRX.addUIMessage("Cedula no encontrada en la base de datos")

    TRX.returnOutput()


