from real_estate.models import modelDto

import pandas as pd
import xlwings as xw

class housingService(object):
    dataset = modelDto()

    # DF 생성하기
    def new_model(self, payload) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        #df = pd.read_excel(this.context + this.fname + '.xlsx', sheet_name='평균전세')

        # 암호화된 엑셀 파일을 open하는데 쓰는 것이다.
        # sheet = xw.Book(this.context + payload + '.xlsx').sheets['매매종합']
        # row_num = sheet.range(1, 1).end('down').end('down').end('down').row
        # data_range = 'A2:GE' + str(row_num)
        # df = sheet[data_range].options(pd.DataFrame, index=False, headers=True).value
        return pd.read_excel(this.context + this.fname + '.xlsx')