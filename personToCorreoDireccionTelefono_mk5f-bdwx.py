#!/usr/bin/env python
# -*- coding: cp1252 -*-
from Maltego import *
from MaltegoTransform import *
import pandas as pd
from sodapy import Socrata


def PersonToCorreoDireccionTelefono_mk5f_bdwx(m):
    TRX = MaltegoTransform()
    #m.parseArguments(sys.argv)
    #nombre=sys.argv[1]
    nombre=m.Value
    try:
        client = Socrata("www.datos.gov.co", None)
        r = client.get("u5mc-hpr6", limit=2000)

        #for key, value in data.items():
            #print key, value
        for i in range(len(r)):
            if ( r[i]['nombre'] == nombre) :
                celular= r[i]['celular']
                correo_electronico= r[i]['correo_electronico']
                direccion=r[i]['direccion']
                celular2=r[i]['telefonos']
                barrio=r[i]['municipio']
                break


        ent1 = TRX.addEntity('maltego.EmailAddress', correo_electronico)
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


