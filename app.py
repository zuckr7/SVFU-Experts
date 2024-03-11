class TheTrainingProgram:
    def __init__(self, name, duration, instructor, materials):
        self.name = name  # Название программы обучения
        self.duration = duration  # Продолжительность программы
        self.instructor = instructor  # Преподаватель
        self.materials = materials  # Материалы для обучения

    def start_program(self):
        # Метод для начала программы обучения
        print(f"Программа обучения '{self.name}' началась.")
        print(f"Продолжительность: {self.duration}.")
        print(f"Инструктор: {self.instructor}.")
        print("Давайте начнем учиться!")

    def complete_program(self):
        # Метод для завершения программы обучения
        print(f"Программа обучения '{self.name}' завершена. Поздравляем!")

    def get_materials(self):
        # Метод для получения материалов программы обучения
        print(f"Материалы для программы обучения '{self.name}':")
        for material in self.materials:
            print(material)
