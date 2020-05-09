from flask import Flask, request
import logging
import json
import sqlite3
from . import db_session
from __all_models.py import InfoRussia
from __all_models.py import InfoWorld
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)
logging.basicConfig(level=logging.INFO)
images = {
    'мир': "1030494/822b7834532e6e1bee43",
    'россия': "1030494/5fdd4125f486ed37ee53",
}
sessionStorage = {}



user = InfoRussia()
user.city = "Москва"
user.illpeople = 80115
session = db_session.create_session()
session.add(user)
user1 = InfoRussia()
user1.city = "Московская область"
user1.illpeople = 17432
session = db_session.create_session()
session.add(user1)
user2 = InfoRussia()
user2.city = "Санкт-Петербург"
user2.illpeople = 6190
session = db_session.create_session()
session.add(user2)
user3 = InfoRussia()
user3.city = "Нижегородская область"
user3.illpeople = 3610
session = db_session.create_session()
session.add(user3)
user4 = InfoRussia()
user4.city = "Республика Дагестан"
user4.illpeople = 2372
session = db_session.create_session()
session.add(user4)
user5 = InfoRussia()
user5.city = "Мурманская область"
user5.illpeople = 2272
session = db_session.create_session()
session.add(user5)
user6 = InfoRussia()
user6.city = "Краснодарский край"
user6.illpeople = 1633
session = db_session.create_session()
session.add(user6)
user7 = InfoRussia()
user7.city = "Тульская область"
user7.illpeople = 1530
session = db_session.create_session()
session.add(user7)
user8 = InfoRussia()
user8.city = "Ростовская область"
user8.illpeople = 1514
session = db_session.create_session()
session.add(user8)
user9 = InfoRussia()
user9.city = "Калужская область"
user9.illpeople = 1486
session = db_session.create_session()
session.add(user9)
user10 = InfoRussia()
user10.city = "Брянская область"
user10.illpeople = 1442
session = db_session.create_session()
session.add(user10)
user11 = InfoRussia()
user11.city = "Свердловская область"
user11.illpeople = 1429
session = db_session.create_session()
session.add(user11)
user12 = InfoRussia()
user12.city = "Республика Татарстан"
user12.illpeople = 1415
session = db_session.create_session()
session.add(user12)
user13 = InfoRussia()
user13.city = "Рязанская область"
user13.illpeople = 1396
session = db_session.create_session()
session.add(user13)
user14 = InfoRussia()
user14.city = "Республика Северная Осетия"
user14.illpeople = 1342
session = db_session.create_session()
session.add(user14)
user15 = InfoRussia()
user15.city = "Ленинградская область"
user15.illpeople = 1263
session = db_session.create_session()
session.add(user15)
user16 = InfoRussia()
user16.city = "Республика Башкортостан"
user16.illpeople = 1243
session = db_session.create_session()
session.add(user16)
user17 = InfoRussia()
user17.city = "Курская область"
user17.illpeople = 1197
session = db_session.create_session()
session.add(user17)
user18 = InfoRussia()
user18.city = "Владимирская область"
user18.illpeople = 1079
session = db_session.create_session()
session.add(user18)
user19 = InfoRussia()
user19.city = "Республика Ингушетия"
user19.illpeople = 1067
session = db_session.create_session()
session.add(user19)
user20 = InfoRussia()
user20.city = "Тамбовская область"
user20.illpeople = 1046
session = db_session.create_session()
session.add(user20)
user21 = InfoRussia()
user21.city = "Республика Мордовия"
user21.illpeople = 1018
session = db_session.create_session()
session.add(user21)
user22 = InfoRussia()
user22.city = "Ямало-Ненецкий автономный округ"
user22.illpeople = 1018
session = db_session.create_session()
session.add(user22)
user23 = InfoRussia()
user23.city = "Кабардино-Балкарская Республика"
user23.illpeople = 1008
session = db_session.create_session()
session.add(user23)
user24 = InfoRussia()
user24.city = "Республика Чувашия"
user24.illpeople = 950
session = db_session.create_session()
session.add(user24)
user25 = InfoRussia()
user25.city = "Ярославская область"
user25.illpeople = 935
session = db_session.create_session()
session.add(user25)
user26 = InfoRussia()
user26.city = "Красноярский край"
user26.illpeople = 933
session = db_session.create_session()
session.add(user26)
user27 = InfoRussia()
user27.city = "Ставропольский край"
user27.illpeople = 887
session = db_session.create_session()
session.add(user27)
user28 = InfoRussia()
user28.city = "Новосибирская область"
user28.illpeople = 876
session = db_session.create_session()
session.add(user28)
user29 = InfoRussia()
user29.city = "Саратовская область"
user29.illpeople = 876
session = db_session.create_session()
session.add(user29)
user30 = InfoRussia()
user30.city = "Орловская область"
user30.illpeople = 865
session = db_session.create_session()
session.add(user30)
user31 = InfoRussia()
user31.city = "Челябинская область"
user31.illpeople = 839
session = db_session.create_session()
session.add(user31)
user32 = InfoRussia()
user32.city = "Республика Марий Эл"
user32.illpeople = 814
session = db_session.create_session()
session.add(user32)
user33 = InfoRussia()
user33.city = "Оренбургская область"
user33.illpeople = 798
session = db_session.create_session()
session.add(user33)
user34 = InfoRussia()
user34.city = "Республика Коми"
user34.illpeople = 782
session = db_session.create_session()
session.add(user34)
user35 = InfoRussia()
user35.city = "Хабаровский край"
user35.illpeople = 781
session = db_session.create_session()
session.add(user35)
user36 = InfoRussia()
user36.city = "Тверская область"
user36.illpeople = 769
session = db_session.create_session()
session.add(user36)
user37 = InfoRussia()
user37.city = "Самарская область"
user37.illpeople = 413
session = db_session.create_session()
session.add(user37)
user = InfoRussia()
user.city = "Республика Марий Эл"
user.illpeople = 845
session = db_session.create_session()
session.add(user)
user1 = InfoRussia()
user1.city = "Волгоградская область"
user1.illpeople = 791
session = db_session.create_session()
session.add(user1)
user2 = InfoRussia()
user2.city = "Воронежская область"
user2.illpeople = 766
session = db_session.create_session()
session.add(user2)
user3 = InfoRussia()
user3.city = "Приморский край"
user3.illpeople = 763
session = db_session.create_session()
session.add(user3)
user4 = InfoRussia()
user4.city = "Липецкая область"
user4.illpeople = 752
session = db_session.create_session()
session.add(user4)
user5 = InfoRussia()
user5.city = "Пермский край"
user5.illpeople = 719
session = db_session.create_session()
session.add(user5)
user6 = InfoRussia()
user6.city = "Кировская область"
user6.illpeople = 718
session = db_session.create_session()
session.add(user6)
user7 = InfoRussia()
user7.city = "Тюменская область"
user7.illpeople = 707
session = db_session.create_session()
session.add(user7)
user8 = InfoRussia()
user8.city = "Чеченская Республика"
user8.illpeople = 705
session = db_session.create_session()
session.add(user8)
user9 = InfoRussia()
user9.city = "Ульяновская область"
user9.illpeople = 681
session = db_session.create_session()
session.add(user9)
user = InfoRussia()
user.city = "Пензенская область"
user.illpeople = 678
session = db_session.create_session()
session.add(user)
user1 = InfoRussia()
user1.city = "Ивановская область"
user1.illpeople = 653
session = db_session.create_session()
session.add(user1)
user2 = InfoRussia()
user2.city = "Смоленская область"
user2.illpeople = 646
session = db_session.create_session()
session.add(user2)
user3 = InfoRussia()
user3.city = "Калининградская область"
user3.illpeople = 637
session = db_session.create_session()
session.add(user3)
user4 = InfoRussia()
user4.city = "Астраханская область"
user4.illpeople = 629
session = db_session.create_session()
session.add(user4)
user5 = InfoRussia()
user5.city = "Алтайский край"
user5.illpeople = 621
session = db_session.create_session()
session.add(user5)
user6 = InfoRussia()
user6.city = "Белгородская область"
user6.illpeople = 613
session = db_session.create_session()
session.add(user6)
user7 = InfoRussia()
user7.city = "Ханты-Мансийский АО"
user7.illpeople = 583
session = db_session.create_session()
session.add(user7)
user8 = InfoRussia()
user8.city = "Республика Бурятия"
user8.illpeople = 518
session = db_session.create_session()
session.add(user8)
user9 = InfoRussia()
user9.city = "Карачаево-Черкесская Республика"
user9.illpeople = 478
session = db_session.create_session()
session.add(user9)
user20 = InfoRussia()
user20.city = "Новгородская область"
user20.illpeople = 457
session = db_session.create_session()
session.add(user20)
user21 = InfoRussia()
user21.city = "Республика Саха"
user21.illpeople = 537
session = db_session.create_session()
session.add(user21)
user22 = InfoRussia()
user22.city = "Республика Калмыкия"
user22.illpeople = 405
session = db_session.create_session()
session.add(user22)
user23 = InfoRussia()
user23.city = "Архангельская область"
user23.illpeople = 372
session = db_session.create_session()
session.add(user23)
user24 = InfoRussia()
user24.city = "Республика Хакасия"
user24.illpeople = 367
session = db_session.create_session()
session.add(user24)
user25 = InfoRussia()
user25.city = "Камчатский край"
user25.illpeople = 353
session = db_session.create_session()
session.add(user25)
user26 = InfoRussia()
user26.city = "Удмуртская Республика"
user26.illpeople = 345
session = db_session.create_session()
session.add(user26)
user27 = InfoRussia()
user27.city = "Костромская область"
user27.illpeople = 333
session = db_session.create_session()
session.add(user27)
user28 = InfoRussia()
user28.city = "Псковская область"
user28.illpeople = 270
session = db_session.create_session()
session.add(user28)
user29 = InfoRussia()
user29.city = "Забайкальский край"
user29.illpeople = 262
session = db_session.create_session()
session.add(user29)
user30 = InfoRussia()
user30.city = "Иркутская область"
user30.illpeople = 255
session = db_session.create_session()
session.add(user30)
user31 = InfoRussia()
user31.city = "Вологодская область"
user31.illpeople = 253
session = db_session.create_session()
session.add(user31)
user32 = InfoRussia()
user32.city = "Омская область"
user32.illpeople = 223
session = db_session.create_session()
session.add(user32)
user33 = InfoRussia()
user33.city = "Республика Адыгея"
user33.illpeople = 212
session = db_session.create_session()
session.add(user33)
user34 = InfoRussia()
user34.city = "Кемеровская область"
user34.illpeople = 204
session = db_session.create_session()
session.add(user34)
user35 = InfoRussia()
user35.city = "Томская область"
user35.illpeople = 176
session = db_session.create_session()
session.add(user35)
user36 = InfoRussia()
user36.city = "Еврейская автономная область"
user36.illpeople = 170
session = db_session.create_session()
session.add(user36)
user37 = InfoRussia()
user37.city = "Республика Крым"
user37.illpeople = 168
session = db_session.create_session()
session.add(user37)
user = InfoRussia()
user.city = "Магаданская область"
user.illpeople = 176
session = db_session.create_session()
session.add(user)
user1 = InfoRussia()
user1.city = "Республика Карелия"
user1.illpeople = 125
session = db_session.create_session()
session.add(user1)
user2 = InfoRussia()
user2.city = "Амурская область"
user2.illpeople = 123
session = db_session.create_session()
session.add(user2)
user3 = InfoRussia()
user3.city = "Севастополь"
user3.illpeople = 118
session = db_session.create_session()
session.add(user3)
user4 = InfoRussia()
user4.city = "Курганская область"
user4.illpeople = 65
session = db_session.create_session()
session.add(user4)
user5 = InfoRussia()
user5.city = "Республика Тыва"
user5.illpeople = 56
session = db_session.create_session()
session.add(user5)
user6 = InfoRussia()
user6.city = "Ненецкий автономный округ"
user6.illpeople = 49
session = db_session.create_session()
session.add(user6)
user7 = InfoRussia()
user7.city = "Республика Алтай"
user7.illpeople = 41
session = db_session.create_session()
session.add(user7)
user8 = InfoRussia()
user8.city = "Сахалинская область"
user8.illpeople = 31
session = db_session.create_session()
session.add(user8)
user9 = InfoRussia()
user9.city = "Чукотский автономный округ"
user9.illpeople = 27
session = db_session.create_session()
session.add(user9)

