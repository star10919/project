from crime_cctv.models import CrimeDTO
from common.services import CommonService
import pandas as pd
import xlwings as xw

class CrimeService(CommonService):
    crime_DTO = CrimeDTO()

    def new_model_csv(self, payload) -> object:
        this = self.crime_DTO
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname + '.csv')

    def new_model_exel(self, payload) -> object:
        this = self.crime_DTO
        this.context = './data/'
        this.fname = payload
        return pd.read_excel(this.context + this.fname + '.xls')