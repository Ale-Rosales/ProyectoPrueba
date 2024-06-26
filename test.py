import pywhatkit

class Test:

    def Prueba(self, hora, minutos):

        try: 
            
            pywhatkit.sendwhatmsg("+50242785124",  
                                    "Mensaje De Prueba",
                                    hora,minutos) 

            print("Mensaje Enviado") 

        except: 
            print("Ocurrio Un Error")