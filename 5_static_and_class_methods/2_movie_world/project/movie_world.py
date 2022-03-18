class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if self.customer_capacity() > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if self.dvd_capacity() > len(self.dvds):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.__get_obj_by_id(self.customers, customer_id)
        dvd = self.__get_obj_by_id(self.dvds, dvd_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        if dvd.is_rented and dvd not in customer.rented_dvds:
            return "DVD is already rented"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.__get_obj_by_id(self.customers, customer_id)
        dvd = self.__get_obj_by_id(self.dvds, dvd_id)

        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"

        return f"{customer.name} does not have that DVD"

    def __get_obj_by_id(self, objects, searched_id):
        for obj in objects:
            if obj.id == searched_id:
                return obj

    def __repr__(self):
        result = ""
        customers = "\n".join([str(customer) for customer in self.customers])
        result += customers + "\n"
        dvds = "\n".join([str(dvd) for dvd in self.dvds])
        result += dvds + "\n"
        return result
