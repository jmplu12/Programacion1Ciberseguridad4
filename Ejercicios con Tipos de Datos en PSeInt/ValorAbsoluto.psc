// 10.5. Ingrese un número real y muestre su valor absoluto.
Algoritmo ValorAbsoluto
	Definir numero, absoluto Como Real
	Escribir 'Ingrese un número real:'
	Leer numero
	Si numero<0 Entonces
		absoluto <- numero*(-1)
	SiNo
		absoluto <- numero
	FinSi
	Escribir 'El valor absoluto es: ', absoluto
FinAlgoritmo
