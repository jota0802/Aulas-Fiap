#Dados para inserir

Sexo = str(input("Coloque H caso seja Homem, e M caso seja Mulher:  "))

Peso = float(input("Insira seu Peso em Kg:  "))
Altura = float(input("Insira sua Altura em Metros:  "))
Idade = int(input("Insira sua Idade:  "))

#Calculo de IMC

IMC = Peso / (Altura * Altura)
if IMC < 17:
    print("Muito abaixo do peso recomendado")
elif IMC < 18.4:
    print ("Abaixo do peso recomendado")
elif IMC < 24.9: 
    print ("Peso normal")
elif IMC < 29.9:
    print("Sobrepeso")
elif IMC < 34.9:
    print ("Obesidade Grau I")
elif IMC < 39.9:
    print ("Obesidade Grau II")
else:
    print ("Obesidade Grau III")

print("")

print (f"Seu IMC é: {IMC:.2f}")

print("")

#Calculo da taxa metaólica

#Formula Maculina
Taxa_Meta_M = 66.5 + (13.75 * Peso) + (500.3 * Altura) - (6.775 * Idade)

#Formula Feminina
Taxa_Meta_F = 655 + (9.56 * Peso) + (185 * Altura) - (4.7 * Idade)

#Condição para determinar o Sexo M ou F
if Sexo == "H":
    print ("Sua taxa metabolica tende a ser proxima de", round(Taxa_Meta_M),"Kcal")
elif Sexo == "M":
    print ("Sua taxa metabolica tende a ser proxima de", round(Taxa_Meta_F), "Kcal") 
print("")

#Calculo de Nutrientes

#Carboidratos
Carbo = round(5* Peso)
print("Seu consumo diário de carboidratos recomendados para uma disposição excelente são de",Carbo,"g")
print("")

#Proteinas
Proteina = round(1.2 * Peso)
Proteina2 = round(1.75 * Peso)
print("Seu consumo diário de proteínas recomendadas são de",Proteina,"g, e caso busque obter mais ganhos musculares são recomendados", Proteina2,"g de proteína")
print("")

#Gorduras
Gorduras = round(0.15 * Proteina)
Gorduras2 = round(0.25 * Proteina)
print ("O consumo de Gorduras/lipídios recomendados vão de no minimo", Gorduras,"g, até no maximo", Gorduras2, "g por dia ; *obs: os valores podem variar de acordo com sua dieta e objetivos")
print ("")

#Água
Água = (40 * Peso)
print("O consumo de Água diário ideal para uma boa hidratação são de aproximadamente",round(Água),"mL")
print("")

#Dietas feitas por IA
#Condiação de escolha da dieta baseada na proteina2, que corresponde a taxa de proteina recomendadas para ganhos musculares

DietaE = int(input("Escolha uma dieta de 1 a 5, sendo 5 a com mais valores proteicos e mais valores caloricos:  "))

if DietaE == 1:

    print("*Café da Manha: 2 ovos mexido ; 2 fatias de pão integral ; 1 colher de queijo cottage ; 1 copo de leite desnatado *Almoço: 100g de peito de frango grelhado (+- 1 filé) ; 1 porção de Arroz ; 1 porção Salada ou Vegetais")
    print("")
    print("**Lanche da tarde: 1 lata de atum em água ; 1 pão *Jantar: 120g de peito de frango (ou Salmão Grelhado) ; 1 batata doce assada ; 1 porção Salada ou Vegetais  *Lanche Noturno: 1 maçã")
    print("")
    print("*Total de proteínas: Aproximadamente 110g Total de calorias: Aproximadamente 1850 kcal.")

elif DietaE == 2:

    print("*Café da Manha: 2 ovos mexido ; 2 fatias de pão integral ; 1 colher de queijo cottage ; 1 xícara de leite desnatado *Almoço: 130g de peito de frango grelhado (+-2 filés) ; 1 porção de Arroz ; 1 porção Salada ou Vegetais")
    print("")
    print("*Lanche da tarde: 1 lata de atum em água ; 1 pão  *Jantar: 130g de peito de frango (ou Salmão Grelhado) ; 1 batata doce assada ; 1 porção Salada ou Vegetais  *Lanche Noturno: 1 porção de queijo cottage ; 1 maçã")
    print("")
    print("*Total de proteínas: Aproximadamente 130g Total de calorias: Aproximadamente 1900 kcal.")

elif DietaE == 3:

    print("*Café da Manha: 2 ovos mexido ; 2 fatias de pão integral ; 1 xícara de leite desnatado *Almoço: 150g de peito de frango grelhado (2 filés) ; 1 porção de Arroz com Feijão ; 1 porção Salada ou Vegetais")
    print("")
    print("*Lanche da tarde: 1 porção de Whey ; 1 pão ; 1 fatia de queijo  *Jantar: 150g de peito de frango ; 1 batata doce assada ; 1 porção Salada ou Vegetais  *Lanche Noturno: 1 Yogurte ; 1 maçã")
    print("")
    print("*Total de proteínas: Aproximadamente 140g Total de calorias: Aproximadamente 1950 kcal.")

elif DietaE == 4:

    print("*Café da Manha: 2 ovos mexido ; 2 fatias de pão integral ; 1 xícara de leite desnatado ; 1 Banana *Almoço: 150g de peito de frango grelhado (2 filés) ; 1 porção de Arroz com Feijão ; 1 porção Salada ou Vegetais")
    print("")
    print("*Lanche da tarde: 1 porção de Whey ; 1 pão ; 1 fatia de queijo ; 1 mix de castanhas *Jantar: 150g de peito de frango ; 2 batata doce assada ; 1 porção Salada ou Vegetais  *Lanche Noturno: 1 Yogurte ; 1 maçã ")
    print("")
    print("*Total de proteínas: Aproximadamente 150g Total de calorias: Aproximadamente 2100 kcal.")

elif DietaE == 5:

    print ("Café da Manha: 3 ovos mexido ; 2 fatias de pão integral ; 1 xícara de leite desnatado ; 1 Banana ; 1 yogurte *Almoço: 150g de peito de frango grelhado (2 files) ; 1 porção de Arroz ; 1 porção Salada ou Vegetais")
    print("")
    print("*Lanche da tarde: 1 porção de Whey ; 1 pão ; 1 fatia de queijo ; 1 mix de castanhas ; 1 maça *Jantar: 150g de peito de frango ; 2 batata doce assada ; 1 porção Salada ou Vegetais  *Lanche Noturno: 1 Yogurte ou 1 copo de leite")
    print("")
    print("*Total de proteínas: Aproximadamente 165g Total de calorias: Aproximadamente 2200 kcal.")

else:
    print("procure um nutricionista...")

print("")

# Caminhada
Cam = float(60* Peso * 5)/100

# Musculação
Musc = float(60 * Peso * 9)/100
ConsumoPratM= Musc + Cam

#Porcentagem da queima calorica em uma dieta de 2000kcal
Porcentagem = (round(ConsumoPratM)/20)

#operação de diferença !=

print("Você ao praticar 1 hora de Musculação gasta em torno", round(Musc), "kcal, e entorno de", round(Cam),"kcal em uma caminhada tranquila por 1 hora")
print("")
print("na soma dessas duas atividades você gastaria proximo de",round(ConsumoPratM),"kcal, e isso representa", round(Porcentagem),"% da quantidade de uma dieta com 2000 kcal")