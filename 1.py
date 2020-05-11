from flask import Flask, request
import logging
import json
from data import db_session
from data.__all_models import InfoRussia, InfoWorld
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)
logging.basicConfig(level=logging.INFO)
images = {
    'мир': "1030494/822b7834532e6e1bee43",
    'россия': "1030494/5fdd4125f486ed37ee53",
}
sessionStorage = {}




@app.route('/post', methods=['POST'])
def main():
    db_session.global_init("db/information.sqlite")
    user = InfoRussia()
    user.city = "Москва"
    user.illpeople = 115909
    session = db_session.create_session()
    session.add(user)
    user1 = InfoRussia()
    user1.city = "Московская область"
    user1.illpeople = 21637
    session.add(user1)
    user2 = InfoRussia()
    user2.city = "Санкт-Петербург"
    user2.illpeople = 7711
    session.add(user2)
    user3 = InfoRussia()
    user3.city = "Нижегородская область"
    user3.illpeople = 4733
    session.add(user3)
    user4 = InfoRussia()
    user4.city = "Республика Дагестан"
    user4.illpeople = 2772
    session.add(user4)
    user5 = InfoRussia()
    user5.city = "Мурманская область"
    user5.illpeople = 2416
    session.add(user5)
    user6 = InfoRussia()
    user6.city = "Краснодарский край"
    user6.illpeople = 2027
    session.add(user6)
    user7 = InfoRussia()
    user7.city = "Тульская область"
    user7.illpeople = 1881
    session.add(user7)
    user8 = InfoRussia()
    user8.city = "Ростовская область"
    user8.illpeople = 1851
    session.add(user8)
    user9 = InfoRussia()
    user9.city = "Калужская область"
    user9.illpeople = 1828
    session.add(user9)
    user10 = InfoRussia()
    user10.city = "Брянская область"
    user10.illpeople = 1678
    session.add(user10)
    user11 = InfoRussia()
    user11.city = "Свердловская область"
    user11.illpeople = 1952
    session.add(user11)
    user12 = InfoRussia()
    user12.city = "Республика Татарстан"
    user12.illpeople = 1761
    session.add(user12)
    user13 = InfoRussia()
    user13.city = "Рязанская область"
    user13.illpeople = 1744
    session.add(user13)
    user14 = InfoRussia()
    user14.city = "Республика Северная Осетия"
    user14.illpeople = 1647
    session.add(user14)
    user15 = InfoRussia()
    user15.city = "Ленинградская область"
    user15.illpeople = 1566
    session.add(user15)
    user16 = InfoRussia()
    user16.city = "Республика Башкортостан"
    user16.illpeople = 1567
    session.add(user16)
    user17 = InfoRussia()
    user17.city = "Курская область"
    user17.illpeople = 1484
    session.add(user17)
    user18 = InfoRussia()
    user18.city = "Владимирская область"
    user18.illpeople = 1326
    session.add(user18)
    user19 = InfoRussia()
    user19.city = "Республика Ингушетия"
    user19.illpeople = 1245
    session.add(user19)
    user20 = InfoRussia()
    user20.city = "Тамбовская область"
    user20.illpeople = 1403
    session.add(user20)
    user21 = InfoRussia()
    user21.city = "Республика Мордовия"
    user21.illpeople = 1190
    session.add(user21)
    user22 = InfoRussia()
    user22.city = "Ямало-Ненецкий автономный округ"
    user22.illpeople = 1239
    session.add(user22)
    user23 = InfoRussia()
    user23.city = "Кабардино-Балкарская Республика"
    user23.illpeople = 132
    session.add(user23)
    user24 = InfoRussia()
    user24.city = "Республика Чувашия"
    user24.illpeople = 1220
    session.add(user24)
    user25 = InfoRussia()
    user25.city = "Ярославская область"
    user25.illpeople = 1192
    session.add(user25)
    user26 = InfoRussia()
    user26.city = "Красноярский край"
    user26.illpeople = 1201
    session.add(user26)
    user27 = InfoRussia()
    user27.city = "Ставропольский край"
    user27.illpeople = 1084
    session.add(user27)
    user28 = InfoRussia()
    user28.city = "Новосибирская область"
    user28.illpeople = 1171
    session.add(user28)
    user29 = InfoRussia()
    user29.city = "Саратовская область"
    user29.illpeople = 1168
    session.add(user29)
    user30 = InfoRussia()
    user30.city = "Орловская область"
    user30.illpeople = 1087
    session.add(user30)
    user31 = InfoRussia()
    user31.city = "Челябинская область"
    user31.illpeople = 1232
    session.add(user31)
    user32 = InfoRussia()
    user32.city = "Республика Марий Эл"
    user32.illpeople = 928
    session.add(user32)
    user33 = InfoRussia()
    user33.city = "Оренбургская область"
    user33.illpeople = 986
    session.add(user33)
    user34 = InfoRussia()
    user34.city = "Республика Коми"
    user34.illpeople = 844
    session.add(user34)
    user35 = InfoRussia()
    user35.city = "Хабаровский край"
    user35.illpeople = 935
    session.add(user35)
    user36 = InfoRussia()
    user36.city = "Тверская область"
    user36.illpeople = 898
    session.add(user36)
    user37 = InfoRussia()
    user37.city = "Самарская область"
    user37.illpeople = 1017
    session.add(user37)
    user38 = InfoRussia()
    user38.city = "Волгоградская область"
    user38.illpeople = 1061
    session = db_session.create_session()
    session.add(user38)
    user2 = InfoRussia()
    user2.city = "Воронежская область"
    user2.illpeople = 899
    session.add(user2)
    user3 = InfoRussia()
    user3.city = "Приморский край"
    user3.illpeople = 907
    session.add(user3)
    user4 = InfoRussia()
    user4.city = "Липецкая область"
    user4.illpeople = 897
    session.add(user4)
    user5 = InfoRussia()
    user5.city = "Пермский край"
    user5.illpeople = 753
    session.add(user5)
    user6 = InfoRussia()
    user6.city = "Кировская область"
    user6.illpeople = 854
    session.add(user6)
    user7 = InfoRussia()
    user7.city = "Тюменская область"
    user7.illpeople = 832
    session.add(user7)
    user8 = InfoRussia()
    user8.city = "Чеченская Республика"
    user8.illpeople = 787
    session.add(user8)
    user9 = InfoRussia()
    user9.city = "Ульяновская область"
    user9.illpeople = 848
    session.add(user9)
    user = InfoRussia()
    user.city = "Пензенская область"
    user.illpeople = 802
    session.add(user)
    user1 = InfoRussia()
    user1.city = "Ивановская область"
    user1.illpeople = 843
    session.add(user1)
    user2 = InfoRussia()
    user2.city = "Смоленская область"
    user2.illpeople = 902
    session.add(user2)
    user3 = InfoRussia()
    user3.city = "Калининградская область"
    user3.illpeople = 753
    session.add(user3)
    user4 = InfoRussia()
    user4.city = "Астраханская область"
    user4.illpeople = 764
    session.add(user4)
    user5 = InfoRussia()
    user5.city = "Алтайский край"
    user5.illpeople = 707
    session.add(user5)
    user6 = InfoRussia()
    user6.city = "Белгородская область"
    user6.illpeople = 798
    session.add(user6)
    user7 = InfoRussia()
    user7.city = "Ханты-Мансийский АО"
    user7.illpeople = 777
    session.add(user7)
    user8 = InfoRussia()
    user8.city = "Республика Бурятия"
    user8.illpeople = 620
    session.add(user8)
    user9 = InfoRussia()
    user9.city = "Карачаево-Черкесская Республика"
    user9.illpeople = 539
    session.add(user9)
    user20 = InfoRussia()
    user20.city = "Новгородская область"
    user20.illpeople = 514
    session.add(user20)
    user21 = InfoRussia()
    user21.city = "Республика Саха"
    user21.illpeople = 551
    session.add(user21)
    user22 = InfoRussia()
    user22.city = "Республика Калмыкия"
    user22.illpeople = 494
    session.add(user22)
    user23 = InfoRussia()
    user23.city = "Архангельская область"
    user23.illpeople = 457
    session.add(user23)
    user24 = InfoRussia()
    user24.city = "Республика Хакасия"
    user24.illpeople = 466
    session.add(user24)
    user25 = InfoRussia()
    user25.city = "Камчатский край"
    user25.illpeople = 384
    session.add(user25)
    user26 = InfoRussia()
    user26.city = "Удмуртская Республика"
    user26.illpeople = 389
    session.add(user26)
    user27 = InfoRussia()
    user27.city = "Костромская область"
    user27.illpeople = 372
    session.add(user27)
    user28 = InfoRussia()
    user28.city = "Псковская область"
    user28.illpeople = 308
    session.add(user28)
    user29 = InfoRussia()
    user29.city = "Забайкальский край"
    user29.illpeople = 344
    session.add(user29)
    user30 = InfoRussia()
    user30.city = "Иркутская область"
    user30.illpeople = 314
    session.add(user30)
    user31 = InfoRussia()
    user31.city = "Вологодская область"
    user31.illpeople = 298
    session.add(user31)
    user32 = InfoRussia()
    user32.city = "Омская область"
    user32.illpeople = 302
    session.add(user32)
    user33 = InfoRussia()
    user33.city = "Республика Адыгея"
    user33.illpeople = 241
    session.add(user33)
    user34 = InfoRussia()
    user34.city = "Кемеровская область"
    user34.illpeople = 260
    session.add(user34)
    user35 = InfoRussia()
    user35.city = "Томская область"
    user35.illpeople = 279
    session.add(user35)
    user36 = InfoRussia()
    user36.city = "Еврейская автономная область"
    user36.illpeople = 185
    session.add(user36)
    user37 = InfoRussia()
    user37.city = "Республика Крым"
    user37.illpeople = 202
    session.add(user37)
    user38 = InfoRussia()
    user38.city = "Магаданская область"
    user38.illpeople = 155
    session.add(user38)
    user39 = InfoRussia()
    user39.city = "Республика Карелия"
    user39.illpeople = 160
    session.add(user39)
    user40 = InfoRussia()
    user40.city = "Амурская область"
    user40.illpeople = 152
    session.add(user40)
    user41 = InfoRussia()
    user41.city = "Севастополь"
    user41.illpeople = 126
    session.add(user41)
    user42 = InfoRussia()
    user42.city = "Курганская область"
    user42.illpeople = 79
    session.add(user42)
    user43 = InfoRussia()
    user43.city = "Республика Тыва"
    user43.illpeople = 93
    session.add(user43)
    user44 = InfoRussia()
    user44.city = "Ненецкий автономный округ"
    user44.illpeople = 50
    session.add(user44)
    user45 = InfoRussia()
    user45.city = "Республика Алтай"
    user45.illpeople = 54
    session.add(user45)
    user46 = InfoRussia()
    user46.city = "Сахалинская область"
    user46.illpeople = 38
    session.add(user46)
    user47 = InfoRussia()
    user47.city = "Чукотский автономный округ"
    user47.illpeople = 31
    session.add(user47)
    session.commit()

    users = InfoWorld()
    users.country = "США"
    users.illpeople = 1367963
    session = db_session.create_session()
    session.add(users)
    users1 = InfoWorld()
    users1.country = "Испания"
    users1.illpeople = 264663
    session.add(users1)
    users2 = InfoWorld()
    users2.country = "Италия"
    users2.illpeople = 219070
    session.add(users2)
    users3 = InfoWorld()
    users3.country = "Великобритания"
    users3.illpeople = 219183
    session.add(users3)
    users4 = InfoWorld()
    users4.country = "Россия"
    users4.illpeople = 221344
    session.add(users4)
    users5 = InfoWorld()
    users5.country = "Франция"
    users5.illpeople = 176970
    session.add(users5)
    users6 = InfoWorld()
    users6.country = "Германия"
    users6.illpeople = 171879
    session.add(users6)
    users6 = InfoWorld()
    users6.country = "Бразилия"
    users6.illpeople = 162699
    session.add(users6)
    users7 = InfoWorld()
    users7.country = "Турция"
    users7.illpeople = 138657
    session.add(users7)
    users8 = InfoWorld()
    users8.country = "Иран"
    users8.illpeople = 109286
    session.add(users8)
    users9 = InfoWorld()
    users9.country = "Китай"
    users9.illpeople = 82918
    session.add(users9)
    users10 = InfoWorld()
    users10.country = "Канада"
    users10.illpeople = 68848
    session.add(users10)
    users11 = InfoWorld()
    users11.country = "Перу"
    users11.illpeople = 67307
    session.add(users11)
    users12 = InfoWorld()
    users12.country = "Индия"
    users12.illpeople = 67700
    session.add(users12)
    users13 = InfoWorld()
    users13.country = "Бельгия"
    users13.illpeople = 53449
    session.add(users13)
    users14 = InfoWorld()
    users14.country = "Нидерланды"
    users14.illpeople = 42627
    session.add(users14)
    users15 = InfoWorld()
    users15.country = "Саудовская Аравия"
    users15.illpeople = 39048
    session.add(users15)
    users16 = InfoWorld()
    users16.country = "Эквадор"
    users16.illpeople = 29559
    session.add(users16)
    users17 = InfoWorld()
    users17.country = "Швейцария"
    users17.illpeople = 30344
    session.add(users17)
    users18 = InfoWorld()
    users18.country = "Мексика"
    users18.illpeople = 35022
    session.add(users18)
    users19 = InfoWorld()
    users19.country = "Португалия"
    users19.illpeople = 27581
    session.add(users19)
    users20 = InfoWorld()
    users20.country = "Пакистан"
    users20.illpeople = 30941
    session.add(users20)
    users21 = InfoWorld()
    users21.country = "Швеция"
    users21.illpeople = 26322
    session.add(users1)
    users22 = InfoWorld()
    users22.country = "Чили"
    users22.illpeople = 28866
    session.add(users22)
    users23 = InfoWorld()
    users23.country = "Ирландия"
    users23.illpeople = 22996
    session.add(users23)
    users24 = InfoWorld()
    users24.country = "Сингапур"
    users24.illpeople = 23822
    session.add(users24)
    users25 = InfoWorld()
    users25.country = "Беларусь"
    users25.illpeople = 23906
    session.add(users25)
    users26 = InfoWorld()
    users26.country = "Катар"
    users26.illpeople = 22520
    session.add(users26)
    users27 = InfoWorld()
    users27.country = "Израиль"
    users27.illpeople = 16492
    session.add(users27)
    users28 = InfoWorld()
    users28.country = "Объединённые Арабские Эмираты"
    users28.illpeople = 18198
    session.add(users28)
    users29 = InfoWorld()
    users29.country = "Австрия"
    users29.illpeople = 15882
    session.add(users29)
    users30 = InfoWorld()
    users30.country = "Япония"
    users30.illpeople = 15777
    session.add(users30)
    users31 = InfoWorld()
    users31.country = "Польша"
    users31.illpeople = 16206
    session.add(users31)
    users32 = InfoWorld()
    users32.country = "Румыния"
    users32.illpeople = 15588
    session.add(users32)
    users33 = InfoWorld()
    users33.country = "Украина"
    users33.illpeople = 15648
    session.add(users33)
    users34 = InfoWorld()
    users34.country = "Бангладеш"
    users34.illpeople = 15691
    session.add(users34)
    users35 = InfoWorld()
    users35.country = "Индонезия"
    users35.illpeople = 14265
    session.add(users35)
    users36 = InfoWorld()
    users36.country = "Южная Корея"
    users36.illpeople = 10909
    session.add(users36)
    users37 = InfoWorld()
    users37.country = "Филиппины"
    users37.illpeople = 11086
    session.add(users37)
    users38 = InfoWorld()
    users38.country = "Дания"
    users38.illpeople = 10513
    session.add(users38)
    users39 = InfoWorld()
    users39.country = "Сербия"
    users39.illpeople = 10114
    session.add(users39)
    users40 = InfoWorld()
    users40.country = "Колумбия"
    users40.illpeople = 11063
    session.add(users40)
    users41 = InfoWorld()
    users41.country = "Доминиканская Республика"
    users41.illpeople = 10347
    session.add(users41)
    users42 = InfoWorld()
    users42.country = "ЮАР"
    users42.illpeople = 10015
    session.add(users42)
    users43 = InfoWorld()
    users43.country = "Норвегия"
    users43.illpeople = 8105
    session.add(users43)
    users44 = InfoWorld()
    users44.country = "Чехия"
    users44.illpeople = 8123
    session.add(users44)
    users45 = InfoWorld()
    users45.country = "Египет"
    users45.illpeople = 9400
    session.add(users45)
    users46 = InfoWorld()
    users46.country = "Панама"
    users46.illpeople = 8448
    session.add(users46)
    users47 = InfoWorld()
    users47.country = "Австралия"
    users47.illpeople = 6948
    session.add(users47)
    users48 = InfoWorld()
    users48.country = "Кувейт"
    users48.illpeople = 8688
    session.add(users48)
    users49 = InfoWorld()
    users49.country = "Малайзия"
    users49.illpeople = 6726
    session.add(users49)
    users50 = InfoWorld()
    users50.country = "Финляндия"
    users50.illpeople = 5984
    session.add(users50)
    users51 = InfoWorld()
    users51.country = "Марокко"
    users51.illpeople = 6226
    session.add(users51)
    users52 = InfoWorld()
    users52.country = "Аргентина"
    users52.illpeople = 6034
    session.add(users52)
    users53 = InfoWorld()
    users53.country = "Алжир"
    users53.illpeople = 5723
    session.add(users53)
    users54 = InfoWorld()
    users54.country = "Казахстан"
    users54.illpeople = 5138
    session.add(users54)
    users55 = InfoWorld()
    users55.country = "Молдова"
    users55.illpeople = 4927
    session.add(users55)
    users56 = InfoWorld()
    users56.country = "Бахрейн"
    users6.illpeople = 4941
    session.add(users56)
    users57 = InfoWorld()
    users57.country = "Люксембург"
    users57.illpeople = 3886
    session.add(users57)
    users58 = InfoWorld()
    users58.country = "Афганистан"
    users58.illpeople = 4687
    session.add(users58)
    users59 = InfoWorld()
    users59.country = "Нигерия"
    users59.illpeople = 4399
    session.add(users59)
    users60 = InfoWorld()
    users60.country = "Венгрия"
    users60.illpeople = 3284
    session.add(users60)
    users61 = InfoWorld()
    users61.country = "Оман"
    users61.illpeople = 3573
    session.add(users61)
    users62 = InfoWorld()
    users62.country = "Гана"
    users62.illpeople = 4700
    session.add(users62)
    users63 = InfoWorld()
    users63.country = "Армения"
    users63.illpeople = 3392
    session.add(users63)
    users4 = InfoWorld()
    users4.country = "Таиланд"
    users4.illpeople = 3015
    session.add(users4)
    users5 = InfoWorld()
    users5.country = "Греция"
    users5.illpeople = 2716
    session.add(users5)
    users6 = InfoWorld()
    users6.country = "Ирак"
    users6.illpeople = 2767
    session.add(users6)
    users7 = InfoWorld()
    users7.country = "Узбекистан"
    users7.illpeople = 2453
    session.add(users7)
    users8 = InfoWorld()
    users8.country = "Камерун"
    users8.illpeople = 2579
    session.add(users8)
    users9 = InfoWorld()
    users9.country = "Азербайджан"
    users9.illpeople = 2519
    session.add(users9)
    users = InfoWorld()
    users.country = "Хорватия"
    users.illpeople = 2187
    session.add(users)
    users1 = InfoWorld()
    users1.country = "Боливия"
    users1.illpeople = 2556
    session.add(users1)
    users2 = InfoWorld()
    users2.country = "Босния и Герцеговина"
    users2.illpeople = 2117
    session.add(users2)
    users3 = InfoWorld()
    users3.country = "Гвинея"
    users3.illpeople = 2146
    session.add(users3)
    users4 = InfoWorld()
    users4.country = "Болгария"
    users4.illpeople = 1981
    session.add(users4)
    users5 = InfoWorld()
    users5.country = "Исландия"
    users5.illpeople = 1801
    session.add(users5)
    users6 = InfoWorld()
    users6.country = "Куба"
    users6.illpeople = 1766
    session.add(users6)
    users7 = InfoWorld()
    users7.country = "Эстония"
    users7.illpeople = 1741
    session.add(users7)
    users8 = InfoWorld()
    users8.country = "Гондурас"
    users8.illpeople = 1972
    session.add(users8)
    users9 = InfoWorld()
    users9.country = "Северная Македония"
    users9.illpeople = 1664
    session.add(users9)
    users = InfoWorld()
    users.country = "Кот-д’Ивуар"
    users.illpeople = 1700
    session.add(users)
    users1 = InfoWorld()
    users1.country = "Сенегал"
    users1.illpeople = 1709
    session.add(users1)
    users2 = InfoWorld()
    users2.country = "Новая Зеландия"
    users2.illpeople = 1497
    session.add(users2)
    users3 = InfoWorld()
    users3.country = "Словакия"
    users3.illpeople = 1457
    session.add(users3)
    users4 = InfoWorld()
    users4.country = "Словения"
    users4.illpeople = 1460
    session.add(users4)
    users5 = InfoWorld()
    users5.country = "Литва"
    users5.illpeople = 1485
    session.add(users5)
    users6 = InfoWorld()
    users6.country = "Джибути"
    users6.illpeople = 1210
    session.add(users6)
    users7 = InfoWorld()
    users7.country = "Тунис"
    users7.illpeople = 1032
    session.add(users7)
    users8 = InfoWorld()
    users8.country = "Судан"
    users8.illpeople = 1365
    session.add(users8)
    users9 = InfoWorld()
    users9.country = "Латвия"
    users9.illpeople = 946
    session.add(users9)
    users = InfoWorld()
    users.country = "Сомали"
    users.illpeople = 1054
    session.add(users)
    users1 = InfoWorld()
    users1.country = "Киргизия"
    users1.illpeople = 1016
    session.add(users1)
    users2 = InfoWorld()
    users2.country = "Демократическая Республика Конго"
    users2.illpeople = 991
    session.add(users2)
    users3 = InfoWorld()
    users3.country = "Кипр"
    users3.illpeople = 898
    session.add(users3)
    users4 = InfoWorld()
    users4.country = "Албания"
    users4.illpeople = 872
    session.add(users4)
    users5 = InfoWorld()
    users5.country = "Гватемала"
    users5.illpeople = 1052
    session.add(users5)
    users6 = InfoWorld()
    users6.country = "Шри-Ланка"
    users6.illpeople = 863
    session.add(users6)
    users7 = InfoWorld()
    users7.country = "Ливан"
    users7.illpeople = 845
    session.add(users7)
    users8 = InfoWorld()
    users8.country = "Нигер"
    users8.illpeople = 821
    session.add(users8)
    users9 = InfoWorld()
    users9.country = "Коста-Рика"
    users9.illpeople = 792
    session.add(users9)
    users = InfoWorld()
    users.country = "Андорра"
    users.illpeople = 755
    session.add(users)
    users1 = InfoWorld()
    users1.country = "Сальвадор"
    users1.illpeople = 958
    session.add(users1)
    users2 = InfoWorld()
    users2.country = "Буркина-Фасо"
    users2.illpeople = 751
    session.add(users2)
    users3 = InfoWorld()
    users3.country = "Уругвай"
    users3.illpeople = 707
    session.add(users3)
    users4 = InfoWorld()
    users4.country = "Мали"
    users4.illpeople = 704
    session.add(users4)
    users5 = InfoWorld()
    users5.country = "Мальдивы"
    users5.illpeople = 835
    session.add(users5)
    users6 = InfoWorld()
    users6.country = "Грузия"
    users6.illpeople = 638
    session.add(users6)
    users7 = InfoWorld()
    users7.country = "Сан-Марино"
    users7.illpeople = 628
    session.add(users7)
    users8 = InfoWorld()
    users8.country = "Кения"
    users8.illpeople = 672
    session.add(users8)
    users9 = InfoWorld()
    users9.country = "Гвинея-Бисау"
    users9.illpeople = 726
    session.add(users9)
    users = InfoWorld()
    users.country = "Габон"
    users.illpeople = 661
    session.add(users)
    users1 = InfoWorld()
    users1.country = "Иордания"
    users1.illpeople = 540
    session.add(users1)
    users2 = InfoWorld()
    users2.country = "Ямайка"
    users2.illpeople = 502
    session.add(users2)
    users3 = InfoWorld()
    users3.country = "Мальта"
    users3.illpeople = 503
    session.add(users3)
    users4 = InfoWorld()
    users4.country = "Танзания"
    users4.illpeople = 509
    session.add(users4)
    users5 = InfoWorld()
    users5.country = "Парагвай"
    users5.illpeople = 713
    session.add(users5)
    users6 = InfoWorld()
    users6.country = "Таджикистан"
    users6.illpeople = 612
    session.add(users6)
    users7 = InfoWorld()
    users7.country = "Экваториальная Гвинея"
    users7.illpeople = 439
    session.add(users7)
    users8 = InfoWorld()
    users8.country = "Венесуэла"
    users8.illpeople = 414
    session.add(users8)
    users9 = InfoWorld()
    users9.country = "Маврикий"
    users9.illpeople = 332
    session.add(users9)
    users = InfoWorld()
    users.country = "Черногория"
    users.illpeople = 324
    session.add(users)
    users1 = InfoWorld()
    users1.country = "Вьетнам"
    users1.illpeople = 288
    session.add(users1)
    users2 = InfoWorld()
    users2.country = "Республика Конго"
    users2.illpeople = 274
    session.add(users2)
    users3 = InfoWorld()
    users3.country = "Руанда"
    users3.illpeople = 284
    session.add(users3)
    users4 = InfoWorld()
    users4.country = "Чад"
    users4.illpeople = 322
    session.add(users4)
    users5 = InfoWorld()
    users5.country = "Сьерра-Леоне"
    users5.illpeople = 307
    session.add(users5)
    users6 = InfoWorld()
    users6.country = "Кабо-Верде"
    users6.illpeople = 246
    session.add(users6)
    users7 = InfoWorld()
    users7.country = "Мадагаскар"
    users7.illpeople = 193
    session.add(users7)
    users8 = InfoWorld()
    users8.country = "Эфиопия"
    users8.illpeople = 250
    session.add(users8)
    users9 = InfoWorld()
    users9.country = "Либерия"
    users9.illpeople = 199
    session.add(users9)
    users = InfoWorld()
    users.country = "Сан-Томе и Принсипи"
    users.illpeople = 208
    session.add(users)
    users1 = InfoWorld()
    users1.country = "Мьянма"
    users1.illpeople = 180
    session.add(users1)
    users2 = InfoWorld()
    users2.country = "Замбия"
    users2.illpeople = 267
    session.add(users2)
    users3 = InfoWorld()
    users3.country = "Эсватини"
    users3.illpeople = 172
    session.add(users3)
    users4 = InfoWorld()
    users4.country = "Бруней"
    users4.illpeople = 141
    session.add(users4)
    users5 = InfoWorld()
    users5.country = "Бенин"
    users5.illpeople = 319
    session.add(users5)
    users6 = InfoWorld()
    users6.country = "Того"
    users6.illpeople = 174
    session.add(users6)
    users7 = InfoWorld()
    users7.country = "Гаити"
    users7.illpeople = 182
    session.add(users7)
    users8 = InfoWorld()
    users8.country = "Камбоджа"
    users8.illpeople = 122
    session.add(users8)
    users9 = InfoWorld()
    users9.country = "Тринидад и Тобаго"
    users9.illpeople = 116
    session.add(users9)
    users = InfoWorld()
    users.country = "Непал"
    users.illpeople = 121
    session.add(users)
    users1 = InfoWorld()
    users1.country = "Уганда"
    users1.illpeople = 121
    session.add(users1)
    users2 = InfoWorld()
    users2.country = "Монако"
    users2.illpeople = 96
    session.add(users2)
    users3 = InfoWorld()
    users3.country = "Центральноафриканская республика"
    users3.illpeople = 143
    session.add(users3)
    users4 = InfoWorld()
    users4.country = "Гайана"
    users4.illpeople = 104
    session.add(users4)
    users5 = InfoWorld()
    users5.country = "Багамские острова"
    users5.illpeople = 92
    session.add(users5)
    users6 = InfoWorld()
    users6.country = "Барбадос"
    users6.illpeople = 84
    session.add(users6)
    users7 = InfoWorld()
    users7.country = "Лихтенштейн"
    users7.illpeople = 82
    session.add(users7)
    users8 = InfoWorld()
    users8.country = "Мозамбик"
    users8.illpeople = 91
    session.add(users8)
    users9 = InfoWorld()
    users9.country = "Южный Судан"
    users9.illpeople = 156
    session.add(users9)
    users = InfoWorld()
    users.country = "Ливия"
    users.illpeople = 64
    session.add(users)
    users1 = InfoWorld()
    users1.country = "Сирия"
    users1.illpeople = 47
    session.add(users1)
    users2 = InfoWorld()
    users2.country = "Малави"
    users2.illpeople = 56
    session.add(users2)
    users3 = InfoWorld()
    users3.country = "Монголия"
    users3.illpeople = 42
    session.add(users3)
    users4 = InfoWorld()
    users4.country = "Эритрея"
    users4.illpeople = 39
    session.add(users4)
    users5 = InfoWorld()
    users5.country = "Ангола"
    users5.illpeople = 45
    session.add(users5)
    users6 = InfoWorld()
    users6.country = "Зимбабве"
    users6.illpeople = 36
    session.add(users6)
    users7 = InfoWorld()
    users7.country = "Антигуа и Барбуда"
    users7.illpeople = 25
    session.add(users7)
    users8 = InfoWorld()
    users8.country = "Йемен"
    users8.illpeople = 51
    session.add(users8)
    users9 = InfoWorld()
    users9.country = "Восточный Тимор"
    users9.illpeople = 24
    session.add(users9)
    users = InfoWorld()
    users.country = "Ботсвана"
    users.illpeople = 23
    session.add(users)
    users1 = InfoWorld()
    users1.country = "Гренада"
    users1.illpeople = 21
    session.add(users1)
    users2 = InfoWorld()
    users2.country = "Лаос"
    users2.illpeople = 19
    session.add(users2)
    users3 = InfoWorld()
    users3.country = "Белиз"
    users3.illpeople = 18
    session.add(users3)
    users4 = InfoWorld()
    users4.country = "Гамбия"
    users4.illpeople = 20
    session.add(users4)
    users5 = InfoWorld()
    users5.country = "Сент-Люсия"
    users5.illpeople = 18
    session.add(users5)
    users6 = InfoWorld()
    users6.country = "Фиджи"
    users6.illpeople = 18
    session.add(users6)
    users7 = InfoWorld()
    users7.country = "Сент-Винсент и Гренадины"
    users7.illpeople = 17
    session.add(users7)
    users8 = InfoWorld()
    users8.country = "Доминика"
    users8.illpeople = 16
    session.add(users8)
    users9 = InfoWorld()
    users9.country = "Намибия"
    users9.illpeople = 16
    session.add(users9)
    users = InfoWorld()
    users.country = "Никарагуа"
    users.illpeople = 16
    session.add(users)
    users1 = InfoWorld()
    users1.country = "Бурунди"
    users1.illpeople = 15
    session.add(users1)
    users2 = InfoWorld()
    users2.country = "Сент-Китс и Невис"
    users2.illpeople = 15
    session.add(users2)
    users3 = InfoWorld()
    users3.country = "Ватикан"
    users3.illpeople = 12
    session.add(users3)
    users4 = InfoWorld()
    users4.country = "Сейшельские острова"
    users4.illpeople = 11
    session.add(users4)
    users5 = InfoWorld()
    users5.country = "Суринам"
    users5.illpeople = 10
    session.add(users5)
    users6 = InfoWorld()
    users6.country = "Коморские острова"
    users6.illpeople = 11
    session.add(users6)
    users7 = InfoWorld()
    users7.country = "Мавритания"
    users7.illpeople = 8
    session.add(users7)
    users8 = InfoWorld()
    users8.country = "Папуа-Новая Гвинея"
    users8.illpeople = 8
    session.add(users8)
    users9 = InfoWorld()
    users9.country = "Бутан"
    users9.illpeople = 9
    session.add(users9)
    users = InfoWorld()
    users.country = "Сахарская Арабская Демократическая Республика"
    users.illpeople = 6
    session.add(users)
    session.commit()
    logging.info('Request: %r', request.json)
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }
    handle_dialog(response, request.json)
    logging.info('Response: %r', response)
    return json.dumps(response)


