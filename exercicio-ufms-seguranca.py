import string

def gerar_alfabeto_chave(chave):
    chave = "".join(dict.fromkeys(chave.lower()))
    alfabeto_padrao = string.ascii_lowercase
    novo_alfabeto = chave + "".join([c for c in alfabeto_padrao if c not in chave])
    return novo_alfabeto

def substituir(texto, alfabeto_origem, alfabeto_destino):
    mapa = str.maketrans(alfabeto_origem, alfabeto_destino)
    mapa.update(str.maketrans(alfabeto_origem.upper(), alfabeto_destino.upper()))
    return texto.translate(mapa)

chave_simples = "CRIPTOGRAFIA"
alfabeto_normal = string.ascii_lowercase
alfabeto_cifrado = gerar_alfabeto_chave(chave_simples)

mensagem = "Criptografado"
texto_cifrado = substituir(mensagem, alfabeto_normal, alfabeto_cifrado)
texto_original = substituir(texto_cifrado, alfabeto_cifrado, alfabeto_normal)

print(f"Alfabeto Cifrado: {alfabeto_cifrado}")
print(f"Cifrado: {texto_cifrado}")
print(f"Decifrado: {texto_original}")