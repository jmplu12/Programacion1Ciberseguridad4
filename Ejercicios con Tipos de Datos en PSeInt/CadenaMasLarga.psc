// 14.4. Ingrese dos cadenas y muestre cuál es más larga.
Algoritmo CadenaMasLarga
	Definir cadena1, cadena2 Como Cadena
	Definir largo1, largo2 Como Entero
	Escribir 'Ingrese la primera cadena:'
	Leer cadena1
	Escribir 'Ingrese la segunda cadena:'
	Leer cadena2
	largo1 <- Longitud(cadena1)
	largo2 <- Longitud(cadena2)
	Si largo1>largo2 Entonces
		Escribir 'La primera cadena es más larga.'
	SiNo
		Si largo2>largo1 Entonces
			Escribir 'La segunda cadena es más larga.'
		SiNo
			Escribir 'Ambas cadenas tienen la misma longitud.'
		FinSi
	FinSi
FinAlgoritmo
