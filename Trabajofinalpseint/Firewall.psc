Algoritmo Firewall
	// aqui Declare las  variables necesarias para manejar las IPs bloqueadas y los paquetes entrantes.
	Definir bloqueadas Como Cadena
	Definir paquetes Como Cadena
	Definir i, j, bloqueado Como Entero
	// se definio el tamaño de los arreglos para evitar errores de subíndices fuera de rango.
	Dimensionar bloqueadas(3)
	Dimensionar paquetes(3,3)
	// Entrada de datos: se solicitan las IPs que se desean bloquear (máximo 3).
	// con este para, hasta que no llegue a 3 seguira pidiendo que ingrese la dirrecion ip que sea bloquear
	Para i<-1 Hasta 3 Hacer
		Escribir 'Ingresa IP bloqueada #', i
		Leer bloqueadas[i]
	FinPara
	// Entrada de datos: se registran las características de cada paquete entrante.
	// aqui es el mismo proceso hasta que no llegue a 3 se registrara los paques y la ip de origen
	Para i<-1 Hasta 3 Hacer
		Escribir 'Paquete #', i
		Escribir 'Ingresa IP de origen:'
		Leer paquetes[i,1]
		Escribir 'Ingresa puerto destino:'
		Leer paquetes[i,2]
		Escribir 'Ingresa protocolo:'
		Leer paquetes[i,3]
	FinPara
	// Proceso de validación: se verifica para cada paquete si la IP de origen está en la lista de bloqueadas.
	Para i<-1 Hasta 3 Hacer
		bloqueado <- 0
		Para j<-1 Hasta 3 Hacer // Inicialización del estado: paquete permitido por defecto.
			Si paquetes[i,1]=bloqueadas[j] Entonces
				bloqueado <- 1
			FinSi // Se marca como bloqueado si coincide la IP con alguna bloqueada.
		FinPara
		// Resultado: mostrar si el paquete es permitido o bloqueado.
		Si bloqueado=1 Entonces
			Escribir 'Paquete ', i, ': BLOQUEADO (IP: ', paquetes[i,1], ')'
		SiNo
			Escribir 'Paquete ', i, ': PERMITIDO (IP: ', paquetes[i,1], ')'
		FinSi
	FinPara
FinAlgoritmo
