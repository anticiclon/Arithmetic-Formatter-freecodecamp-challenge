# -*- coding: utf-8 -*-

import operator

digitos = set('0123456789')

operadores = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.floordiv,
    '^' : operator.pow,
}


def es_digito(var):
    return var in digitos

def dame_numero(varstr):
    s = ""
    for c in varstr:
        if not es_digito(c):
            return "Error: Numbers must only contain digits."
            break
        s += c
    return (int(s), len(s))

def calcula(string, num1, num2):
    op = operadores.get(string)
    if op == operator.add or op == operator.sub:
        return op(num1, num2)
    else:
        return "Error: Operator must be '+' or '-'."

def calculador(expresion):
    lista = expresion.split()
    numero1 = dame_numero(lista[0])
    numero2 = dame_numero(lista[2])
    if numero1 == "Error: Numbers must only contain digits." or numero2 == "Error: Numbers must only contain digits.":
        return "Error: Numbers must only contain digits."
    if numero1[1]>4 or numero2[1]>4:
        return "Error: Numbers cannot be more than four digits."
    else:
        aux = calcula(lista[1], numero1[0], numero2[0])
        if aux == "Error: Operator must be '+' or '-'.":
            return "Error: Operator must be '+' or '-'."
        else:
            return aux
    
def dibujo(expresion, cuenta):
    espacio = " "    
    raya="-"
    lista = expresion.split()
    largo1 = len(lista[0])
    largo2 = len(lista[2])
    diferencia = abs(largo1-largo2)
    aux = calculador(expresion)
    if aux == "Error: Numbers must only contain digits.":
        return "Error: Numbers must only contain digits."
    elif aux == "Error: Numbers cannot be more than four digits.":
        return "Error: Numbers cannot be more than four digits."
    elif aux == "Error: Operator must be '+' or '-'.":
        return "Error: Operator must be '+' or '-'."
    else:
        resultado = str(aux)
    largo3 = len(resultado)
    dife1 = abs(largo3-(largo1+2))
    dife2 = abs(largo3-(largo2+2))
    if largo1>4 or largo2>4:
        return "Error: Numbers cannot be more than four digits."
    else:
        if largo1>largo2 and cuenta == False:
            resultado = (2*espacio+lista[0]+"\n"+lista[1]+(1+diferencia)*espacio
                  +lista[2]+"\n"+raya*(largo1+2))
        elif largo1>largo2 and cuenta == True:
            resultado = (2*espacio+lista[0]+"\n"+lista[1]+(1+diferencia)*espacio
                  +lista[2]+"\n"+raya*(largo1+2)+"\n"+dife1*espacio+resultado)
        elif largo1<=largo2 and cuenta == False:
            resultado = ((2+diferencia)*espacio + lista[0]+"\n"+lista[1]+espacio+
                  lista[2]+"\n"+raya*(largo2+2))
        elif largo1<=largo2 and cuenta == True:
            resultado = ((2+diferencia)*espacio + lista[0]+"\n"+lista[1]+espacio+
                  lista[2]+"\n"+raya*(largo2+2)+"\n"+dife2*espacio+resultado)
    return resultado
 
def arithmetic_arranger(problems, print_result = False):
    espacio = " "    
    raya="-"
    lista4 =[]
    if len(problems) > 5:
        return 'Error: Too many problems.'
    else:
        if print_result == True:
            lista1 = [dibujo(x, True) for x in problems]
        else:
            lista1 = [dibujo(x, False) for x in problems]
        
        if "Error: Numbers must only contain digits." in lista1:
            return "Error: Numbers must only contain digits."
        elif "Error: Numbers cannot be more than four digits." in lista1:
            return "Error: Numbers cannot be more than four digits."
        elif "Error: Operator must be '+' or '-'." in lista1:
            return "Error: Operator must be '+' or '-'."
        elif "Error: Numbers cannot be more than four digits." in lista1:
            return "Error: Numbers cannot be more than four digits."
        else:
            lista2 = [x.splitlines() for x in lista1]
            for x in range(len(lista2[0])):
                lista3 =[]
                for idx, entry in enumerate(lista2):
                    if idx != len(lista2)-1:
                        lista3.append(entry[x]+ 4*espacio)
                    else:
                        lista3.append(entry[x])
                lista3str="".join(lista3)
                lista4.append(lista3str)
            lista4="\n".join(lista4)
            return lista4
        

