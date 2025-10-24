//17.2. Solicitar contraseñas hasta que el usuario ingrese la correcta ('admin123').

Algoritmo lOGEO
	Definir clave, contrasena Como Caracter
	
	clave <- "admin123"
	
	Repetir
		Escribir "Introduzca su contraseña correcta"
		Leer contrasena
		si contrasena <> clave Entonces
			Escribir "La contaseña es incorrecta"
			
		FinSi
	Hasta Que contrasena = clave
	Escribir "La contraseña es correcta"
	
FinAlgoritmo
