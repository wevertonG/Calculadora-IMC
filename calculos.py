def calcular_imc(peso, altura):
    
    if '.' not in altura:
        altura = altura[:-2] + '.' + altura[-2:]

    peso = float(peso)
    altura = float(altura) 

    calculo_imc = peso / (altura ** 2)
    calculo_imc_arredondado = round(calculo_imc, 2)
    
    return calculo_imc_arredondado