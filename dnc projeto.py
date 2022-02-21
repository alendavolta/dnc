#informações
população = 19120000
#service addressable market 
SAM = 0.12*população
#
#70% do leads são da capital IMPORTANTE
market = 0.10
market = market*SAM
#segmento
industria = 0.300
ecommerce = 0.240
tecnologia = 0.150
pd = 0.140
serviço = 0.170

    #produtos
#industria
ipind = 0.800
dexind = 0.200
#ecommerce
dexecom = 0.200
smsecom = 0.500
ppmecom = 0.300
#tecnologia
ppmtec = 0.600
dextec = 0.400
#pd
ippd = 0.700
ppmpd = 0.300
#serviços
ipserv = 0.600
ppmserv = 0.300
smsserv = 0.100
#porcentagens relativas
ipindustria = ipind*industria
dexindustria = dexind*industria

dexcomerce= dexecom*ecommerce 
smscomerce = smsecom*ecommerce
ppmecom = ppmecom*ecommerce

ppmtecnologia = ppmtec*tecnologia
dextecnologia = dextec*tecnologia

ippd2 = ippd*pd 
ppmpd2 = ppmpd*pd

ipserviço = ipserv*serviço
ppmserviço = ppmserv*serviço
smsserviço = smsserv*serviço
#soma das porcentagens dos cursos
somaip = ipindustria+ippd2+ipserviço
somadex = dexindustria+dexcomerce+dextecnologia
somasms = smscomerce+smsserviço
somappm = ppmecom+ppmpd2+ppmtecnologia+ppmserviço
#taxas de conversão de oportunidades para vendas e de leads para oportunidades
Txopor = 0.05
Txleads = 0.23
marketsharednc = (market*Txleads*Txopor)
#total de alunos em cada formação
alunosip = int(somaip*marketsharednc)+1
alunosdex = int(somadex*marketsharednc)+1
alunossms = int(somasms*marketsharednc)
alunosppm = int(somappm*marketsharednc)
#turmas de até 400 alunos, após isso se divide em 2
#numero de turmas para cada formação
#total de alunos DNC
totalalunosdnc = (alunosip+alunosdex+alunossms+alunosppm)
#funil de marketing
leads = int(market)
oportunidades = int(market*Txleads)
vendas = int(oportunidades*Txopor)

Capitalleads = int(market*0.7)
Capitalopor = int(oportunidades*0.7)
Capitalvendas = int(vendas*0.7)

cidadeleads = int(market*0.3)
cidadeopor = int(oportunidades*0.3)
cidadevendas = int(vendas*0.3)+1
#CPL
cplcapital = 4
cplcidade = 3.20
cplcapitalt = cplcapital*Capitalleads
cplcidadet = cidadeleads*cplcidade
cpltotal = cplcapitalt+cplcidadet
#custo por min de legenda 1h = 60
#Clegendas = 1.20
ipc = 380*60*1.20
dexc = 520*60*1.20
smsc = 420*60*1.20
ppmc = 480*60*1.20
Custolegendas = ipc+dexc+smsc+ppmc
#custo legendas+leads
custototal = (Custolegendas+cpltotal)
#Ticket médio de R$5200,00
ticket = 5200
#cambio
peso = 0.00625
#FATURAMENTO
faturamento = totalalunosdnc*ticket
faturamentopesos = faturamento/peso
#prints 1
print ("Total de alunos em cada formação")
print ("Imersão de projetos\n", alunosip)
print ("Data expert\n", alunosdex)
print ("Sales and Marketing\n", alunossms)
print ("Produt Management\n", alunosppm)
print()
#prints 2
print ("Total de alunos DNC", totalalunosdnc)
print()
#prints 3
print  (" Imersão de Projetos", somaip,"\n",\
       "Data expert", somadex,"\n",\
       "Sales and Marketing",somasms,"\n",\
       "Produt Management",somappm,"\n")
print()
#prints 4
print (" Nº de turmas em imersão de proejetos", alunosip//400+1,"\n","Nº de turmas em data expert", alunosdex//400+1,"\n",\
       "Nº de turmas em sales and marketing", alunossms//400+1,"\n","Nº de turmas em produt management", alunosppm//400+1)
print()
#prints 5
print ("Funil Capital", Capitalleads,Capitalopor, Capitalvendas)
print ("Funil cidades", cidadeleads,cidadeopor, cidadevendas)

#prints 6
#6 print ("CPL CAPITAL",cplcapitalt,"CPL cidades", cplcidadet)
print ("CPL TOTAL",cpltotal)
print()
#prints 7
print ("Custo legendas", Custolegendas)
#prints 8
print("INVESTIMENTO TOTAL",custototal)
print()
#prints 9
print ("Faturamento em brl", faturamento)
#prinst 10
print ("Faturamento em pesos chilenos", faturamentopesos)











