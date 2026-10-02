class User:
    def __init__(self, last_name, first_name, surname, phone, street_address, house, building, apartment):
        self.last_name = last_name
        self.first_name = first_name
        self.surname = surname
        self.phone = phone
        self.street_address = street_address
        self.house = house
        self.building = building
        self.apartment = apartment

    def __str__(self):
        return f"{self.first_name} {self.surname} {self.last_name} - tel: {self.phone}"

    def __repr__(self):
        return self.__str__()