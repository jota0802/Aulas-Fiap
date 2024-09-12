#Valor das Questões
lista_q = [4,2,3,2,3,3,2,2,3,3]

#Equipes
MER = [] #mudar para tudo minusculo
POR = []
AUD = []
DS  = []
NIS = []
BMW = []
JAG = []
VEN = []
MAH = []
NIO = []

Equipes = [MER,POR,AUD,DS,NIS,BMW,JAG,VEN,MAH,NIO]

Mer = " Mercedes-Benz " #mudar para tudo maiusculo
Por = " Porsche " 
Aud = " Audi "
Ds = " DS Automobil "
Nis = " Nissan "
Bmw = " BMW " 
Jag = " Jaguar "
Ven = " Venturi "
Mah = " Mahindra "
Nio = " NIO "


Pontos = [0,0,0,0,0,0,0,0,0,0,0]
Valor = [0,0,0,0,0,0,0,0,0,0]

#Questões
Quiz_Realizado = True

Q = ["Q1","Q2","Q3","Q4","Q5","Q6","Q7","Q8","Q9","Q10"]
while Quiz_Realizado:
    for j in range(0,10):
        Q[j] = True

    #Q1

    while Q[0]:
        print("")
        print("     1 - Qual marca de carro você mais admira ou tem afinidade?")
        print(" 1 - Mercedes-Benz","\n 2 - Porsche","\n 3 - Audi","\n 4 - DS Automobil","\n 5 - Nissan","\n 6 - BMW","\n 7 - Jaguar","\n 8 - Venturi","\n 9 - Mahindra","\n 10 - NIO")
        questão1 = int(input("Digite um Numero"))

        if questão1 == 1:
            if lista_q [0] in lista_q:
                MER.append(lista_q[0])
                break

        elif questão1 == 2:
            if lista_q [0] in lista_q:
                POR.append(lista_q[0])
                break

        elif questão1 == 3:
            if lista_q [0] in lista_q:
                AUD.append(lista_q[0])
                break

        elif questão1 == 4:
            if lista_q [0] in lista_q:
                DS.append(lista_q[0])
                break

        elif questão1 == 5:
            if lista_q [0] in lista_q:
                NIS.append(lista_q[0])
                break

        elif questão1 == 6:
            if lista_q [0] in lista_q:
                BMW.append(lista_q[0])
                break

        elif questão1 == 7:
            if lista_q [0] in lista_q:
                JAG.append(lista_q[0])
                break

        elif questão1 == 8:
            if lista_q [0] in lista_q:
                VEN.append(lista_q[0])
                break

        elif questão1 == 9:
            if lista_q [0] in lista_q:
                MAH.append(lista_q[0])
                break

        elif questão1 == 10:
            if lista_q [0] in lista_q:
                NIO.append(lista_q[0])
                break

        else:
            print("\n Numero invalido")

    #Q2

    while Q[1]:
        print("")
        print("     2 - O que mais te atrai na Fórmula E?")
        print("\n 1 - Inovação tecnológica","\n 2 - Sustentabilidade ambiental","\n 3 - Competição acirrada","\n 4 - História e tradição","\n 5 - Velocidade e desempenho")
        questão2 = int(input("Digite um Numero"))

        if questão2 == 1:
            if lista_q [1] in lista_q:
                MER.append(lista_q[1])
                POR.append(lista_q[1])
                AUD.append(lista_q[1])
                break
            
        elif questão2 == 2:
            if lista_q [1] in lista_q:
                NIS.append(lista_q[1])
                MAH.append(lista_q[1])
                break

        elif questão2 == 3:
            if lista_q [1] in lista_q:
                DS.append(lista_q[1])
                VEN.append(lista_q[1])
                break

        elif questão2 == 4:
            if lista_q [1] in lista_q:
                JAG.append(lista_q[1])
                break

        elif questão2 == 5:
            if lista_q [1] in lista_q:
                BMW.append(lista_q[1])
                break

        else:
            print("\n Numero Invalido")


    #Q3
    while Q[2]:
        print("")
        print("     3 - Qual é o seu estilo de vida preferido?") 
        print("\n 1 - Urbano e moderno","\n 2 - Aventureiro e arrojado ","\n 3 - Sofisticado e elegante ","\n 4 - Consciente e sustentável")
        questão3 = int(input("Digite um Numero"))

        if questão3 == 1:
            if lista_q [2] in lista_q:
                DS.append(lista_q[2])
                NIS.append(lista_q[2])
                break
            
        elif questão3 == 2:
            if lista_q [2] in lista_q:
                VEN.append(lista_q[2])
                NIO.append(lista_q[2])
                break

        elif questão3 == 3:
            if lista_q [2] in lista_q:
                JAG.append(lista_q[2])
                AUD.append(lista_q[2])
                BMW.append(lista_q[2])
                break

        elif questão3 == 4:
            if lista_q [2] in lista_q:
                MAH.append(lista_q[2])
                MER.append(lista_q[2])
                break

        else:
            print("\n Numero Invalido")


    #Q4
    while Q[3]:
        print("")
        print("     4 - Qual equipe de esportes motorizados você mais acompanha ou admira?")
        print("\n 1-Equipes da Fórmula 1", "\n 2-Equipes de endurance (WEC, Le Mans)", "\n 3-Equipes de rali (WRC, Dakar)","\n 4-Outros")
        questão4 = int(input("Digite um Numero"))

        if questão4 == 1:
            if lista_q [3] in lista_q:
                MER.append(lista_q[3])
                POR.append(lista_q[3])
                break
            
        elif questão4 == 2:
            if lista_q [3] in lista_q:
                AUD.append(lista_q[3])
                NIS.append(lista_q[3])
                break

        elif questão4 == 3:
            if lista_q [3] in lista_q:
                DS.append(lista_q[3])
                BMW.append(lista_q[3])
                break

        elif questão4 == 4:
            if lista_q [3] in lista_q:
                JAG.append(lista_q[3])
                VEN.append(lista_q[3])
                NIO.append(lista_q[3])
                MAH.append(lista_q[3])
                break

        else:
            print("\n Numero Invalido")


    #Q5
    
    while Q[4]:

        print("")
        print("     5 - Qual é o seu interesse em veículos elétricos?")
        print("\n 1-Tecnologia avançada","\n 2-Redução da pegada de carbono","\n 3-Desempenho e potência","\n 4-Economia de combustível")
        questão5 = int(input("Digite um Numero"))

        if questão5 == 1:
            if lista_q [4] in lista_q:
                MER.append(lista_q[4])
                POR.append(lista_q[4])
                AUD.append(lista_q[4])
                break
            
        elif questão5 == 2:
            if lista_q [4] in lista_q:
                MAH.append(lista_q[4])
                NIS.append(lista_q[4])
                break

        elif questão5 == 3:
            if lista_q [4] in lista_q:
                DS.append(lista_q[4])
                BMW.append(lista_q[4])
                break

        elif questão5 == 4:
            if lista_q [4] in lista_q:
                JAG.append(lista_q[4])
                VEN.append(lista_q[4])
                NIO.append(lista_q[4])
                break

        else:
            print("\n Numero Invalido")


    #Q6
    while Q[5]:
        print("")
        print("     6 - Você se identifica mais com equipes estabelecidas e tradicionais ou com novas equipes em ascensão?") 
        print("\n 1-Equipes estabelecidas e tradicionais","\n 2-Novas equipes em ascensão")
        questão6 = int(input("Digite um Numero"))

        if questão6 == 1:
            if lista_q [5] in lista_q:
                MER.append(lista_q[5])
                POR.append(lista_q[5])
                AUD.append(lista_q[5])
                JAG.append(lista_q[5])
                VEN.append(lista_q[5])
                DS.append(lista_q[5])
                BMW.append(lista_q[5])
                NIS.append(lista_q[5])
                break
            
        elif questão6 == 2:
            if lista_q [5] in lista_q:
                NIO.append(lista_q[5])
                MAH.append(lista_q[5])
                break

        else:
            print("\n Numero Invalido")

        
    #Q7

    while Q[6]:
        print("")
        print("     7 - Que tipo de patrocinadores você valoriza mais em uma equipe?")
        print("\n 1-Empresas de tecnologia","\n 2-Marcas automotivas de prestígio","\n 3-Empresas comprometidas com a sustentabilidade","\n 4-Outros")
        
        questão7 = int(input("Digite um Numero"))

        if questão7 == 1:
            if lista_q [6] in lista_q:
                MER.append(lista_q[6])
                POR.append(lista_q[6])
                AUD.append(lista_q[6])
                break
            
        elif questão7 == 2:
            if lista_q [6] in lista_q:
                JAG.append(lista_q[6])
                BMW.append(lista_q[6])
                break

        elif questão7 == 3:
            if lista_q [6] in lista_q:
                MAH.append(lista_q[6])
                NIS.append(lista_q[6])
                break

        elif questão7 == 6:
            if lista_q [6] in lista_q:
                DS.append(lista_q[6])
                VEN.append(lista_q[6])
                NIO.append(lista_q[6])
                break

        else:
            print("\n Numero Invalido")

    #Q8

    while Q[7]:
    
        print("")
        print("     8 - Qual é o seu histórico de apoio a equipes esportivas?")
        print("\n 1-Geralmente apoio equipes líderes","\n 2-Geralmente apoio equipes subestimadas ou azarões","\n 3-Acompanho várias equipes, independentemente do desempenho")
        
        questão8 = int(input("Digite um Numero"))

        if questão8 == 1:
            if lista_q [7] in lista_q:
                MER.append(lista_q[7])
                AUD.append(lista_q[7])
                break

        elif questão8 == 2:
            if lista_q [7] in lista_q:
                MAH.append(lista_q[7])
                DS.append(lista_q[7])
                break

        elif questão8 == 3:
            if lista_q [7] in lista_q:
                JAG.append(lista_q[7])
                BMW.append(lista_q[7])
                NIS.append(lista_q[7])
                POR.append(lista_q[7])
                NIO.append(lista_q[7])
                VEN.append(lista_q[7])
                break

            else:
                print("\n Numero Invalido")

    #Q9
    while Q[8]:

        print("")
        print("     9 - Qual é a sua visão de sucesso na Fórmula E?")
        print("\n 1-Vitórias e títulos de campeonato","\n 2-Desenvolvimento de tecnologia inovadora","\n 3-Contribuição para a conscientização soe veículos elétricos")
        questão9 = int(input("Digite um Numero"))

        if questão9 == 1:
            if lista_q [8] in lista_q:
                MER.append(lista_q[8])
                POR.append(lista_q[8])
                AUD.append(lista_q[8])
                break
            
        elif questão9 == 2:
            if lista_q [8] in lista_q:
                MAH.append(lista_q[8])
                DS.append(lista_q[8])
                BMW.append(lista_q[8])
                break
            

        elif questão9 == 3:
            if lista_q [8] in lista_q:
                JAG.append(lista_q[8])
                NIS.append(lista_q[8])
                NIO.append(lista_q[8])
                VEN.append(lista_q[8])
                break

        else:
            print("\n Numero Invalido")

    #Q10

    while Q[9]:
        print("")
        print("     10 - O que mais te inspira na Fórmula E?")
        print("\n 1-Os pilotos e suas habilidades","\n 2-O espírito de equipe e colaboração","\n 3-A busca contínua por excelência e inovação")
        print("")

        questão10 = int(input("Digite um Numero"))

        if questão10 == 1:

            if lista_q [9] in lista_q:
                MER.append(lista_q[9])
                POR.append(lista_q[9])
                AUD.append(lista_q[9])
                break
            
        elif questão10 == 2:
            if lista_q [9] in lista_q:
                MAH.append(lista_q[9])
                DS.append(lista_q[9])
                NIS.append(lista_q[9])
                break
            

        elif questão10 == 3:
            if lista_q [9] in lista_q:
                JAG.append(lista_q[9])
                BMW.append(lista_q[9])
                NIO.append(lista_q[9])
                VEN.append(lista_q[9])
                break

        else:
            print("\n Numero Invalido")

    for i in range (0,9):
        Pontos[i] = 0
        for Valor[i] in Equipes[i]:
            Pontos[i] += Valor[i]

    Carros = [Mer, Por, Aud, Ds , Nis, Bmw, Jag, Ven, Mah, Nio] 
    Marcas = []
    for i in range (0, 10):
        Marcas.append((Carros[i], Pontos [i]))

    Maior_Marca = None #uso para criar uma variavel vazia, assim como no for
    Maior_Pontuacao = -1 #uso do -1 para evitar erro de resposta caso todos os valores sejam = 0

    for Carros, Pontos in Marcas:
        if Pontos > Maior_Pontuacao:
            Maior_Marca = Carros
            Maior_Pontuacao = Pontos
    print("        A Equipe cujo você tem mais afinidade é a Equipe do(a):", Maior_Marca)

    print(Marcas)
    Quiz_Realizado = False
