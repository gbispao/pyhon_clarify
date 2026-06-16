import requests
import pandas as pd
import sqlite3
import datetime
import time
import random 
from bs4 import BeautifulSoup 

#jquery - Serve para ver o tamanho do meu código e poder mimificar ele, diminuir

# SUPABASE - banco de dados

# VERCEL - manter site no ar

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0 Safari/537.36'}
baseURL = 'https://www.sampaingressos.com.br/templates/ajax/lista_espetaculo.php'
filmes = []
data_hoje = datetime.date.today().strftime('%d-%m-%Y')
agora = datetime.datetime.now()
bancoDados = r"C:\Users\noturno\Desktop\Python_Guilherme\banco_filmes.db" # O barra n da problema, então colocamos o r para ele não olhar essa parte
saidaCSV = f"C:/Users/noturno/Desktop/Python_Guilherme/show_sampaingressos_{data_hoje}.csv" # Aqui seria outra forma de fazer, invertendo a barra

paginaLimite = 1
pagTempoMin = 1
pagTempoMax = 5
cardTempMin = 1
cardTempMax = 1

for pagina in range(1, paginaLimite + 1):
    url = f"{baseURL}?pagina={pagina}&tipoEspetaculo=shows"
    print(f"Coletando dados da pagina {pagina} : {url}")
    resposta = requests.get(url, headers = header)
    soup = BeautifulSoup(resposta.text, "html.parser")
    
    if resposta.status_code != 200:
        print(f'Erro ao caregar a página {pagina}. Codigo de erro é: {resposta.status_code}')
        continue 
    
    cards = soup.find_all('div', id = 'box_espetaculo')
    
    for card in cards:
        try:
            titulo_tag = card.find('b', class_ = 'titulo')
            local_tag = card.find('span', class_ = 'local')
            horario_tag = card.find('span', class_ = 'horario')
        
            titulo = titulo_tag.text.strip() if titulo_tag else 'N/A'
            local = local_tag.text.strip() if local_tag else 'N/A'
            horario = horario_tag.text.strip() if local_tag else 'N/A'
            
            if titulo != 'N/A':
                filmes.append({
                    'Titulo' : titulo, 
                    'Local' : local,
                    'Horario' : horario
                })       
            else:
                print('Cartão sem titulo (ignorado)')   
        
            tempo = random.uniform(cardTempMin, cardTempMax)
            time.sleep(tempo)
        
        except Exception as e:
            print(f'Erro ao processar o cartão. Erro: {e}')
    
    tempo = random.uniform(pagTempoMin, pagTempoMax)
    time.sleep(tempo)

df = pd.DataFrame(filmes)
print(df.head())

df.to_csv(saidaCSV, index = False, encoding = 'utf-8-sig', quotechar = "'", quoting = 1)

conn = sqlite3.connect(bancoDados)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS shows(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Titulo TEXT,
        Local TEXT,
        Horario TEXT    
    )
''')

for evento in filmes :
    try:
        cursor.execute('''
        INSERT INTO shows (Titulo, Local, Horario) VALUES (?, ?, ?)                
''', (
    evento['Titulo'],
    evento['Local'],
    evento['Horario']
))
    except Exception as e:
        print(f'Erro ao inserir o evento {evento['Titulo']} no banco de dados. Codigo de identificação do erro: {e}')

conn.commit()
conn.close()
        
print('----------------------------------')
print('Dados raspados com sucesso!')
print('Obrigado por usar meu BOT')
print('Feito com ♥ por Guilherme Menezes')


