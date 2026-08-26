from pprint import pprint
import requests
from utils import utils

def main(nome):
    pprint(utils.tabela_Nome_By_Uf(nome))

if __name__ == '__main__':
    main('Miqueias')