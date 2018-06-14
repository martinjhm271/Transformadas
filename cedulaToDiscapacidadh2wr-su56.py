#!/usr/bin/env python
# -*- coding: cp1252 -*-



from Maltego import *
from MaltegoTransform import *
import pandas as pd
from sodapy import Socrata



def CedulaToDiscapacidadh2wr_su56(m):
    TRX = MaltegoTransform()
    #m.parseArguments(sys.argv)
    #cedula=sys.argv[1]
    cedula=m.Value
    try:
        client = Socrata("www.datos.gov.co", None)
        r = client.get("h2wr-su56", limit=2000)
        #for key, value in data.items():
            #print key, value
        for i in range(len(r)):
            tempid=r[i]['identificacion'].replace(",","")
            tempid=tempid.replace(".","")
            tempid = tempid.replace("T.I.", "")
            tempid = tempid.replace("NUIP ", "")
            if ( tempid ==  cedula) :
                direccion=r[i]['direccion']
                discapacidad = r[i]['discapacidad']
                fecha=r[i]['fecha_de_nacimiento']
                nombres=r[i]['nombres_y_apellidos']
                break

        ent = TRX.addEntity('maltego.Person', nombres)
        ent.addAdditionalFields("person.firtsnames", "Firts Names", True, nombres)
        ent.addAdditionalFields("person.lastname", "Surname", True, "")

        ent2 = TRX.addEntity('eci.Discapacidad', discapacidad)
        ent2.addAdditionalFields("fechaNacimiento", "Born Date", True, fecha)

        ent4 = TRX.addEntity('maltego.Location', direccion)
        ent4.addAdditionalFields("country", "Country", True, "Colombia")
        ent4.addAdditionalFields("location.area", "Area", True, "")
        ent4.addAdditionalFields("streetaddress", "Street Address", True, direccion)

    except Exception as e:
        TRX.addUIMessage("Nombre no encontrado en la base de datos")

    TRX.returnOutput()


