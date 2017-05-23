from models import SubwaySandwichOrder


def menu_list():
    print('-------------------------')
    print('주문 메뉴를 선택해 주세요')

    bread_type = list(bread_dict.keys())
    input('빵을 선택해 주세요\n1. {}\n2. {}\n3. {}\n'.format(
        bread_type[0],
        bread_type[1],
        bread_type[2]
    ))
    choiced_bread = bread_type[int(input()) - 1]

    meat_type = list(meat_dict.keys())
    input('패티를 선택해주세요\n1. {}\n2. {}\n3. {}\n'.format(
        meat_type[0],
        meat_type[1],
        meat_type[2]
    ))
    choiced_meat = meat_type[int(input()) - 1]

    sauce_type = list(sauce_dict.keys())
    input('소스를 선택해주세요\n1. {}\n2. {}\n3. {}\n'.format(
        sauce_type[0],
        sauce_type[1],
        sauce_type[2]
    ))
    choiced_sauce = sauce_type[int(input()) - 1]

    total_price = bread_dict[choiced_bread] + meat_dict[choiced_meat] + sauce_dict[choiced_sauce]
    SubwaySandwichOrder(choiced_bread, choiced_meat, choiced_sauce, total_price, False)



bread_dict = {
    '허니오트':1700,
    '파마산 오레가노':1800,
    '플랫 브래드':1500
}

meat_dict = {
    '미트볼':1500,
    '튜나':1600,
    '에그마요':1400
}

sauce_dict = {
    '랜치드레싱':500,
    '스위트 칠리':600,
    '사우스웨스트':700
}



