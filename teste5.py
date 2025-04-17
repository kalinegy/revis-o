peso=float(input("Digite seu peso:"))
altura=float(input("Digite sua altura:"))
imc= peso/(altura)**2
if imc < 18.6:
    print("Você está abaixo do peso, engorde")
if imc > 18.6 and imc<= 24.9:
    print("Você está no peso ideal parabéns!")
if imc >= 25.0 and imc<= 29.9:
    print("Você está levemente acima do peso")
if imc >= 30.0 and imc<= 34.9:
    print("Você está com obesidade grau1")
if imc >= 35.0 and imc<= 39.9:
    print("Você está com obesidade severa(grau2)")
if imc >= 40.0:
    print("Você está com obesidade severa(mórbida)")
