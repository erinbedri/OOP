class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget < price and self.__animal_capacity > len(self.animals):
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum([worker.salary for worker in self.workers])
        # total_salaries = sum(map(lambda worker: worker.salary, self.workers))
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_care_amount = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= total_care_amount:
            self.__budget -= total_care_amount
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        zoo_dict = {"Lion": [],
                    "Tiger": [],
                    "Cheetah": []}
        text_to_return = ""
        for animal in self.animals:
            zoo_dict[animal.__class__.__name__].append(animal)
        text_to_return += f"You have {len(self.animals)} animals"
        text_to_return += "\n"
        for type_of_animal, animals in zoo_dict.items():
            text_to_return += f"----- {len(animals)} {type_of_animal}s:"
            text_to_return += "\n"
            for animal in animals:
                text_to_return += f"{animal.__repr__()}"
                text_to_return += "\n"
        return text_to_return.strip()

    def workers_status(self):
        workers_dict = {"Keeper": [],
                        "Caretaker": [],
                        "Vet": []}
        text_to_return = ""
        for worker in self.workers:
            workers_dict[worker.__class__.__name__].append(worker)
        text_to_return += f"You have {len(self.workers)} workers"
        text_to_return += "\n"
        for type_of_worker, workers in workers_dict.items():
            text_to_return += f"----- {len(workers)} {type_of_worker}s:"
            text_to_return += "\n"
            for worker in workers:
                text_to_return += f"{worker.__repr__()}"
                text_to_return += "\n"
        return text_to_return.strip()