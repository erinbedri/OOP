class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, id):
        result = ""

        subscription = self.__get_obj_by_id(self.subscriptions, id)
        customer = self.__get_obj_by_id(self.customers, id)
        trainer = self.__get_obj_by_id(self.trainers, id)
        plan = self.__get_obj_by_id(self.plans, id)
        equipment = self.__get_obj_by_id(self.equipment, id)

        result += str(subscription) + "\n"
        result += str(customer) + "\n"
        result += str(trainer) + "\n"

        result += str(equipment) + "\n"
        result += str(plan) + "\n"

        return result

    @staticmethod
    def __get_obj_by_id(objects, searched_id):
        for obj in objects:
            if obj.id == searched_id:
                return obj

