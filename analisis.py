#calculo de la media
def calcular_media(lista):
	return sum(lista)/len(lista)

#contador mayor que umbral
def contar_mayores(lista,umbral):
	contador= 0
	for t in lista:
		if t > umbral:
			contador+=1
	return contador

#clasificar temperturas
def clasificar_temperaturas(t):
	if t<20:
		return "frio"
	elif t<=22:
		return "templado"
	else:
		return "calor"

#resumen_temperaturas
def resumen_temperaturas(lista):
	resumen=[]
	for t in lista:
		etiqueta=clasificar_temperaturas(t)
		resumen.append((t,etiqueta))
	return resumen




