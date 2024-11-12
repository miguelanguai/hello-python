gas = True
encendido = True
edad = 18

if gas and encendido:
    print("Puedes avanzar")
    
if gas or encendido:
    print("Puedes ir")
    
if not gas or encendido:
    print("Puedes continuar")
    
if not gas and encendido:
    print("Puedes seguir")
    
if gas and (encendido or edad > 17):
    print("Puedes avanzar")
    
if gas and encendido and edad > 17:
    print("Puedes avanzar")
    
