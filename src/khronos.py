#! /usr/bin/python3
#------------------------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
#+ Autor:	Ran#
#+ Creado:	2019/07/20 12:38:02
#+ Editado:	2022/01/15 22:22:54.320547
#------------------------------------------------------------------------------------------------
from datetime import datetime as dt
#------------------------------------------------------------------------------------------------
def agora() -> int:
    """
    formatador de datas en texto estándar

    Exemplo:
    +20190710095500000000
    → +2019 07 10 09 55 00 000000

    +(1)	→ a.C 			→ 1bit
    ou
    -(0)	→ d.C 			→ Mesmo bit
    2019 	→ ano 			→ Nbits
    07 		→ mes 			→ 2bits
    10 		→ día 			→ 2bits
    55 		→ minuto 		→ 2bits
    00 		→ segundo 		→ 2bits
    000000 	→ microsegundo 	→ 6bits

    comando para sacar os valores precisos
    echo -n '+';date +"%Y-%m-%d %H:%M:%S:%6N"

    @entradas:
        Ningunha

    @saídas:
        Enteiro -   Sempre
        └ Co timestamp
    """

    agora = dt.now()

    valores = [
            agora.year,
            agora.month,
            agora.day,
            agora.hour,
            agora.minute,
            agora.second,
            agora.microsecond
            ]

    return '+'+''.join([str(ele) for ele in valores])
#------------------------------------------------------------------------------------------------
