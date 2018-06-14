import urllib
from Maltego import *
from MaltegoTransform import *

from selenium import webdriver
from PIL import ImageTk, Image
import time
import tkinter as tk
import sys
from selenium.webdriver.common.keys import Keys

# user = "H4sIAAAAAAAAAJWUT0hUQRzHZ3fdNF3FFIOIrc1EyPKpUBBoKIbWI81IXUMPNrtv2n3b7JtxZt7uE0nqUEF16FC3oKCOduoUeJHOBkl1qEvUITrUIYLADvV7b/+6aX8Gdubx3u83v8/v+/v9dukzCnIp0I4UzmDNVibVTmKZHMU8WP1m5dnO8y8CKKCj+jiOJ8lszFRpLC8Oo1rKsDGM44oJHW1XSUFkklHD4T9h9Q8gd4WyNbA3ws+vUAjHCVd4jCuTWbZAzTMjXkSKrYQ2FkuRuOq9/fzc/UZ5gPoRcgRqrPyOSsvhsFXZc2gRBdz7i0/B4pOv9BXS64yztCZtS7sAHNLbKVFSI1SbwIlRopLMGHI4pCGBLx/FF/JAdrkgjmtaaYebvrUNfphTOeDmol3J4uHVG+Nfp9f6XAuXpwpY2plIaKkYk1LLEmq4DlNwVl4eC6+8XG8PRfzIN4JqDOBNYEUU2u0J53QR2lXp0gsUPRW3eyWFEMNMZLEwTOu3bN8+bfmxemt5ucBYJ929AUj3FlTbJHc9zWmtePJ6pj+cCRU8sxrq2L+ALUXixCBwyEGCLS1X+wki0qbF5IgpFbGIuIRQZSOMKwGAvY/Xoh8/hRdO+POV9inUmhM3Vz6Sgbu1KKY2OZ4EPzLkvuDcyU6hyS7TMoijOUmVppGBI92Heg53RzIl20L4Y63/Ttrq5DUp7c3Zvv/KtaGUZZSZhtedLW6XATbnvNit1YsCdZQnCzXgzHITntR1i9uq7YxgnAg1f4rMy8JENHktWBZkyLLT5R+97lOonrI4pp504zAAhcH3XAYZo5DCakRcfnVv/Qs03jQKesrlvNGie4SV99I0PBn2+YD34Fa8Y7b6E7B7wR6Vj5ERqCoDymwYc85zUUAlsEvNmkbPZlPPyxUMAFHnVkRRk2TPMvZXpm0US6UbGwXSocoJIpreP3j0/cr1oyCQXhBow//VaTsdI+La0t1w3Z13N4uzDxGiUO1f+XLW2XMFAAA="


def ReCapcha(m):
    TRX = MaltegoTransform()
    #m.parseArguments(sys.argv)
    #cedulaTg = sys.argv[1]
    # cedulaTg = 1026585645
    cedulaTg=m.Value
    nombre = ""


    def get_captcha(driver, element, path):
        # now that we have the preliminary stuff out of the way time to get that image :D
        location = element.location
        size = element.size
        # saves screenshot of entire page
        driver.save_screenshot(path)

        # uses PIL library to open image in memory
        image = Image.open(path)

        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']

        image = image.crop((left, top, right, bottom))  # defines crop points
        image.save(path, 'png')  # saves new cropped image


    try:

        driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
        driver.set_window_position(-3000, 0)
        driver.get("https://antecedentes.policia.gov.co:7005/WebJudicial/index.xhtml")
        aceptaOption = driver.find_element_by_id("aceptaOption:0")
        driver.execute_script("arguments[0].click();", aceptaOption)
        bandera = True

        while (bandera):
            try:
                continuarBtn = driver.find_element_by_name("continuarBtn")
                continuarBtn.click()
                bandera = False
            except Exception:
                m.addUIMessage("Cedula no encontrada en la base de datos1")
        bandera = True
        while (bandera):
            try:
                cedula = driver.find_element_by_id("cedulaInput")
                cedula.send_keys(cedulaTg)
                bandera = False
            except Exception:
                m.addUIMessage("Cedula no encontrada en la base de datos2")
        time.sleep(2)
        # driver.switch_to.default_content()
        image = driver.find_elements_by_xpath("//img[@id='capimg']")[0]
        get_captcha(driver, image, "captcha.png")

        window = tk.Tk()
        window.title("Enter Captcha")
        window.geometry("140x120")
        window.configure(background='grey')

        path = "captcha.png"

        # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        img = ImageTk.PhotoImage(Image.open(path))

        # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        panel = tk.Label(window, image=img).grid(row=0)

        # The Pack geometry manager packs widgets in rows or columns.
        # panel.pack(side = "bottom", fill = "both", expand = "yes")

        e1 = tk.Entry(window)

        e1.grid(row=1, column=0)

        tk.Button(window, text='Aceptar', command=window.quit).grid(row=3, column=0, pady=4)
        # Start the GUI
        window.mainloop()

        textcaptcha = driver.find_element_by_id("textcaptcha")
        textcaptcha.send_keys(e1.get())

        bandera = True
        while (bandera):
            try:
                j_idt20 = driver.find_element_by_name("j_idt20")
                j_idt20.click()
                bandera = False
            except Exception:
                m.addUIMessage("Cedula no encontrada en la base de datos3")

        bandera = True

        while (bandera):
            try:
                nombre = driver.find_elements_by_xpath('.//span[@id = "form:mensajeCiudadano"]/b')[2].text
                antecedentes = driver.find_elements_by_xpath('.//span[@id = "form:mensajeCiudadano"]/b')[3].text
                bandera = False
            except Exception:
                TRX.addUIMessage('Cedula no encontrada4')

        ent = TRX.addEntity('eci.AntecedentesPersonales', antecedentes.encode('utf8'))
        ent.addAdditionalFields("properity.eci.nombre", "Nombre", True, nombre.encode('utf8'))

    except Exception:
        TRX.addUIMessage("Cedula no encontrada en la base de datos")
    driver.quit()
    TRX.returnOutput()
