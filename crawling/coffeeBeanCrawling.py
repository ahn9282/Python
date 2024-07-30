import random

from driver.chrome_driver import chrome_driver
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re

if __name__ == "__main__":

    df = pd.DataFrame(columns=['메뉴', '설명', '열량', '포하지방', '낱륨', '탄수', '당', '카페인', '단4'])

    # URL 주소 설정
    url = "https://www.coffeebeankorea.com/member/login.asp#loginArea"
    # 크롬 창 띄우는 명령어
    driver = chrome_driver()
    # 크롬창 띄우는 명령어에 위 설정한 URL 넣어서 동작
    driver.get(url)
    # 띄운 창 최대 크기로 확대
    driver.maximize_window()
    #1~4 초 랜덤으로 시간 텀을 둠
    time.sleep(random.uniform(1, 2))

    # ID 칸
    username = driver.find_element(By.XPATH, '''//*[@id="loginForm"]/fieldset/div/div[1]/div[1]/div/p[1]/input''')
    # 비밀번호 입력 칸
    password = driver.find_element(By.XPATH, '''//*[@id="loginForm"]/fieldset/div/div[1]/div[1]/div/p[2]/input''')

    # ID 칸에 내 id 넣기
    username.send_keys("id")
    #1~4 초 랜덤으로 시간 텀을 둠
    time.sleep(random.uniform(1, 2))

    # 비밀번호 입력 칸에 비밀번호 넣기
    password.send_keys("password")
    #1~4 초 랜덤으로 시간 텀을 둠
    time.sleep(random.uniform(1, 2))

    # 로그인 버튼 클릭
    driver.find_element(By.XPATH, '''//*[@id="loginForm"]/fieldset/div/div[1]/div[1]/a''').click()
    #1~4 초 랜덤으로 시간 텀을 둠
    time.sleep(random.uniform(1, 2))

    # 메뉴 버튼 클릭
    driver.find_element(By.XPATH, '''//*[@id="gnb"]/ul/li[3]/a''').click()
    #1~4 초 랜덤으로 시간 텀을 둠
    time.sleep(random.uniform(1, 2))

    # 페이지 코드 가져옴
    html = driver.page_source

    # 전체 띄운 웹 페이지의 코드를 가져옴
    soup = BeautifulSoup(html, "html.parser")
    # 가져 온 코드에서 지정한 부분 가져옴 -> 이쪽 부터는 웹 페이지 관련 지식이 필요해서 일단 생략
    # 들어가서 로그인하고 넘어간 웹 페이지에서 웹페이지 코드를 가져와 골라꺼내서 확인하는 실습 내용
    ul = soup.select_one('''#contents > div > div > ul''')
    lis = ul.find_all('li')
    jdx = 0
    page = 4
    while (1):
        try:
            for i, li in enumerate(lis):
                menu = li.select_one(
                    f'''#contents > div > div > ul > li:nth-child({i + 1}) > dl > dt > span.kor''').text
                des = li.select_one(f'''#contents > div > div > ul > li:nth-child({i + 1}) > dl > dd''').text.strip()
                dls = li.find_all('dl')
                tmpList = [menu, des]
                for idx, dl in enumerate(dls):
                    if idx == 0: continue
                    number = re.sub(r'[^0-9]', '', dl.text)
                    tmpList.append(number)
                df.loc[jdx] = tmpList
                jdx += 1
            if page == 4:
                driver.find_element(By.XPATH, f'''//*[@id="contents"]/div/div/div/a[{page}]''').click()
                page += 1
            else:
                driver.find_element(By.XPATH, f'''//*[@id="contents"]/div/div/div/a[{page}]''').click()
            time.sleep(random.uniform(1, 4))
        except Exception as e:
            print(df)
            break
    print(df.to_csv("data/coffeebean.csv"))
    # print(lis[1])
    # page = 1
    # while page <= 3:
    #     try:
    #         for indexNum, li in enumerate(lis):
    #             menu = lis[indexNum].select_one( f'#contents > div > div > ul > li:nth-child({indexNum + 1}) > dl > dt > span.kor').text
    #             #print('menu : ',menu)
    #             des = lis[indexNum].select_one(f'#contents > div > div > ul > li:nth-child({indexNum + 1}) > dl > dd').text.strip()
    #             #print('des : ', des)
    #             dls = lis[indexNum].find_all('dl')
    #             #print('Length of dls',len(dls))
    #             tmpList = [menu, des]
    #
    #             for idx, dl in enumerate(dls):
    #                 if idx == 0: continue
    #                 number = re.sub("[^0-9]", "", dl.text)
    #                 tmpList.append(number)
    #
    #             df.loc[indexNum] = tmpList
    #             page += 1
    #         driver.find_element(By.XPATH, f'//*[@id="contents"]/div/div/div/a[{page}]').click()
    #     except Exception as ex:
    #         print("예외 발생!!")
    #         print(df)
    #         break


