from faker import Faker

fake = Faker()
add = fake.address()
fake.name()

print(fake.name())
print(add)