def handle_dialog(res, req):
    user_id = req['session']['user_id']
    if req['session']['new']:
        res['response']['text'] = 'Привет! Как тебя зовут?'
        sessionStorage[user_id] = {
            'first_name': None,  # здесь будет храниться имя
            'information': False  # здесь информация о том, что пользователь запросил информацию. По умолчанию False
        }
        return

    if sessionStorage[user_id]['first_name'] is None:
        first_name = get_first_name(req)
        if first_name is None:
            res['response']['text'] = 'Не расслышала имя. Повтори, пожалуйста!'
        else:
            sessionStorage[user_id]['first_name'] = first_name

            res['response']['text'] = f'Приятно познакомиться, {first_name.title()}. Я Алиса. Что ты хочешь узнать?'
            res['response']['buttons'] = [
                {
                    'title': 'Информация про субъект Российской Федерации',
                    'hide': True
                },
                {
                    'title': 'Информация про страны мира',
                    'hide': True
                },
                {
                    'title': 'Симптомы',
                    'hide': True
                },
                {
                    'title': 'Рекомендации',
                    'hide': True
                },
                {
                    'title': "Чем заняться в карантин?",
                    'hide': True
                }
            ]
    else:
        if not sessionStorage[user_id]['information']:
            # запрос не поступил, значит мы ожидаем запрос.
            if ('Информация про субъект Российской Федерации' in req['request']['nlu']['tokens'] or
                    'информация про субъект Российской Федерации' in req['request']['nlu']['tokens'] or
                    "информация про город" in req['request']['nlu']['tokens'] or "Информация про город" in
                    req['request']['nlu']['tokens']):
                sessionStorage[user_id]['information'] = True
                # вызываем необходимую функцию

            elif 'Информация про страну' in req['request']['nlu']['tokens'] or \
                    'информация про страну' in req['request']['nlu']['tokens']:
                sessionStorage[user_id]['information'] = True
                # вызываем необходимую функцию

            elif 'Симптомы' in req['request']['nlu']['tokens'] or 'симптомы' in req['request']['nlu']['tokens']:
                sessionStorage[user_id]['information'] = True
                symptomes(res, req)

            elif 'Рекомендации' in req['request']['nlu']['tokens'] or 'рекомендации' in req['request']['nlu']['tokens']:
                sessionStorage[user_id]['information'] = True
                recomendation(res, req)

            elif ('Чем заняться в карантин?' in req['request']['nlu']['tokens'] or
                    'чем заняться в карантин?' in req['request']['nlu']['tokens'] or
                    "чем заняться на самоизоляции?" in req['request']['nlu']['tokens'] or
                    "Чем заняться на самоизоляции?" in req['request']['nlu']['tokens'] or
                    "чем заняться во время самоизоляции?" in req['request']['nlu']['tokens'] or
                    "Чем заняться во время самоизоляции?" in req['request']['nlu']['tokens'] or
                    "Чем заняться?" in req['request']['nlu']['tokens'] or
                    "Что делать?" in req['request']['nlu']['tokens'] or
                    "что делать?" in req['request']['nlu']['tokens'] or
                    'Что делать? в карантин?' in req['request']['nlu']['tokens'] or
                    'что делать? в карантин?' in req['request']['nlu']['tokens'] or
                    "чем заняться?" in req['request']['nlu']['tokens'] or
                    "что делать? на самоизоляции?" in req['request']['nlu']['tokens'] or
                    "Что делать? на самоизоляции?" in req['request']['nlu']['tokens'] or
                    "что делать? во время самоизоляции?" in req['request']['nlu']['tokens'] or
                    "Что делать? во время самоизоляции?" in req['request']['nlu']['tokens']):
                sessionStorage[user_id]['information'] = True
                stay_home(res, req)
            else:
                res['response']['text'] = ('К сожалению у меня нет такого раздела. Выберите из перечисленных' +
                                           ' или перейдите на официальный сайт, где такая информация может быть.')
                res['response']['buttons'] = [
                    {
                        'title': 'Информация про субъект Российской Федерации',
                        'hide': True
                    },
                    {
                        'title': 'Информация про страны мира',
                        'hide': True
                    },
                    {
                        'title': 'Симптомы',
                        'hide': True
                    },
                    {
                        'title': 'Рекомендации',
                        'hide': True
                    },
                    {
                        'title': "Чем заняться в карантин?",
                        'hide': True
                    }
                ]
        else:
            if ('Информация про субъект Российской Федерации' in req['request']['nlu']['tokens'] or
                    'информация про субъект Российской Федерации' in req['request']['nlu']['tokens'] or
                    "информация про город" in req['request']['nlu']['tokens'] or
                    "Информация про город" in req['request']['nlu']['tokens']):
                sessionStorage[user_id]['information'] = True
                # вызываем необходимую функц
            elif 'Информация про страну' in req['request']['nlu']['tokens'] or \
                    'информация про страну' in req['request']['nlu']['tokens']:
                sessionStorage[user_id]['information'] = True
                # вызываем необходимую функцию

            elif 'Симптомы' in req['request']['nlu']['tokens'] or 'симптомы' in req['request']['nlu']['tokens']:
                sessionStorage[user_id]['information'] = True
                # вызываем необходимую функцию
                symptomes(res, req)
            elif 'Рекомендации' in req['request']['nlu']['tokens'] or 'рекомендации' in req['request']['nlu']['tokens']:
                sessionStorage[user_id]['information'] = True
                # вызываем необходимую функцию
                recomendation(res, req)
            elif 'Чем заняться в карантин?' in req['request']['nlu']['tokens'] or \
                    'чем заняться в карантин?' in req['request']['nlu']['tokens'] or \
                    "чем заняться на самоизоляции?" in req['request']['nlu']['tokens'] or \
                    "Чем заняться на самоизоляции?" in req['request']['nlu']['tokens'] or \
                    "чем заняться во время самоизоляции?" in req['request']['nlu']['tokens'] or \
                    "Чем заняться во время самоизоляции?" in req['request']['nlu']['tokens'] or \
                    "Чем заняться?" in req['request']['nlu']['tokens'] or \
                    "Что делать?" in req['request']['nlu']['tokens'] or \
                    "что делать?" in req['request']['nlu']['tokens'] or \
                    'Что делать? в карантин?' in req['request']['nlu']['tokens'] or \
                    'что делать? в карантин?' in req['request']['nlu']['tokens'] or \
                    "чем заняться?" in req['request']['nlu']['tokens'] or \
                    "что делать? на самоизоляции?" in req['request']['nlu']['tokens'] or \
                    "Что делать? на самоизоляции?" in req['request']['nlu']['tokens'] or \
                    "что делать? во время самоизоляции?" in req['request']['nlu']['tokens'] or \
                    "Что делать? во время самоизоляции?" in req['request']['nlu']['tokens']:
                sessionStorage[user_id]['information'] = True
                # вызываем необходимую функцию
                stay_home(res, req)


