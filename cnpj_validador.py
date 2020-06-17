def cnpj_valido(cnpj):
    validador = True

    # Verificador do número de dígitos do CNPJ
    if len(cnpj) != 14:
        validador = False

    cnpj_list = [int(x) for x in list(cnpj)]

    # Verificador do primeiro dígito do CNPJ
    soma1 = 0
    multiplicador1 = 5
    for i in range(0, 4):
        soma1 += cnpj_list[i]*multiplicador1
        multiplicador1 -= 1
    multiplicador2 = 9
    for f in range(4, 12):
        soma1 += cnpj_list[f]*multiplicador2
        multiplicador2 -= 1
    resto1 = soma1 % 11
    if resto1 < 2:
        digito1 = 0
        if cnpj_list[12] != digito1:
            validador = False
    else:
        digito1 = 11 - resto1
        if cnpj_list[12] != digito1:
            validador = False
   
    # Verificador do segundo dígito do CNPJ
    soma2 = 0
    multi1 = 6
    for i in range(0, 5):
        soma2 += cnpj_list[i]*multi1
        multi1 -= 1
    multi2 = 9
    for f in range(5, 13):
        soma2 += cnpj_list[f]*multi2
        multi2 -= 1
    resto2 = soma2 % 11
    if resto2 < 2:
        digito2 = 0
        if cnpj_list[13] != digito2:
            validador = False
    else:
        digito2 = 11 - resto2
        if cnpj_list[13] != digito2:
            validador = False

    return validador

cnpj = "11444777000161"
print(cnpj_valido(cnpj))
