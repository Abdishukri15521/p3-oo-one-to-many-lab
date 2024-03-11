class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all_pets = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        if owner:
            owner.add_pet(self)  # If owner is provided, add pet to owner's list
        Pet.all_pets.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self.pet_list = []

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type")
        self.pet_list.append(pet)
        pet.owner = self

    def remove_pet(self, pet):
        self.pet_list.remove(pet)
        pet.owner = None

    def pets(self):
        return self.pet_list

    def get_sorted_pets(self):
        return sorted(self.pet_list, key=lambda pet: pet.name)
