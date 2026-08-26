from pprint import pprint
from utils import utils

def main(nome):
    pprint(utils.tabela_Nome_By_Uf(nome))

    print('\n===========================\n')

    pprint(utils.tabela_Frequencia_Decadas(nome))

if __name__ == '__main__':
    main('Miqueias')