// 4.4. Solicite dos números e indique cuál es mayor.
Algoritmo NUMEROSESMAYOR1
	Definir num1, num2 Como Entero
	Escribir 'Ingrese el primer número:'
	Leer num1
	Escribir 'Ingrese el segundo número:'
	Leer num2
	Si num1>num2 Entonces
		Escribir num1, ' es mayor que ', num2
	SiNo
		Si num2>num1 Entonces
			Escribir num2, ' es mayor que ', num1
		SiNo
			Escribir 'Ambos números son iguales'
		FinSi
	FinSi
FinAlgoritmo
