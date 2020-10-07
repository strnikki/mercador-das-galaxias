if __name__ == '__main__':
    numero_romano = str(input("Digite um numero:"))
    conversao = { 'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000 }
    print(conversao[numero_romano])
