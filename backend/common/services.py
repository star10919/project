class CommonService(object):

    def print_this(self, this):
        print('*' * 100)
        print(f'1. 대상의 type\n{type(this)} 이다.')
        print(f'2. 대상의 column\n{this.columns} 이다.')
        print(f'3. 대상의 상위 5개 행\n{this.head()} 이다.')
        print(f'4. 대상의 null 의 갯수\n {this.isnull().sum()}개')
        print('*' * 100)