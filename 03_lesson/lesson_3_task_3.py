from address import Address
from mailing import Mailing

to_address = Address(index=650002, gorod="Кемерово",
                     ulica="Институтская", dom=1, kvartira=331)
from_address = Address(index=100030, gorod="Томск",
                       ulica="Советская", dom=23, kvartira=17)
mail = Mailing(to_address, from_address, track="EFGY215", cost=200)

print(f' Отправление {mail.track} из {mail.from_address.index},'
      f' {mail.from_address.gorod}, {mail.from_address.ulica}, '
      f' {mail.from_address.dom}, {mail.from_address.kvartira},'
      f' в {mail.to_address.index}, {mail.to_address.gorod},'
      f' {mail.to_address.ulica}, {mail.to_address.dom},'
      f' {mail.to_address.kvartira}. Стоимость {mail.cost} рублей.')
