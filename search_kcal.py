import pandas as pd
import requests
import os
import sqlite3
from tqdm import tqdm

def consulta_informacao():
    alimentos_brasileiros = [
    "Arroz",
    "Feijão",
    "Macarrão",
    "Batata",
    "Milho",
    "Mandioca",
    "Farinha de trigo",
    "Pão",
    "Carne bovina",
    "Frango",
    "Porco",
    "Peixe",
    "Ovo",
    "Leite",
    "Queijo",
    "Iogurte",
    "Açúcar",
    "Sal",
    "Óleo de soja",
    "Azeite",
    "Café",
    "Chá",
    "Banana",
    "Maçã",
    "Laranja",
    "Abacaxi",
    "Alface",
    "Couve",
    "Espinafre",
    "Cenoura",
    "Tomate",
    "Cebola",
    "Pimentão",
    "Abobrinha",
    "Sopa",
    "Massa de pastel",
    "Pizza",
    "Sorvete",
    "Bolo",
    "Brigadeiro",
    "Beijinho",
    "Coxinha",
    "Pão de queijo",
    "Açaí",
    "Batata frita",
    "Pastel",
    "Suco de laranja",
    "Suco de abacaxi",
    "Coca Cola",
    "Guaraná",
    "Cerveja"
    ]

    
    descricao = []
    quantidade = []
    calorias = []
    session = requests.Session()
    for alimento in tqdm(alimentos_brasileiros, desc="Processando alimentos"):
        url = f"https://caloriasporalimentoapi.herokuapp.com/api/calorias/?descricao={alimento}"

        response = session.get(url)

        if response.status_code == 200:
            json_data = response.json()
            
            for item in json_data:
                descricao.append(item['descricao'])  
                quantidade.append(item['quantidade'])  
                calorias.append(item['calorias'])
            
    d = {'descricao': descricao, 'quantidade': quantidade, 'calorias': calorias}
    
    df = pd.DataFrame(d)
    return df


def main():
    
    conn = sqlite3.connect('alimentos.db')
    df = consulta_informacao()
    df.to_sql('tb_calorias', conn, if_exists='replace', index=False)
    
    conn.close()


if __name__ == "__main__": 
       main()
