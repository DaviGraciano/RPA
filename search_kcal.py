import pandas as pd
import requests
import os
import sqlite3
from tqdm import tqdm

def consulta_informacao(lista_alimentos):

    

    #### declaro listas vazias apra montar um dicionario com as informacoes coletadas na api
    descricao = []
    quantidade = []
    calorias = []
    session = requests.Session()
    for alimento in tqdm(lista_alimentos, desc="Processando alimentos"):
        url = f"https://caloriasporalimentoapi.herokuapp.com/api/calorias/?descricao={alimento}"

        response = session.get(url)
        ##### Faco a requisicao, se o statuscode for 200, jogo os valores para a lista
        if response.status_code == 200:
            json_data = response.json()
            
            for item in json_data:
                descricao.append(item['descricao'])  
                quantidade.append(item['quantidade'])  
                calorias.append(item['calorias'])

    ### monto o dicionario e coloco em um dataframe do pandas    
    d = {'descricao': descricao, 'quantidade': quantidade, 'calorias': calorias}
    
    df = pd.DataFrame(d)
    return df


def main():

    #### lista com o nome dos alimentos que irei consultar na api
    alimentos_brasileiros = ["Arroz","Feijão","Macarrão","Batata","Milho","Mandioca","Farinha de trigo","Pão","Carne bovina","Frango","Porco","Peixe","Ovo","Leite","Queijo","Iogurte","Açúcar","Sal","Óleo de soja","Azeite","Café","Chá","Banana","Maçã","Laranja","Abacaxi","Alface","Couve","Espinafre","Cenoura","Tomate","Cebola","Pimentão","Abobrinha","Sopa","Massa de pastel","Pizza","Sorvete","Bolo","Brigadeiro","Beijinho","Coxinha","Pão de queijo","Açaí","Batata frita","Pastel","Suco de laranja","Suco de abacaxi","Coca Cola","Guaraná","Cerveja"]
    
    ## crio a conexao com o banco de dados sqlites
    conn = sqlite3.connect('alimentos.db')

    #####consulto as informacoes
    df = consulta_informacao(alimentos_brasileiros)

    #### crio a tabela de calorias com as informacoes que busquei na api
    df.to_sql('tb_calorias', conn, if_exists='replace', index=False)
    
    conn.close()


if __name__ == "__main__": 
       main()
