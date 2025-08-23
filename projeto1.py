pesoCarro = float(input("Digite o peso do carro em libras: "))
porcentagemPesoDianteira = float(input("Digite a porcentagem do peso da dianteira: "))
porcentagemPesoTraseira = 100 - porcentagemPesoDianteira

molaDianteira = (pesoCarro - (pesoCarro * porcentagemPesoDianteira / 100)) / 2 
molaTraseira = (pesoCarro - (pesoCarro * porcentagemPesoTraseira / 100)) / 2

def CalculoRigidezRetorno(numero: float) -> float:
    
    num_str = str(float(numero))
    primeiro = int(num_str[0]) + 1
    segundo = num_str[1]
    
    valor = float(f"{primeiro}.{segundo}")
    return valor

rigidezRetornoDianteira = CalculoRigidezRetorno(molaDianteira)
rigidezRetornoTraseira = CalculoRigidezRetorno(molaTraseira)

rigidezCompressãoDianteira = rigidezRetornoDianteira * 1.5
rigidezCompressãoTraseira = rigidezRetornoTraseira * 1.5

print(f"O valor que você deve inserir na mola dianteira é: ", molaDianteira)
print(f"O valor que você deve inserir na mola traseira é: ", molaTraseira)
print(f"O valor da rigidez do retorno dianteiro é: ", rigidezRetornoDianteira)
print(f"O valor da rigidez do retorno traseiro é: ", rigidezRetornoTraseira)
print(f"O valor da rigidez da compressão dianteira é: ", rigidezCompressãoDianteira)
print(f"O valor da rigidez da compressão traseira é: ", rigidezCompressãoTraseira)




