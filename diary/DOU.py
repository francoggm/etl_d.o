from .extractor_interface import IExtractor

import certifi
import datetime
import io

import urllib3

class DOU(IExtractor):
    def __init__(self):
        self.base_url = "https://pesquisa.in.gov.br/imprensa/servlet/INPDFViewer"
        self.format_url = "jornal={0}&pagina={1}&data={2}&captchafield=firstAccess"
        self.jornals = [515, 529, 530]
        self.extra_jornals = [600, 601]
        self.last_read = None
        self.date_now = None
        self.read_all = False

        self.headers = {
            'Content-Type': 'application/pdf',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en,pt-BR;q=0.8,pt;q=0.6',
            'Cache-Controle': 'no-cache',
            'Connection': 'keep-alive',
            'Host': 'pesquisa.in.gov.br',
            'Upgrade-Insecure-Requests': '1'
        }

    @staticmethod
    def verify_today_diary() -> bool:
        today = datetime.date.today().strftime("%d/%m/%Y")
        http = urllib3.HTTPSConnectionPool(host="pesquisa.in.gov.br", port=443, ca_certs=certifi.where())
        headers = {
            'Content-Type': 'application/pdf',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en,pt-BR;q=0.8,pt;q=0.6',
            'Cache-Controle': 'no-cache',
            'Connection': 'keep-alive',
            'Host': 'pesquisa.in.gov.br',
            'Upgrade-Insecure-Requests': '1'
        }

        for jornal in [515, 529, 530]:
            url = f"https://pesquisa.in.gov.br/imprensa/servlet/INPDFViewer?jornal={jornal}&pagina=1&data={today}&captchafield=firstAccess"

            try:
                http.request('GET', url, headers=headers)
                return True
            except urllib3.exceptions.HostChangedError:
                continue
        return False

    def extract(self):
        today = datetime.date.today().strftime("%d/%m/%Y")
        http = urllib3.HTTPSConnectionPool(host="pesquisa.in.gov.br", port=443, ca_certs=certifi.where())
        jornals = self.jornals[:] + self.extra_jornals[:]
        page = 1

        for jornal in jornals:
            while not self.read_all:
                url_format = self.base_url + "?" + self.format_url.format(jornal, page, today)
                print(f"Page={page}, Jornal={jornal}")
                try:
                    response = http.request('GET', url_format, headers=self.headers)
                    # if response.headers['Content-Type'] == 'application/pdf':
                    #     print(response.data)

                    page += 1
                except urllib3.exceptions.HostChangedError:
                    page = 1
                    break
                except:
                    break

    def transform(self):
        pass

    def load(self):
        pass

class DOUBuilder:
    pass