
from address import Address
from mailing import Mailing

from_address = Address(
    "101000", "Репово", "Тучная", "1", "10"
)

to_address = Address(
    "190000", "Луково", "Облачная", "100", "25"
)

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=350,
    track="RA123456789RU"
)

print(
    f"Отправление {mailing.track} из "
    f"{mailing.from_address.index}, "
    f"{mailing.from_address.city}, "
    f"{mailing.from_address.street}, "
    f"{mailing.from_address.house} - "
    f"{mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, "
    f"{mailing.to_address.city}, "
    f"{mailing.to_address.street}, "
    f"{mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)