def symptomes(res, req):
    user_id = req['session']['user_id']
    res['response']['text'] = "".join(['Основными признаками наличия коронавируса у человека являются:' +
                                       'слабость, усталость,',
                                       ' затрудненное дыхание,',
                                       ' высокая температура,',
                                       ' кашель (сухой или с небольшим количеством мокроты) и/или боль в горле,',
                                       'По симптоматике коронавирус схож с простудой' +
                                       ' и респираторными заболеваниями.',
                                       'Особое внимание стоит обратить на одышку:' +
                                       ' при ее наличии немедленно обратитесь к врачу.'])
    sessionStorage[user_id]['information'] = False
    res['response']['buttons'] = [
        {
            'title': 'Информация про субъект Российской Федерации',
            'hide': True
        },
        {
            'title': 'Информация про страны мира',
            'hide': True
        },
        {
            'title': 'Симптомы',
            'hide': True
        },
        {
            'title': 'Рекомендации',
            'hide': True
        },
        {
            'title': "Чем заняться в карантин?",
            'hide': True
        }
    ]


def recomendation(res, req):
    user_id = req['session']['user_id']
    res['response']['text'] = "sep=\n".join(['Регулярно обрабатывайте руки спиртосодержащим средством' +
                                             ' или мойте их с мылом. ',
                                             'Держитесь от людей на расстоянии как минимум 1 метра, особенно если у' +
                                             ' них кашель, насморк и повышенная температура.',
                                             'По возможности, не трогайте руками глаза, нос и рот.',
                                             'При кашле и чихании прикрывайте рот и нос салфеткой или сгибом локтя;' +
                                             ' сразу выкидывайте салфетку в контейнер для мусора с крышкой и' +
                                             ' обрабатывайте руки спиртосодержащим антисептиком или мойте их' +
                                             ' водой с мылом.',
                                             'При повышении температуры, появлении кашля и затруднении дыхания как' +
                                             ' можно быстрее обращайтесь за медицинской помощью.',
                                             'По симптоматике коронавирус схож с простудой' +
                                             ' и респираторными заболеваниями.',
                                             'Следите за новейшей информацией и выполняйте рекомендации медицинских' +
                                             ' специалистов.'])
    sessionStorage[user_id]['information'] = False
    res['response']['buttons'] = [
        {
            'title': 'Информация про субъект Российской Федерации',
            'hide': True
        },
        {
            'title': 'Информация про страны мира',
            'hide': True
        },
        {
            'title': 'Симптомы',
            'hide': True
        },
        {
            'title': 'Рекомендации',
            'hide': True
        },
        {
            'title': "Чем заняться в карантин?",
            'hide': True
        }
    ]


