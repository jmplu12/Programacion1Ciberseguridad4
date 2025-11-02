//18.	3. Ingrese un carácter y muestre su código ASCII.

Algoritmo MostrarCodigoASCII
	Definir caracter Como Cadena
	Definir codigoAscii, i Como Entero
	Definir alfabeto Como Cadena
	codigoAscii <- 0
	alfabeto <- 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	Escribir 'Ingrese un carácter:'
	Leer caracter
	// Verifica si es mayúscula
	Para i<-0 Hasta Longitud(alfabeto)-1 Hacer
		Si Subcadena(alfabeto,i+1,i+1)=Mayusculas(caracter) Entonces
			codigoAscii <- i+65
		FinSi // ASCII de 'A' es 65
	FinPara
	Si codigoAscii=0 Entonces
		Para i<-0 Hasta Longitud(alfabeto)-1 Hacer
			Si Subcadena(alfabeto,i+1,i+1)=Minusculas(caracter) Entonces
				codigoAscii <- i+97
			FinSi // ASCII de 'a' es 97
		FinPara
	FinSi
	Si codigoAscii<>0 Entonces
		Escribir 'El código ASCII de ', caracter, ' es: ', codigoAscii
	SiNo
		Escribir 'El carácter no es una letra.'
	FinSi
FinAlgoritmo
