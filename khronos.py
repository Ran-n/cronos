#! /usr/bin/python3
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	20/07/2019 12:38:02
#+ Editado:	20/07/2019 13:15:02
#------------------------------------------------------------------------------------------------
"""
formatador de datas en texto estándar

Exemplo:
102019071009550000
→ 1 02019 07 10 09 55 00 00

0 		→ a.C 			→ 1bit
ou
1 		→ d.C 			→ Mesmo bit
02019 	→ ano 			→ 5bits
07 		→ mes 			→ 2bits
10 		→ día 			→ 2bits
55 		→ minuto 		→ 2bits
00 		→ segundo 		→ 2bits
00 		→ microsegundo 	→ 2bits

comando para sacar os valores precisos
date +"%Y-%m-%d %H:%M:%S:%2N" 
"""
#------------------------------------------------------------------------------------------------
from datetime import datetime as dt
#------------------------------------------------------------------------------------------------
def getAgora():
	tempo = dt.now()
	ano = str(tempo.year)
	# axustámolo aos 5 díxitos que usamos no formateo
	ano = '0'+ano if len(ano) < 5 else ano

	mes = str(tempo.month)
	# igual ca ano formatamos o mes
	mes = '0'+mes if len(mes) < 2 else mes
	
	dia = str(tempo.day)
	# mesmo rollete
	dia = '0'+dia if len(dia) < 2 else dia
	
	hora = str(tempo.hour)
	# mesmo rollete
	hora = '0'+hora if len(hora) < 2 else hora
	
	minuto = str(tempo.minute)
	# mesmo rollete
	minuto = '0'+minuto if len(minuto) < 2 else minuto
	
	segundo = str(tempo.second)
	# mesmo rollete
	segundo = '0'+segundo if len(segundo) < 2 else segundo
	
	microsegundo = str(tempo.microsecond)[:2]

	return '1'+ano+mes+dia+hora+minuto+segundo+microsegundo
#------------------------------------------------------------------------------------------------
if __name__=="__main__":
	print(getAgora())
#------------------------------------------------------------------------------------------------
