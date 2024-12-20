class Pet:
    PET_TYPES =["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all =[]
    def __init__(self,name, pet_type,owner=None):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type. Must be one of {Pet.PET_TYPES}")
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of the Owner class")

        self.name = name
        self.pet_type =pet_type
        self.owner =owner
        Pet.all.append(self)
        

class Owner:
    def __init__(self,name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name

    def pets(self):
        
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        
        return sorted(self.pets(), key=lambda pet: pet.name)
