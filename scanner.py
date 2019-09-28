import json
import Tree
t = Tree.Tree()

entrada = open('arquivo.txt', 'r')
linha = entrada.read()
caracter = ['/']
tokens = []
erros = []


def analiseSintatica(entrada):
    linha = entrada.split('/')
    saida = ''
    if (not(str(entrada).__contains__('/'))):
        print('erro: caractere invalido')
        return False

    elif (len(linha) != 3):
        print('erro: formato de data inválido')
        return False

    elif (len(linha[0]) != 2 or not(linha[0].isdigit())):
        print('erro: Tipo de entrada inválida ou quantidade de digitos para dia inválido')
        return False

    elif(len(linha[1]) != 2 or not(linha[1].isdigit())):
        print('erro: Tipo de entrada inválida ou quantidade de digitos para mês inválido')
        return False

    elif(len(linha[2]) != 4 or not(linha[2].isdigit())):
        print('erro: Tipo de entrada inválida ou quantidade de digitos para ano inválido')
        return False

    else:
        return True


def analiseLexica(entrada):
    token = ""
    indice = 1
    for i in range(len(linha)):
        token += linha[i]
        if(token in caracter):
            tokens.append({
                "token": token,
                "identificacao": "Caractere",
                "tamanho": len(token),
                "posicao": ('({},{})'.format(0, i - len(token)))
            })
            token = ""
        elif (token.isdigit()):

            tokens.append({
                "token": token,
                "identificacao": "numero",
                "tamanho": len(token),
                "posicao": ("({},{})".format(0, i - len(token)))
            })
            token = ""
            indice += 1
        else:
            print(token)
            erros.append({
                "token": token,
                "posicao": ("({},{})".format(0, i - len(token)))
            })
            token = ""
    entrada.close()
    with open('output.json', 'w+') as output:
        output.write('{\n\t"tokens": [\n')
        for i in range(len(tokens)):
            if i <= len(tokens)-2:
                ij = json.dumps(tokens[i])
                output.write("\t"+ij+",\n")
            else:
                ij = json.dumps(tokens[i])
                output.write("\t"+ij+"\n")
        output.write("\t],\n")

        output.write('\t"erros": [\n')
        for i in range(len(erros)):
            if i <= len(erros)-2:
                ij = json.dumps(erros[i])
                output.write("\t"+ij + ",\n")
            else:
                ij = json.dumps(erros[i])
                output.write("\t"+ij + "\n")
        output.write("\t]\n}\n")

    output.close()


analiseLexica(entrada)
