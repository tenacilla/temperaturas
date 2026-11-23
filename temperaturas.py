temperaturas=[19, 20, 21, 22, 18, 23]

media=sum(temperaturas)/len(temperaturas)
maxima=max(temperaturas)
minima=min(temperaturas)

print (temperaturas)

print("La media de las temperaturas es de : ", media)
print("La maxima de las temperaturas es de : ", maxima)
print("La minima de las temperaturas es de : ", minima)


umbral_calor=30

if maxima>umbral_calor:
    print("Aviso! Se ha superado el umbral de calor: ",umbral_calor)
else:
    print("Todo en orden")

