Algoritmo VocalOConsonante
	Definir letra Como Cadena
	Escribir 'Ingrese una letra:'
	Leer letra
	letra <- Minusc[letra]
	Si letra='a' O letra='e' O letra='i' O letra='o' O letra='u' Entonces // Convierte a minúscula para simplificar comparación
		Escribir 'La letra es una vocal.'
	SiNo
		Si letra>='b' Y letra<='z' Entonces
			Escribir 'La letra es una consonante.'
		SiNo
			Escribir 'Entrada no válida. Por favor, ingrese una letra.'
		FinSi
	FinSi
FinAlgoritmo
