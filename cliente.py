import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9999

s.connect((host, port))
data = []


def tabela():
    print('Escolha a opcao desejada\n1. Metro para centimetro\n'
          '2. Metro para quilometro\n'
          '3. Metro quadrado para centimetro quadrado\n'
          '4. Metro quadrado para quilometro quadrado\n'
          '5. Metro cubico para centimetro cubico\n'
          '6. Metro cubico para quilometro cubico\n ')


confirm = True

while confirm:
    tabela()
    resp = int(input('Insira a opção de conversão\n'))
    val1 = int(input('Insira o valor que quer converter\n'))
    data.append(resp)
    data.append(val1)
    s.send(pickle.dumps(data))
    valConvertido = s.recv(1024)
    valConvertido = pickle.loads(valConvertido)
    s.close()
    if resp == 1:
        print(f"\nO novo valor é: {valConvertido} cm\n")

    if resp == 2:
        print(f"\nO novo valor é: {valConvertido} km\n")

    if resp == 3:
        print(f"\nO novo valor é: {valConvertido} cm²\n")

    if resp == 4:
        print(f"\nO novo valor é: {valConvertido} km²\n")

    if resp == 5:
        print(f"\nO novo valor é: {valConvertido} cm³\n")

    if resp == 6:
        print(f"\nO novo valor é: {valConvertido} km³\n")

    confirm = input('Deseja continuar a converter?')
    data.clear()
    if confirm == 'S' or confirm == 's':
        s.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
    else:
        confirm = False

s.close()
