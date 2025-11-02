// 15.5. Ingrese una palabra y muestre su primera y última letra.
Algoritmo PrimeraUltimaLetra
	Definir palabra Como Cadena
	Definir primera, ultima Como Cadena
	Definir cantidad Como Entero
	Escribir 'Ingrese una palabra:'
	Leer palabra
	cantidad <- Longitud(palabra)
	Si cantidad>0 Entonces
		primera <- SubCadena(palabra,1,1)
		ultima <- SubCadena(palabra,cantidad,cantidad)
		Escribir 'Primera letra: ', primera
		Escribir 'Última letra: ', ultima
	SiNo
		Escribir 'No ingresó una palabra válida.'
	FinSi
FinAlgoritmo