users = InfoWorld()
users.country = "США"
users.illpeople = 1256972
session = db_session.create_session()
session.add(users)
users1 = InfoWorld()
users1.country = "Испания"
users1.illpeople = 221447
session = db_session.create_session()
session.add(users1)
users2 = InfoWorld()
users2.country = "Италия"
users2.illpeople = 215858
session = db_session.create_session()
session.add(users2)
users3 = InfoWorld()
users3.country = "Великобритания"
users3.illpeople = 207977
session = db_session.create_session()
session.add(users3)
users4 = InfoWorld()
users4.country = "Россия"
users4.illpeople = 187859
session = db_session.create_session()
session.add(users4)
users5 = InfoWorld()
users5.country = "Франция"
users5.illpeople = 174918
session = db_session.create_session()
session.add(users5)
users6 = InfoWorld()
users6.country = "Германия"
users6.illpeople = 169430
session = db_session.create_session()
session.add(users6)
users6 = InfoWorld()
users6.country = "Бразилия"
users6.illpeople = 135773
session = db_session.create_session()
session.add(users6)
users7 = InfoWorld()
users7.country = "Турция"
users7.illpeople = 133721
session = db_session.create_session()
session.add(users7)
users8 = InfoWorld()
users8.country = "Иран"
users8.illpeople = 103135
session = db_session.create_session()
session.add(users8)
users9 = InfoWorld()
users9.country = "Китай"
users9.illpeople = 83976
session = db_session.create_session()
session.add(users9)
users  = InfoWorld()
users.country = "Канада"
users.illpeople = 66201
session = db_session.create_session()
session.add(users)
users1 = InfoWorld()
users1.country = "Перу"
users1.illpeople = 58526
session = db_session.create_session()
session.add(users1)
users2 = InfoWorld()
users2.country = "Индия"
users2.illpeople = 56516
session = db_session.create_session()
session.add(users2)
users3 = InfoWorld()
users3.country = "Бельгия"
users3.illpeople = 52011
session = db_session.create_session()
session.add(users3)
users4 = InfoWorld()
users4.country = "Нидерланды"
users4.illpeople = 41973
session = db_session.create_session()
session.add(users4)
users5 = InfoWorld()
users5.country = "Саудовская Аравия"
users5.illpeople = 33721
session = db_session.create_session()
session.add(users5)
users6 = InfoWorld()
users6.country = "Эквадор"
users6.illpeople = 30298
session = db_session.create_session()
session.add(users6)
users7 = InfoWorld()
users7.country = "Швейцария"
users7.illpeople = 30126
session = db_session.create_session()
session.add(users7)
users8 = InfoWorld()
users8.country = "Мексика"
users8.illpeople = 29616
session = db_session.create_session()
session.add(users8)
users9 = InfoWorld()
users9.country = "Португалия"
users9.illpeople = 26715
session = db_session.create_session()
session.add(users9)
users  = InfoWorld()
users.country = "Пакистан"
users.illpeople = 25837
session = db_session.create_session()
session.add(users)
users1 = InfoWorld()
users1.country = "Швеция"
users1.illpeople = 24623
session = db_session.create_session()
session.add(users1)
users2 = InfoWorld()
users2.country = "Чили"
users2.illpeople = 24581
session = db_session.create_session()
session.add(users2)
users3 = InfoWorld()
users3.country = "Ирландия"
users3.illpeople = 22385
session = db_session.create_session()
session.add(users3)
users4 = InfoWorld()
users4.country = "Сингапур"
users4.illpeople = 21707
session = db_session.create_session()
session.add(users4)
users5 = InfoWorld()
users5.country = "Беларусь"
users5.illpeople = 20168
session = db_session.create_session()
session.add(users5)
users6 = InfoWorld()
users6.country = "Катар"
users6.illpeople = 18890
session = db_session.create_session()
session.add(users6)
users7 = InfoWorld()
users7.country = "Израиль"
users7.illpeople = 16409
session = db_session.create_session()
session.add(users7)
users8 = InfoWorld()
users8.country = "Объединённые Арабские Эмираты"
users8.illpeople = 16240
session = db_session.create_session()
session.add(users8)
users9 = InfoWorld()
users9.country = "Австрия"
users9.illpeople = 15752
session = db_session.create_session()
session.add(users9)
users  = InfoWorld()
users.country = "Япония"
users.illpeople = 15477
session = db_session.create_session()
session.add(users)
users1 = InfoWorld()
users1.country = "Польша"
users1.illpeople = 15200
session = db_session.create_session()
session.add(users1)
users2 = InfoWorld()
users2.country = "Румыния"
users2.illpeople = 14499
session = db_session.create_session()
session.add(users2)
users3 = InfoWorld()
users3.country = "Украина"
users3.illpeople = 14195
session = db_session.create_session()
session.add(users3)
users4 = InfoWorld()
users4.country = "Бангладеш"
users4.illpeople = 13134
session = db_session.create_session()
session.add(users4)
users5 = InfoWorld()
users5.country = "Индонезия"
users5.illpeople = 13112
session = db_session.create_session()
session.add(users5)
users6 = InfoWorld()
users6.country = "Южная Корея"
users6.illpeople = 10822
session = db_session.create_session()
session.add(users6)
users7 = InfoWorld()
users7.country = "Филиппины"
users7.illpeople = 10463
session = db_session.create_session()
session.add(users7)
users8 = InfoWorld()
users8.country = "Дания"
users8.illpeople = 10281
session = db_session.create_session()
session.add(users8)
users9 = InfoWorld()
users9.country = "Сербия"
users9.illpeople = 9848
session = db_session.create_session()
session.add(users9)
users  = InfoWorld()
users.country = "Колумбия"
users.illpeople = 9456
session = db_session.create_session()
session.add(users)
users1 = InfoWorld()
users1.country = "Доминиканская Республика"
users1.illpeople = 9095
session = db_session.create_session()
session.add(users1)
users2 = InfoWorld()
users2.country = "ЮАР"
users2.illpeople = 8232
session = db_session.create_session()
session.add(users2)
users3 = InfoWorld()
users3.country = "Норвегия"
users3.illpeople = 8034
session = db_session.create_session()
session.add(users3)
users4 = InfoWorld()
users4.country = "Чехия"
users4.illpeople = 8031
session = db_session.create_session()
session.add(users4)
users5 = InfoWorld()
users5.country = "Египет"
users5.illpeople = 7981
session = db_session.create_session()
session.add(users5)
users6 = InfoWorld()
users6.country = "Панама"
users6.illpeople = 7868
session = db_session.create_session()
session.add(users6)
users7 = InfoWorld()
users7.country = "Австралия"
users7.illpeople = 6914
session = db_session.create_session()
session.add(users7)
users8 = InfoWorld()
users8.country = "Кувейт"
users8.illpeople = 6567
session = db_session.create_session()
session.add(users8)
users9 = InfoWorld()
users9.country = "Малайзия"
users9.illpeople = 6535
session = db_session.create_session()
session.add(users9)
users  = InfoWorld()
users.country = "Финляндия"
users.illpeople = 5673
session = db_session.create_session()
session.add(users)
users1 = InfoWorld()
users1.country = "Марокко"
users1.illpeople = 5548
session = db_session.create_session()
session.add(users1)
users2 = InfoWorld()
users2.country = "Аргентина"
users2.illpeople = 5371
session = db_session.create_session()
session.add(users2)
users3 = InfoWorld()
users3.country = "Алжир"
users3.illpeople = 5182
session = db_session.create_session()
session.add(users3)
users4 = InfoWorld()
users4.country = "Казахстан"
users4.illpeople = 4753
session = db_session.create_session()
session.add(users4)
users5 = InfoWorld()
users5.country = "Молдова"
users5.illpeople = 4605
session = db_session.create_session()
session.add(users5)
users6 = InfoWorld()
users6.country = "Бахрейн"
users6.illpeople = 4199
session = db_session.create_session()
session.add(users6)
users7 = InfoWorld()
users7.country = "Люксембург"
users7.illpeople = 3859
session = db_session.create_session()
session.add(users7)
users8 = InfoWorld()
users8.country = "Афганистан"
users8.illpeople = 3563
session = db_session.create_session()
session.add(users8)
users9 = InfoWorld()
users9.country = "Нигерия"
users9.illpeople = 3526
session = db_session.create_session()
session.add(users9)
users  = InfoWorld()
users.country = "Венгрия"
users.illpeople = 3178
session = db_session.create_session()
session.add(users)
users1 = InfoWorld()
users1.country = "Оман"
users1.illpeople = 3112
session = db_session.create_session()
session.add(users1)
users2 = InfoWorld()
users2.country = "Гана"
users2.illpeople = 3091
session = db_session.create_session()
session.add(users2)
users3 = InfoWorld()
users3.country = "Армения"
users3.illpeople = 3029
session = db_session.create_session()
session.add(users3)
users4 = InfoWorld()
users4.country = "Таиланд"
users4.illpeople = 3000
session = db_session.create_session()
session.add(users4)
users5 = InfoWorld()
users5.country = "Греция"
users5.illpeople = 2678
session = db_session.create_session()
session.add(users5)
users6 = InfoWorld()
users6.country = "Ирак"
users6.illpeople = 2543
session = db_session.create_session()
session.add(users6)
users7 = InfoWorld()
users7.country = "Узбекистан"
users7.illpeople = 2298
session = db_session.create_session()
session.add(users7)
users8 = InfoWorld()
users8.country = "Камерун"
users8.illpeople = 2267
session = db_session.create_session()
session.add(users8)
users9 = InfoWorld()
users9.country = "Азербайджан"
users9.illpeople = 2204
session = db_session.create_session()
session.add(users9)
users  = InfoWorld()
users.country = "Хорватия"
users.illpeople = 2125
session = db_session.create_session()
session.add(users)
users1 = InfoWorld()
users1.country = "Боливия"
users1.illpeople = 2081
session = db_session.create_session()
session.add(users1)
users2 = InfoWorld()
users2.country = "Босния и Герцеговина"
users2.illpeople = 2027
session = db_session.create_session()
session.add(users2)
users3 = InfoWorld()
users3.country = "Гвинея"
users3.illpeople = 1927
session = db_session.create_session()
session.add(users3)
users4 = InfoWorld()
users4.country = "Болгария"
users4.illpeople = 1865
session = db_session.create_session()
session.add(users4)
users5 = InfoWorld()
users5.country = "Исландия"
users5.illpeople = 1801
session = db_session.create_session()
session.add(users5)
users6 = InfoWorld()
users6.country = "Куба"
users6.illpeople = 1729
session = db_session.create_session()
session.add(users6)
users7 = InfoWorld()
users7.country = "Эстония"
users7.illpeople = 1725
session = db_session.create_session()
session.add(users7)
users8 = InfoWorld()
users8.country = "Гондурас"
users8.illpeople = 1685
session = db_session.create_session()
session.add(users8)
users9 = InfoWorld()
users9.country = "Северная Македония"
users9.illpeople = 1572
session = db_session.create_session()
session.add(users9)
users  = InfoWorld()
users.country = "Кот-д’Ивуар"
users.illpeople = 1571
session = db_session.create_session()
session.add(users)
users1 = InfoWorld()
users1.country = "Сенегал"
users1.illpeople = 1492
session = db_session.create_session()
session.add(users1)
users2 = InfoWorld()
users2.country = "Новая Зеландия"
users2.illpeople = 1490
session = db_session.create_session()
session.add(users2)
users3 = InfoWorld()
users3.country = "Словакия"
users3.illpeople = 1455
session = db_session.create_session()
session.add(users3)
users4 = InfoWorld()
users4.country = "Словения"
users4.illpeople = 1449
session = db_session.create_session()
session.add(users4)
users5 = InfoWorld()
users5.country = "Литва"
users5.illpeople = 1436
session = db_session.create_session()
session.add(users5)
users6 = InfoWorld()
users6.country = "Джибути"
users6.illpeople = 1133
session = db_session.create_session()
session.add(users6)
users7 = InfoWorld()
users7.country = "Тунис"
users7.illpeople = 1026
session = db_session.create_session()
session.add(users7)
users8 = InfoWorld()
users8.country = "Судан"
users8.illpeople = 930
session = db_session.create_session()
session.add(users8)
users9 = InfoWorld()
users9.country = "Латвия"
users9.illpeople = 928
session = db_session.create_session()
session.add(users9)
users  = InfoWorld()
users.country = "Сомали"
users.illpeople = 928
session = db_session.create_session()
session.add(users)
users1 = InfoWorld()
users1.country = "Киргизия"
users1.illpeople = 906
session = db_session.create_session()
session.add(users1)
users2 = InfoWorld()
users2.country = "Демократическая Республика Конго"
users2.illpeople = 897
session = db_session.create_session()
session.add(users2)
users3 = InfoWorld()
users3.country = "Кипр"
users3.illpeople = 889
session = db_session.create_session()
session.add(users3)
users4 = InfoWorld()
users4.country = "Албания"
users4.illpeople = 842
session = db_session.create_session()
session.add(users4)
users5 = InfoWorld()
users5.country = "Гватемала"
users5.illpeople = 832
session = db_session.create_session()
session.add(users5)
users6 = InfoWorld()
users6.country = "Шри-Ланка"
users6.illpeople = 824
session = db_session.create_session()
session.add(users6)
users7 = InfoWorld()
users7.country = "Ливан"
users7.illpeople = 784
session = db_session.create_session()
session.add(users7)
users8 = InfoWorld()
users8.country = "Нигер"
users8.illpeople = 781
session = db_session.create_session()
session.add(users8)
users9 = InfoWorld()
users9.country = "Коста-Рика"
users9.illpeople = 765
session = db_session.create_session()
session.add(users9)
users  = InfoWorld()
users.country = "Андорра"
users.illpeople = 752
session = db_session.create_session()
session.add(users)
users1 = InfoWorld()
users1.country = "Сальвадор"
users1.illpeople = 742
session = db_session.create_session()
session.add(users1)
users2 = InfoWorld()
users2.country = "Буркина-Фасо"
users2.illpeople = 736
session = db_session.create_session()
session.add(users2)
users3 = InfoWorld()
users3.country = "Уругвай"
users3.illpeople = 684
session = db_session.create_session()
session.add(users3)
users4 = InfoWorld()
users4.country = "Мали"
users4.illpeople = 650
session = db_session.create_session()
session.add(users4)
users5 = InfoWorld()
users5.country = "Мальдивы"
users5.illpeople = 648
session = db_session.create_session()
session.add(users5)
users6 = InfoWorld()
users6.country = "Грузия"
users6.illpeople = 623
session = db_session.create_session()
session.add(users6)
users7 = InfoWorld()
users7.country = "Сан-Марино"
users7.illpeople = 622
session = db_session.create_session()
session.add(users7)
users8 = InfoWorld()
users8.country = "Кения"
users8.illpeople = 607
session = db_session.create_session()
session.add(users8)
users9 = InfoWorld()
users9.country = "Гвинея-Бисау"
users9.illpeople = 564
session = db_session.create_session()
session.add(users9)
users  = InfoWorld()
users.country = "Габон"
users.illpeople = 504
session = db_session.create_session()
session.add(users)
users1 = InfoWorld()
users1.country = "Иордания"
users1.illpeople = 494
session = db_session.create_session()
session.add(users1)
users2 = InfoWorld()
users2.country = "Ямайка"
users2.illpeople = 488
session = db_session.create_session()
session.add(users2)
users3 = InfoWorld()
users3.country = "Мальта"
users3.illpeople = 486
session = db_session.create_session()
session.add(users3)
users4 = InfoWorld()
users4.country = "Танзания"
users4.illpeople = 480
session = db_session.create_session()
session.add(users4)
users5 = InfoWorld()
users5.country = "Парагвай"
users5.illpeople = 462
session = db_session.create_session()
session.add(users5)
users6 = InfoWorld()
users6.country = "Таджикистан"
users6.illpeople = 461
session = db_session.create_session()
session.add(users6)
users7 = InfoWorld()
users7.country = "Экваториальная Гвинея"
users7.illpeople = 439
session = db_session.create_session()
session.add(users7)
users8 = InfoWorld()
users8.country = "Венесуэла"
users8.illpeople = 381
session = db_session.create_session()
session.add(users8)
users9 = InfoWorld()
users9.country = "Маврикий"
users9.illpeople = 332
session = db_session.create_session()
session.add(users9)
users  = InfoWorld()
users.country = "Черногория"
users.illpeople = 324
session = db_session.create_session()
session.add(users)
users1 = InfoWorld()
users1.country = "Вьетнам"
users1.illpeople = 288
session = db_session.create_session()
session.add(users1)
users2 = InfoWorld()
users2.country = "Республика Конго"
users2.illpeople = 274
session = db_session.create_session()
session.add(users2)
users3 = InfoWorld()
users3.country = "Руанда"
users3.illpeople = 271
session = db_session.create_session()
session.add(users3)
users4 = InfoWorld()
users4.country = "Чад"
users4.illpeople = 253
session = db_session.create_session()
session.add(users4)
users5 = InfoWorld()
users5.country = "Сьерра-Леоне"
users5.illpeople = 231
session = db_session.create_session()
session.add(users5)
users6 = InfoWorld()
users6.country = "Кабо-Верде"
users6.illpeople = 218
session = db_session.create_session()
session.add(users6)
users7 = InfoWorld()
users7.country = "Мадагаскар"
users7.illpeople = 193
session = db_session.create_session()
session.add(users7)
users8 = InfoWorld()
users8.country = "Эфиопия"
users8.illpeople = 191
session = db_session.create_session()
session.add(users8)
users9 = InfoWorld()
users9.country = "Либерия"
users9.illpeople = 189
session = db_session.create_session()
session.add(users9)
users  = InfoWorld()
users.country = "Сан-Томе и Принсипи"
users.illpeople = 187
session = db_session.create_session()
session.add(users)
users1 = InfoWorld()
users1.country = "Мьянма"
users1.illpeople = 176
session = db_session.create_session()
session.add(users1)
users2 = InfoWorld()
users2.country = "Замбия"
users2.illpeople = 153
session = db_session.create_session()
session.add(users2)
users3 = InfoWorld()
users3.country = "Эсватини"
users3.illpeople = 153
session = db_session.create_session()
session.add(users3)
users4 = InfoWorld()
users4.country = "Бруней"
users4.illpeople = 141
session = db_session.create_session()
session.add(users4)
users5 = InfoWorld()
users5.country = "Бенин"
users5.illpeople = 140
session = db_session.create_session()
session.add(users5)
users6 = InfoWorld()
users6.country = "Того"
users6.illpeople = 135
session = db_session.create_session()
session.add(users6)
users7 = InfoWorld()
users7.country = "Гаити"
users7.illpeople = 129
session = db_session.create_session()
session.add(users7)
users8 = InfoWorld()
users8.country = "Камбоджа"
users8.illpeople = 122
session = db_session.create_session()
session.add(users8)
users9 = InfoWorld()
users9.country = "Тринидад и Тобаго"
users9.illpeople = 116
session = db_session.create_session()
session.add(users9)
users  = InfoWorld()
users.country = "Непал"
users.illpeople = 101
session = db_session.create_session()
session.add(users)
users1 = InfoWorld()
users1.country = "Уганда"
users1.illpeople = 101
session = db_session.create_session()
session.add(users1)
users2 = InfoWorld()
users2.country = "Монако"
users2.illpeople = 95
session = db_session.create_session()
session.add(users2)
users3 = InfoWorld()
users3.country = "Центральноафриканская республика"
users3.illpeople = 94
session = db_session.create_session()
session.add(users3)
users4 = InfoWorld()
users4.country = "Гайана"
users4.illpeople = 93
session = db_session.create_session()
session.add(users4)
users5 = InfoWorld()
users5.country = "Багамские острова"
users5.illpeople = 92
session = db_session.create_session()
session.add(users5)
users6 = InfoWorld()
users6.country = "Барбадос"
users6.illpeople = 82
session = db_session.create_session()
session.add(users6)
users7 = InfoWorld()
users7.country = "Лихтенштейн"
users7.illpeople = 82
session = db_session.create_session()
session.add(users7)
users8 = InfoWorld()
users8.country = "Мозамбик"
users8.illpeople = 81
session = db_session.create_session()
session.add(users8)
users9 = InfoWorld()
users9.country = "Южный Судан"
users9.illpeople = 74
session = db_session.create_session()
session.add(users9)
users  = InfoWorld()
users.country = "Ливия"
users.illpeople = 64
session = db_session.create_session()
session.add(users)
users1 = InfoWorld()
users1.country = "Сирия"
users1.illpeople = 45
session = db_session.create_session()
session.add(users1)
users2 = InfoWorld()
users2.country = "Малави"
users2.illpeople = 43
session = db_session.create_session()
session.add(users2)
users3 = InfoWorld()
users3.country = "Монголия"
users3.illpeople = 42
session = db_session.create_session()
session.add(users3)
users4 = InfoWorld()
users4.country = "Эритрея"
users4.illpeople = 39
session = db_session.create_session()
session.add(users4)
users5 = InfoWorld()
users5.country = "Ангола"
users5.illpeople = 36
session = db_session.create_session()
session.add(users5)
users6 = InfoWorld()
users6.country = "Зимбабве"
users6.illpeople = 34
session = db_session.create_session()
session.add(users6)
users7 = InfoWorld()
users7.country = "Антигуа и Барбуда"
users7.illpeople = 25
session = db_session.create_session()
session.add(users7)
users8 = InfoWorld()
users8.country = "Йемен"
users8.illpeople = 25
session = db_session.create_session()
session.add(users8)
users9 = InfoWorld()
users9.country = "Восточный Тимор"
users9.illpeople = 24
session = db_session.create_session()
session.add(users9)
users  = InfoWorld()
users.country = "Ботсвана"
users.illpeople = 23
session = db_session.create_session()
session.add(users)
users1 = InfoWorld()
users1.country = "Гренада"
users1.illpeople = 21
session = db_session.create_session()
session.add(users1)
users2 = InfoWorld()
users2.country = "Лаос"
users2.illpeople = 19
session = db_session.create_session()
session.add(users2)
users3 = InfoWorld()
users3.country = "Белиз"
users3.illpeople = 18
session = db_session.create_session()
session.add(users3)
users4 = InfoWorld()
users4.country = "Гамбия"
users4.illpeople = 19
session = db_session.create_session()
session.add(users4)
users5 = InfoWorld()
users5.country = "Сент-Люсия"
users5.illpeople = 18
session = db_session.create_session()
session.add(users5)
users6 = InfoWorld()
users6.country = "Фиджи"
users6.illpeople = 18
session = db_session.create_session()
session.add(users6)
users7 = InfoWorld()
users7.country = "Сент-Винсент и Гренадины"
users7.illpeople = 17
session = db_session.create_session()
session.add(users7)
users8 = InfoWorld()
users8.country = "Доминика"
users8.illpeople = 16
session = db_session.create_session()
session.add(users8)
users9 = InfoWorld()
users9.country = "Намибия"
users9.illpeople = 16
session = db_session.create_session()
session.add(users9)
users  = InfoWorld()
users.country = "Никарагуа"
users.illpeople = 16
session = db_session.create_session()
session.add(users)
users1 = InfoWorld()
users1.country = "Бурунди"
users1.illpeople = 15
session = db_session.create_session()
session.add(users1)
users2 = InfoWorld()
users2.country = "Сент-Китс и Невис"
users2.illpeople = 15
session = db_session.create_session()
session.add(users2)
users3 = InfoWorld()
users3.country = "Ватикан"
users3.illpeople = 12
session = db_session.create_session()
session.add(users3)
users4 = InfoWorld()
users4.country = "Сейшельские острова"
users4.illpeople = 11
session = db_session.create_session()
session.add(users4)
users5 = InfoWorld()
users5.country = "Суринам"
users5.illpeople = 10
session = db_session.create_session()
session.add(users5)
users6 = InfoWorld()
users6.country = "Коморские острова"
users6.illpeople = 8
session = db_session.create_session()
session.add(users6)
users7 = InfoWorld()
users7.country = "Мавритания"
users7.illpeople = 8
session = db_session.create_session()
session.add(users7)
users8 = InfoWorld()
users8.country = "Папуа-Новая Гвинея"
users8.illpeople = 8
session = db_session.create_session()
session.add(users8)
users9 = InfoWorld()
users9.country = "Бутан"
users9.illpeople = 7
session = db_session.create_session()
session.add(users9)
users  = InfoWorld()
users.country = "Сахарская Арабская Демократическая Республика"
users.illpeople = 6
session = db_session.create_session()
session.add(users)


