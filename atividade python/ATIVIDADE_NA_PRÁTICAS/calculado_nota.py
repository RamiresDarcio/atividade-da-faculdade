#entrada de dados 
primeiraNota = float(input("diginte a primeira nota:"))
sengudaNota = float(input("diginte senguda nota"))
treceiraNota = float(input("diginte treceira nota"))
#processamentos do codigo
suaMedia = (primeiraNota+sengudaNota+treceiraNota) /3 
if suaMedia >=7:
   print("aprovador")
else:
  print("reprovandor") 
#resutando final pode ser aprovador ou reprovando