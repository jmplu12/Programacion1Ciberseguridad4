//9.4. Según el tipo de operación (+, -, *, /), mostrar el resultado entre dos números.

Algoritmo sumaDosnumero
	Definir N1, N2 Como Entero
	Definir operacion Como Caracter
	Escribir "Introduzca Dos numeros"
	Leer N1, N2
	Escribir "Elija una operacion (+, -, *, /)"
	leer operacion
	
	Segun operacion Hacer
		"+":
			resultado <- N1 + N2
			Escribir "El Resultado de la suma es = ", resultado
			
		"-": 
			resultado <- N1 - N2
			Escribir "El Resultado de la resta es = ", resultado
			
		"*": 
			resultado <- N1 * N2
			Escribir "El Resultado de la multiplicacion es = ", resultado
			
		"/": 
			resultado <- N1 / N2
			Escribir "El Resultado de la divicion es = ", resultado
		De Otro Modo:
			Escribir "Elija los operadore que se le indica,(+, -, *, /)"
	FinSegun
	
	
FinAlgoritmo