@app.route('/post', methods=['POST'])
def main():
    db_session.global_init("db/information.sqlite")
    global con
    # con = sqlite3.connect("infor.db")
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
            if ('Информация про субъект Российской Федерации'  in req['request']['nlu']['tokens'] or
                'информация про субъект Российской Федерации' in req['request']['nlu']['tokens'] or
                "информация про город" in req['request']['nlu']['tokens'] or "Информация про город" in
                req['request']['nlu']['tokens']):
                sessionStorage[user_id]['information'] = True
                # вызываем необходимую функцию

            elif 'Информация про страну' in req['request']['nlu']['tokens'] or\
                    'информация про страну' in req['request']['nlu']['tokens']:
                sessionStorage[user_id]['information'] = True
                # вызываем необходимую функцию

            elif 'Симптомы' in req['request']['nlu']['tokens'] or 'симптомы' in req['request']['nlu']['tokens']:
                sessionStorage[user_id]['information'] = True
                symptomes(res, req)

            elif 'Рекомендации' in req['request']['nlu']['tokens'] or 'рекомендации' in req['request']['nlu']['tokens']:
                sessionStorage[user_id]['information'] = True
                recomendation(res, req)

            elif 'Чем заняться в карантин?' in req['request']['nlu']['tokens'] or\
                    'чем заняться в карантин?' in req['request']['nlu']['tokens'] or\
                    "чем заняться на самоизоляции?" in req['request']['nlu']['tokens'] or\
                    "Чем заняться на самоизоляции?" in req['request']['nlu']['tokens'] or\
                    "чем заняться во время самоизоляции?" in req['request']['nlu']['tokens'] or\
                    "Чем заняться во время самоизоляции?" in req['request']['nlu']['tokens'] or\
                    "Чем заняться?" in req['request']['nlu']['tokens'] or\
                    "Что делать?" in req['request']['nlu']['tokens'] or\
                    "что делать?" in req['request']['nlu']['tokens'] or\
                    'Что делать? в карантин?' in req['request']['nlu']['tokens'] or\
                    'что делать? в карантин?' in req['request']['nlu']['tokens'] or\
                    "чем заняться?" in req['request']['nlu']['tokens'] or\
                    "что делать? на самоизоляции?" in req['request']['nlu']['tokens'] or\
                    "Что делать? на самоизоляции?" in req['request']['nlu']['tokens'] or\
                    "что делать? во время самоизоляции?" in req['request']['nlu']['tokens'] or\
                    "Что делать? во время самоизоляции?" in req['request']['nlu']['tokens']:
                sessionStorage[user_id]['information'] = True
                # вызываем необходимую функцию


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
            elif 'Информация про страну' in req['request']['nlu']['tokens'] or\
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
            elif 'Чем заняться в карантин?' in req['request']['nlu']['tokens'] or\
                    'чем заняться в карантин?' in req['request']['nlu']['tokens'] or\
                    "чем заняться на самоизоляции?" in req['request']['nlu']['tokens'] or\
                    "Чем заняться на самоизоляции?" in req['request']['nlu']['tokens'] or\
                    "чем заняться во время самоизоляции?" in req['request']['nlu']['tokens'] or\
                    "Чем заняться во время самоизоляции?" in req['request']['nlu']['tokens'] or\
                    "Чем заняться?" in req['request']['nlu']['tokens'] or\
                    "Что делать?" in req['request']['nlu']['tokens'] or\
                    "что делать?" in req['request']['nlu']['tokens'] or\
                    'Что делать? в карантин?' in req['request']['nlu']['tokens'] or\
                    'что делать? в карантин?' in req['request']['nlu']['tokens'] or\
                    "чем заняться?" in req['request']['nlu']['tokens'] or\
                    "что делать? на самоизоляции?" in req['request']['nlu']['tokens'] or\
                    "Что делать? на самоизоляции?" in req['request']['nlu']['tokens'] or\
                    "что делать? во время самоизоляции?" in req['request']['nlu']['tokens'] or\
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


def get_first_name(req):
    # перебираем сущности
    for entity in req['request']['nlu']['entities']:
        # находим сущность с типом 'YANDEX.FIO'
        if entity['type'] == 'YANDEX.FIO':
            # Если есть сущность с ключом 'first_name', то возвращаем её значение.
            # Во всех остальных случаях возвращаем None.
            return entity['value'].get('first_name', None)


if __name__ == '__main__':
    app.run()