//22.	2. Mostrar la tabla de multiplicar de un número ingresado (del 1 al 10).
Proceso tablaMultiplicar
	Definir numero, resultado Como Entero
	Escribir "Ingrese un número:"
	Leer numero
	
	Para i <- 1 Hasta 10 Con Paso 1 Hacer
		resultado <- numero * i
		Escribir numero, " x ", i, " = ", resultado
	FinPara
FinProceso

