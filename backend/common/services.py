import json
import pandas as pd
from common.abstracts import PrinterBase, ReaderBase

class Printer(PrinterBase):

    def dframe(self, this):
        print('*' * 100)
        print(f'1. 대상의 type\n{type(this)} 이다.')
        print(f'2. 대상의 column\n{this.columns} 이다.')
        print(f'3. 대상의 상위 5개 행\n{this.head()} 이다.')
        print(f'4. 대상의 null 의 갯수\n {this.isnull().sum()}개')
        print('*' * 100)


class Reader(ReaderBase):
    def new_file(self, file) -> str:
        return file._context + file._fname

    def csv(self, file) -> object:
        return pd.read_csv(f'{self.new_file(file)}.csv', thousands=',')   #encodings 화면깨짐방지

    def xls(self, file, header, usecols) -> object:
        return pd.read_excel(f'{self.new_file(file)}.xls', encodings='UTF-8', header=header, usecols=usecols)

    def json(self, file) -> object:
        return json.load(open(f'{self.new_file(file)}.json', encodings='UTF-8'))

    def test(self) -> object:
        pass