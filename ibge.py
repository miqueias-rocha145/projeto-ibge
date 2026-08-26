from utils import utils

class dados_ibge():

    @staticmethod
    def get_UFs() -> dict[str, dict[str, int,str]]:
        url  = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'
        params = {
            'orderBy': 'nome'
        }

        resultado = utils.fazer_requests(url=url,params=params)

        parsed_resposta = { #Cria dicionário contendo UF como chave e ID e NOME como Value
            item['id']: {
                'UF': item['sigla'],
                'Nome_UF': item['nome']
                }
            for item in resultado
        }

        return parsed_resposta

    @staticmethod
    def get_Frequencia_Nome_By_UFs(nome: str):
        url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
        params = {
            'groupBy': 'UF'
            }

        return utils.fazer_requests(url=url,params=params)

    @staticmethod
    def get_Nome_By_UF(nome: str, id_uf: int):
        url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
        params = {
            'sexo': 'M',
            'localidade': id_uf
        }

        resultado = utils.fazer_requests(url=url,params=params)

        return resultado[0]