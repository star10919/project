from real_estate.services import housingService
from common.services import CommonService

class Housing_API(CommonService):

    @staticmethod
    def main():
        ser = CommonService()
        util = housingService()
        while 1:
            menu = input('0-Exit 1-데이터프레임생성')
            if menu == '0':
                break
            elif menu == '1':
                this = util.new_model('kb_housing')
                ser.print_this(this)
            else:
                continue

Housing_API.main()