# Este sera un conversor de DOLAR a QUETZALES

usd_valor_actual = 1 # Este valor no se modifica
qtm_valor_actual = 7.71 # Este valor se actualiza de manera Manual
imprimir = "El cambio de moneda actual es: \n" + str(usd_valor_actual) + " dolar \n" +str(qtm_valor_actual)+" quetzales \n"
print(imprimir)

cantidad_a_cambiar = int(input("Ingrese la cantidad de dolares a cambiar: "))
pregunta1 = "\nDesea cambiar " + str(cantidad_a_cambiar) + " dolares a quetzales?"
print(pregunta1)
pregunta2 = int(input("1 para covertir / 2 para detener: "))

resultado=0
if(pregunta2==1):
    resultado= qtm_valor_actual*cantidad_a_cambiar
    print("\nEl valor de " +str(cantidad_a_cambiar) + " dolares es de " + str(resultado) + " quetzales")
else:
    print("S\ne ha cancelado la operacion")