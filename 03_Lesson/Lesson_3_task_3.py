from Address import Address
from Mailing import Mailing

to_adress = Address(692330, "Арсеньев", "Ленинская", 40, 12)

from_adress = Address(564823, "Баку", "Октябрьская", 54, 96)

mailing = Mailing ("45213259", from_adress, to_adress, "450")


print(mailing)

