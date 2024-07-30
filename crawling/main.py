from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from tqdm import tqdm

def crawling(soup):

    table = soup.find('table')
    ths = table.find_all('th')

    columns = []
    for idx, th in enumerate(ths):
        if idx == 4: continue
        columns.append(th.string)
    i = 0
    df = pd.DataFrame(columns=columns)
    trs = table.find_all('tr')

    for jdx, tr, in enumerate(trs):
        if jdx == 0: continue
        tds = tr.find_all('td')
        temps = []
        for idx, td in enumerate(tds):
            if idx == 4: continue
            temps.append(td.text)
        df.loc[i] = temps
        i += 1
    return df


if __name__ == "__main__":

    df = pd.DataFrame()

    page=1
    while tqdm(1):
        try:
            url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}"
            response = requests.get(url)
            html = response.text
            soup = bs(html, 'html.parser')
            result = crawling(soup)
            print(page)
            page +=1
        except Exception as ex :
            print(ex)
            break
        else:
            df = pd.concat([df, result])

    df.reset_index(inplace=True)
    df.to_csv("dataStorage/hollys.csv")
    print(df)
