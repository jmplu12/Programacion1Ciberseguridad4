//24.	4. Contar cuántos números pares hay entre 1 y 20.

Proceso contarPares
	Definir contador Como Entero
	contador <- 0
	
	Para i <- 1 Hasta 20 Con Paso 1 Hacer
		Si i MOD 2 = 0 Entonces
			contador <- contador + 1
		FinSi
	FinPara
	
	Escribir "Cantidad de números pares entre 1 y 20: ", contador
FinProceso
