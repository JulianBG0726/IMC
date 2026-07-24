peso = float(input("Ingresa tu peso (kg): "))
estatura = float(input("Ingresa tu estatura (m): "))
imc = peso/(estatura**2)

match imc:
    case imc if imc <= 18.5:
        print("Tu índice de masa corporal es de: ", imc, " tienes un peso inferior al normal")
    case imc if imc > 18.5 and imc < 24.9:
        print("Tu índice de masa corporal es de: ", imc, " tienes un peso normal")
    case imc if imc >= 25 and imc <=29.9:
        print("Tu índice de masa corporal es de: ", imc, " tienes un peso superior al normal")    
    case imc if imc >= 30:
        print("Tu índice de masa corporal es de: ", imc, " tienes obesidad")    