def stay_home(res, req):
    user_id = req['session']['user_id']
    res['response']['text'] = "sep=\n".join(['Все по-разному проводят время на карантине, но есть несколько полезных' +
                                             ' советов, как получить от самоизляции удовольствие и пользу.',
                                             '1)Первым делом, не стоит забывать про учебу или работу. Во время' +
                                             ' карантина мы советуем регулярно укреплять или усовершенствовать свои' +
                                             ' навыки или знания. Многие обучающие площадки устраивают бесплатные' +
                                             ' тренинги и курсы. почему бы не воспользоваться этим?',
                                             "2)Займитесь своим любимым хобби! Ничто не поможет" +
                                             " провести карантин лучше, чем приятное сердцу дело!",
                                             "3) Займитесь спортом и своим здоровьем. Отличный шанс улучшить свое" +
                                             " физическое состояние и не испортить фигуру за время карантина!",
                                             "4) Не забывайте про развлечения! Посмотрите кино или сериалы, которые" +
                                             " давно хотели, сыграйте в компьютерные или настольные игры с родными," +
                                             " проведите время с домашним питомцем или, в конце концов, поиграйте со" +
                                             " мной! Послушайте любимую музыку или посмотрите онлайн-концерты" +
                                             " исполнителей, которых вы любите, или знакомьтесь с новыми!",
                                             "5)Помогите окружающим! Многие в сложившейся ситуации нуждаются в помощи" +
                                             " и поддержке, если у вас есть возможность, совершите доброе дело!"])
    sessionStorage[user_id]['information'] = False
    res['response']['buttons'] = [
        {
            'title': 'Информация про субъект Российской Федерации',
            'hide': True
        },
        {
            'title': 'Информация про страны мира',
            'hide': True
        },
        {
            'title': 'Симптомы',
            'hide': True
        },
        {
            'title': 'Рекомендации',
            'hide': True
        },
        {
            'title': "Чем заняться в карантин?",
            'hide': True
        }
    ]


