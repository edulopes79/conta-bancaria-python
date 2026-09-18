class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def mostra_saldo(self):
        print(f"\nTitular: {self.titular}")
        print(f"Saldo: {self.saldo}")

nome1 = input("Digite o nome do titular: ").upper().strip()
sal_a1 = float(input("Digite o saldo inicial: R$"))
dep1 = float(input("Quantos reais você deseja depositar? R$"))
sac1 = float(input("Quantos reais você deseja sacar? R$"))
salf1 = sal_a1 + dep1 - sac1

nome2 = input("\nDigite o nome do titular: ").upper().strip()
sal_a2 = float(input("Digite o saldo inicial: R$"))
dep2 = float(input("Quantos reais você deseja depositar? R$"))
sac2 = float(input("Quantos reais você deseja sacar? R$"))
salf2 = sal_a2 + dep2 - sac2

titular1 = ContaBancaria(f"{nome1}", f"R$ {salf1:.2f}")
titular2 = ContaBancaria(f"{nome2}", f"R$ {salf2:.2f}")

titular1.mostra_saldo()
titular2.mostra_saldo()
