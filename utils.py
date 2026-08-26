import requests
from ibge import dados_ibge

class utils():

    def fazer_requests(url: str, params: dict = None):
        resposta = requests.get(
             url, 
             params=params,
             timeout=10
         )
        
        try:
             resposta.raise_for_status()
        except requests.HTTPError as e:
             print(f"Ocorreu um erro: {e}")
             resultado = None
        else:
             resultado = resposta.json()
        finally:
             return resultado

    def tabela_Nome_By_Uf(nome):
        ufs = dados_ibge.get_UFs()
        Frequencia_Nome_By_UFs = dados_ibge.get_Frequencia_Nome_By_UFs(nome)

        tabela_final = {
            ufs[int(item['localidade'])]['Nome_UF']: #Acessa ufs pela localidade que vem de Frequencia_Nome_By_UFs
            item['res'][0]['proporcao'] #Acessa proporcao que vem de Frequencia_Nome_By_UFs
            for item in Frequencia_Nome_By_UFs
        }

        return tabela_final

if __name__ == '__main__':
     pass