def inforussia(res, req):
    user_id = req['session']['user_id']
    cur = con.cursor()
    sp = cur.execute("""SELECT illpeople FROM russia""").fetchall()
    if req['request']['nlu']['tokens'] in sp:
        result = cur.execute("""SELECT illpeople FROM russia WHERE
    territory == {0}""".format(req['request']['nlu']['tokens'])).fetchone()
    else:
        result = 'Я не расслышала. Попробуйте еще раз.'
    res['response']['text'] = result
    res['response']['card'] = {}
    res['response']['card']['type'] = 'BigImage'
    res['response']['card']['title'] = 'Заражение в России'
    res['response']['card']['image_id'] = images['россия']
    sessionStorage[user_id]['information'] = False
    res['response']['buttons'] = [
        {
            'title': 'Информация про субъект Российской Федерации',
            'hide': True
        },
        {
            'title': 'Информация про страны мира',
            'hide': True
        },
        {
            'title': 'Симптомы',
            'hide': True
        },
        {
            'title': 'Рекомендации',
            'hide': True
        },
        {
            'title': "Чем заняться в карантин?",
            'hide': True
        }
    ]


def infocounties(res, req):
    user_id = req['session']['user_id']
    cur = con.cursor()
    sp = cur.execute("""SELECT illpeople FROM world""").fetchall()
    if req['request']['nlu']['tokens'] in sp:
        result = cur.execute("""SELECT illpeople FROM world WHERE
            territory == {0}""".format(req['request']['nlu']['tokens'])).fetchone()
    else:
        result = 'Я не расслышала. Попробуйте еще раз.'
    res['response']['text'] = result
    res['response']['card']['type'] = 'BigImage'
    res['response']['card']['title'] = 'Заражение в мире'
    res['response']['card']['image_id'] = images['мир']
    sessionStorage[user_id]['information'] = False
    res['response']['buttons'] = [
        {
            'title': 'Информация про субъект Российской Федерации',
            'hide': True
        },
        {
            'title': 'Информация про страны мира',
            'hide': True
        },
        {
            'title': 'Симптомы',
            'hide': True
        },
        {
            'title': 'Рекомендации',
            'hide': True
        },
        {
            'title': "Чем заняться в карантин?",
            'hide': True
        }
    ]


def get_first_name(req):
    # перебираем сущности
    for entity in req['request']['nlu']['entities']:
        # находим сущность с типом 'YANDEX.FIO'
        if entity['type'] == 'YANDEX.FIO':
            # Если есть сущность с ключом 'first_name', то возвращаем её значение.
            # Во всех остальных случаях возвращаем None.
            return entity['value'].get('first_name', None)


if __name__ == '__main__':
    db_session.global_init("db/inform.sqlite")
    app.run()