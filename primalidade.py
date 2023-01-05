n = int(input("Digite um número inteiro: "))


# procure por um divisor de n entre 2 e n-1


divisor = 2


primalidade = True


while divisor < n and primalidade == True:

	if n % divisor == 0:

		primalidade = False

	divisor = divisor + 1


if primalidade == True and n != 1:

	print("primo")

	
else:

	print("não primo")