class calculate_needing:
    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight
        self.calorie=0
        self.water=0
        self.protein=0
        self.BMI=0
        self.carbohydrates=0
        self.cholesterol=0
        self.fibroid=0

    def calculate_calorie(self):
        self.calorie = 10*self.weight + 6.25*self.height - 5*self.age + 5
        return self.calorie

    def calculate_water(self):
        self.water = 30*self.weight
        return self.water

    def calculate_protein(self):
        self.protein = 0.8*self.weight
        return self.protein

    def calculate_BMI(self):
        self.BMI = self.weight/(self.height*self.height)
        return self.BMI

    def calculate_carbohydrates(self):
        self.carbohydrates = 0.5*self.weight
        return self.carbohydrates

    def calculate_cholesterol(self):
        self.cholesterol = 300
        return self.cholesterol
