//4.4. Escriba un algoritmo que indique si un número es positivo, negativo o cero.

Algoritmo NumeroNegativoPositivoOcero
	Escribir "Determinar si un numero es negativo, positivo o es cero"
	definir numero Como Entero
	Escribir "Introduzca un numero"
	Leer numero
	
	si numero > 0 Entonces
		Escribir "El numero es positivo"
		
		Si numero < 0 Entonces 
			Escribir "El numero es Negativo"
		FinSi
		Si numero == 0 Entonces 
			Escribir "El numero es Cero"
		FinSi
	FinSi
	
	
FinAlgoritmo
