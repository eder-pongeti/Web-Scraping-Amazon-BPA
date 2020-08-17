"""
@Make by Eder Pongeti
"""

from requests import get
from bs4 import BeautifulSoup

#URL = 'http://www.amazon.com.br/s?k=iphone'
#URL = 'https://www.amazon.in/gp/product/B0794JD9JS/ref=s9_acss_bw_cg_famcat1_3a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=DT9XVBR7CAEHX2W2S4ND&pf_rd_t=101&pf_rd_p=014d2fb9-0a03-415a-8da8-feb434b3d68f&pf_rd_i=14156834031'
URL = 'https://www.amazon.in/s?k=iphone&ref=nb_sb_noss_2'

headers = {
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"    
}

#fazendo a requisição à url
response = get(URL, headers=headers)

#Parseando a resposta da Requisição
page = BeautifulSoup(response.text, 'lxml')

for i in range(len(page.find_all('span', class_='celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results'))):
    
    produto = page.find('div', attrs={'class':'s-main-slot s-result-list s-search-results sg-row'}).find_all('div', attrs={'class':'s-include-content-margin s-border-bottom s-latency-cf-section'})[i].find('div', attrs={'class':'a-section a-spacing-medium'}).find('a', attrs={'class':'a-link-normal a-text-normal'}).find_all('span')[0].text.strip()
    preco = page.find_all('div', attrs={'class':'s-include-content-margin s-border-bottom s-latency-cf-section'})[i].find_all('span', attrs={'class':'a-offscreen'})[0].text.strip().replace(",",".")
    arquivo = open('amazon_produto.xls', 'a+')#Abre para gravação no modo append
    arquivo.write(f'\n {i+1} .'+produto+' ,'+preco)#Grava texto



    #nome do produto
    print(i+1,'.', 
    produto    
    )
    #preco do produto
    print(
        preco       
    
        )
    
arquivo.close()#Fecha o arquivo        
    

