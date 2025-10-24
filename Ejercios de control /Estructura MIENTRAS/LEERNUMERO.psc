//11.1. Leer números hasta que el usuario ingrese 0 y mostrar cuántos números ingresó.

Algoritmo LEERNUMERO
	Escribir "INTRODUZCA LOS NUMERROS QUE DESEE PERO EL SISTEMA NO SE DETENDRA HASTA QUE INTRODUZCA UN 0"
	Definir numero, contador Como Entero
    contador <- 0
	Escribir "Ingrese un número (0 para finalizar): "
	leer numero
	
	Mientras numero <> 0 Hacer
		contador <- contador + 1
        Leer numero
		Escribir "Los numero ingresados son: ", numero
	FinMientras
	Escribir "La cantidad de números ingresados es: ", contador
FinAlgoritmo
