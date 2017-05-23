from chat import *
from menu_list import *


# subway_sinsa = Subway('신사역점')
# worker = Worker(
#     subway = subway_sinsa,
#     name = '박보영'
# )


def main_list():
    print('---------------------------------')
    print('Subway 신사역 점에 오신걸 환영합니다')
    print('---------------------------------')
    while True:
        choice = input('====다음 메뉴를 선택해 주세요====\n1.메뉴선택\n2.계산하기\n3.기타주문사항\n4.주문완료\n메뉴를 입력하세요:')
        if choice == '4':
            print('-----------------------')
            print('주문이 완료되었습니다.')
            print('===== 감사합니다. =====')
            break
        elif choice == '1':

            menu_list()


        elif choice == '3':
            send_message()

if __name__ == '__main__':
    main_list()
