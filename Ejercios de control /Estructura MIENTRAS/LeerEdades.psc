//13.	3. Leer edades hasta que se ingrese una edad fuera del rango 0-120.

Proceso LeerEdades
    Definir edad Como Entero
	
    Escribir "Ingrese una edad (si ingresa una edad fuera del rango 0-120 finaliza el sistema): "
    Leer edad
	
    Mientras edad >= 0 Y edad <= 120 Hacer
        Escribir "Edad válida: ", edad
        Escribir "Ingrese otra edad (fuera del rango 0-120 para finalizar): "
        Leer edad
    FinMientras
	
    Escribir "Edad fuera del rango detectada. Programa finalizado."
FinProceso

