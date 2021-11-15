import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder, carrier

phoneNumber = phonenumbers.parse("+918095989419")
timeZone = timezone.time_zones_for_number(phoneNumber)
print(phoneNumber)
print(timeZone)


Carrier = carrier.name_for_number(phoneNumber, 'en')

# Getting region information
Region = geocoder.description_for_number(phoneNumber, 'en')
print(Carrier)
print(Region)
valid = phonenumbers.is_valid_number(phoneNumber)

# Checking possibility of a number
possible = phonenumbers.is_possible_number(phoneNumber)

# Printing the output
print(valid)
print(possible)
