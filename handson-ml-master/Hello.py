import requests
from bs4 import BeautifulSoup
import pandas as pd

number = 18
name = '강기정'


url = '''
        https://www.lawmaking.go.kr/opnPtcp/nsmLmSts/out?sugCd={}&sgtCls=&cptOfiOrgCd=&searchStDtNew=&searchEdDtNew=
        &rslRsltNmL=&rslRsltNmR=&scCptPpostCmt=&scPpsUsr=%{}&scBlNo=&scBlNm=scBlNm_blNm&scBlNmSct=

      '''.format(number, name)


print(url)