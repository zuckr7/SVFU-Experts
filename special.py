class Speciality:
    def __init__(self,CodePS,FullCode,Name,RegNumber,Description,OccupationGroup,EconomicActivity):
        self.CodePS=CodePS
        self.FullCode=FullCode
        self.Name=Name
        self.RegNumber=RegNumber
        self.Description=Description
        self.OccupationGroup=OccupationGroup
        self.EconomicActivity=EconomicActivity

    def info(self):
        print("Код ПС:", self.CodePS)
        print("Полный Код", self.FullCode)
        print("Наименование", self.Name)
        print("Регистрационный номер", self.RegNumber)
        print("Основная цель вида профессиональной деятельности", self.Description)
        print("Группа занятий:")
        for group in self.OccupationGroup:
            print("Код ОКЗ:", group["CodeOKZ"])
            print("Наименование:", group["Name"])
        print("Отнесение к видам экономической деятельности:")
        for activity in self.EconomicActivity:
            print("Код ОКВЭД:", activity["CodeOKVED"])
            print("Наименование:", activity["Name"])


testData = {
    "CodePS": "06",
    "FullCode": "06.001",
    "Name": "Программист",
    "RegNumber": "4",
    "Description": "Разработка, отладка, проверка работоспособности, модификация компьютерного программного обеспечения",
    "OccupationGroup": [
        {"CodeOKZ": "3512", "Name": "Специалисты-техники по поддержке пользователей ИКТ"},
        {"CodeOKZ": "2512", "Name": "Разработчики программного обеспечения"},
        {"CodeOKZ": "2514", "Name": "Программисты приложений"}
    ],
    "EconomicActivity": [
        {"CodeOKVED": "62.01", "Name": "Разработка компьютерного программного обеспечения"}
    ]
}

test = Speciality(**testData)
test.info()