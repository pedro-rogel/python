

def nova_pessoa():
    nome = input('Digite o nome da nova pessoa que deseja cadastrar: ')
    idade = input('Digite a idade da nova pessoa que deseja cadastrar: ')
    cidade = input('Digite a cidade da pessoa que deseja ccadastrar: ')
    dados_pessoa = {'pessoa':nome, 'idade':idade, 'cidade':cidade}
    lista_pessoa.append(dados_pessoa)
    listar_nomes()

def listar_nomes():
    global nome
    global pessoa
    for pessoa in lista_pessoa:
        nome = pessoa['pessoa']
        idade = pessoa['idade']
        cidade = pessoa['cidade']
        print(f'{nome.ljust(10)} | {idade.ljust(10)} | {cidade} ')
        
def cadastro():
    global x
    x = input('O seu nome está nessa lista?: ').upper()
    if x == 'NAO' or x =='NÃO':
        nova_pessoa() 
    elif x == 'SIM':
        nome_encontrado = False
        for pessoa in lista_pessoa:
             x1 = input('Digite seu nome: ')
             if x1 == pessoa['pessoa']:
                 print(f'Seja Bem Vindo, {x1}')
                 nome_encontrado = True              
             else:
                 print('Nome não encontrado.')
                 cadastro()
lista_pessoa = [
    {'pessoa' : 'Pedro' , 'idade':'18', 'cidade':'São Paulo'}, 
    {'pessoa' : 'Joao'  , 'idade':'18', 'cidade':'Rio Grande do Sul'},
    {'pessoa' : 'Maria' , 'idade':'18', 'cidade':'Minas Gerais'},
    {'pessoa' : 'Paulo', 'idade':'18', 'cidade':'São Paulo' }
]
print(f'Nome | Idade  | Cidade')  
listar_nomes()
cadastro()
cadastro()
