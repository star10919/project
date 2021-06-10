from common.models import FileDTO
from common.services import Printer, Reader
from common.abstracts import ReaderBase

class CrimeService(ReaderBase):
    printer = Printer()
    reader = Reader()
    file = FileDTO()

    def csv(self, payload):    #payload는 리덕스에서 받는 값이구나!하고 생각하기
        self.file.context = payload.get('context')
        self.file.fname = payload.get('fname')
        self.printer.dframe(self.reader.csv(self.file))

    def xls(self, payload):
        self.file.context = payload.get('context')
        self.file.fname = payload.get('fname')
        self.printer.dframe(self.reader.xls(self.file, header=1, usecols=None))

    def json(self, payload):
        self.file.context = payload.get('context')
        self.file.fname = payload.get('fname')
        self.printer.dframe(self.reader.json(self.file))


    def new_file(self):
        pass

    # 추상클래스에 정의되지 않은 추가 메소드
    def test(self):
        pass
