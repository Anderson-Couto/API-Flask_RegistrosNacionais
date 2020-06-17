def cpf_valido(cpf):
    validador = True

    # Verificador do número de dígitos do CPF
    if len(cpf) != 11:
        validador = False

    # Verificador do CPF para dígitos repetitivos
    for x in range(0,10):
        if str(cpf) == str(x)*11:
            validador = False

    cpf_list = [int(x) for x in list(cpf)]

    # Verificador do primeiro dígito do CPF após "-"
    soma1 = 0
    multiplicador1 = 10
    for i in range(0, 9):
        soma1 += cpf_list[i]*multiplicador1
        multiplicador1 -= 1
    resto1 = soma1*10 % 11
    if resto1 == 10:
        resto1 = 0
    if resto1 != cpf_list[9]:
        validador = False

    # Verificador do segundo dígito do CPF após "-"
    soma2 = 0
    multiplicador2 = 11
    for i in range(0, 10):
        soma2 += cpf_list[i]*multiplicador1
        multiplicador2 -= 1
    resto2 = soma2*10 % 11
    if resto2 == 10:
        resto2 = 0
    if resto2 != cpf_list[10]:
        validador = False
    
    return validador
