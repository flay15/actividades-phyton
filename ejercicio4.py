# Definimos una variable de tipo flotante
saldo = 50.0

# Simulamos un ciclo de depósitos de saldo hasta que el saldo supere 150
while saldo < 150:
    deposito = 20.0
    saldo += deposito
    print(f"Se ha depositado {deposito}, saldo actual: {saldo}")
