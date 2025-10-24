//12.	2. Contar cuántos números positivos 
//se ingresan antes de ingresar un número negativo.

Proceso ContarPositivos
    Definir numero, contador Como Entero
    contador <- 0
	
    Escribir "Ingrese un número (negativo para finalizar): "
    Leer numero
	
    Mientras numero >= 0 Hacer
        Si numero > 0 Entonces
            contador <- contador + 1
        FinSi
		
        Escribir "Ingrese otro número (negativo para finalizar): "
        Leer numero
    FinMientras
	
    Escribir "La cantidad de números positivos ingresados es: ", contador
FinProceso
