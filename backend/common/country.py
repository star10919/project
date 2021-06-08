class Country(object):
    name = '국가명'
    population = '인구'
    capital = '수도'

    def show(self):
        print('국가 클래스의 메소드입니다.')


class Korea(Country):
    def show_name(self):
        print(f'국가명은 {self.name}')


def main():    # 함수형 프로그래밍(class Country, class Korea를 사용)
    k = Korea()
    k.name = '대한민국'
    k.show_name()

main()