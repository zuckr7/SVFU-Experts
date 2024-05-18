import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup


class ProfStandart:
    def __init__(self,title,reg_number,codePS,goal,list_okz,list_okved,generalized_functions):
        self.title = title
        self.reg_number = reg_number
        self.codePS = codePS
        self.goal = goal
        self.list_okz = list_okz
        self.list_okved = list_okved
        self.generalized_functions = generalized_functions


class WorkFunction:
    code = ""
    name = ""
    qualification = ""


class GeneralFunction(WorkFunction):
    possible_jobs = []
    edu_requirements = []
    requirement_experience = []
    special_conditions = []
    particular_functions = []


class ParticularFunction(WorkFunction):
    labor_act = []
    req_skill = []
    knowledge = []


def parse_xml(content):
    try:
        root = ET.fromstring(content)

        title = root.find(".//NameProfessionalStandart").text
        reg_number = root.find(".//RegistrationNumber").text
        codePS = root.find(".//CodeKindProfessionalActivity").text
        goal = root.find(".//PurposeKindProfessionalActivity").text
        list_okz = {unit.find(".//CodeOKZ").text: unit.find(".//NameOKZ").text for unit in root.findall(".//ListOKZ/UnitOKZ")}
        list_okved = {unit.find(".//CodeOKVED").text: unit.find(".//NameOKVED").text for unit in root.findall(".//ListOKVED/UnitOKVED")}

        general_functions = []
        for unit in root.findall(".//GeneralizedWorkFunctions/GeneralizedWorkFunction"):
            general_function = GeneralFunction()
            general_function.code = unit.find(".//CodeOTF").text
            general_function.name = unit.find(".//NameOTF").text
            general_function.qualification = unit.find(".//LevelOfQualification").text
            general_function.possible_jobs = [i.find(".//PossibleJobTitle").text for i in unit.findall(".//PossibleJobTitles")]
            general_function.edu_requirements = [i.find(".//EducationalRequirement").text for i in unit.findall(".//EducationalRequirements")]
            general_function.requirement_experience = [
                i.find(".//RequirementWorkExperience").text if i.find(".//RequirementWorkExperience") is not None else ""
                for i in unit.findall(".//RequirementsWorkExperiences")
            ]
            general_function.special_conditions = [
                i.find(".//SpecialConditionForAdmissionToWork").text if i.find(".//SpecialConditionForAdmissionToWork") is not None else ""
                for i in unit.findall(".//SpecialConditionsForAdmissionToWork")
            ]
            general_functions.append(general_function)

            for i in unit.findall(".//ParticularWorkFunctions/ParticularWorkFunction"):
                particular_function = ParticularFunction()
                particular_function.code = i.find(".//CodeTF").text
                particular_function.name = i.find(".//NameTF").text
                particular_function.qualification = i.find(".//SubQualification").text
                particular_function.labor_act = [
                    i.find(".//LaborAction").text if i.find(".//LaborAction") is not None else ""
                    for i in unit.findall(".//LaborActions")
                ]
                particular_function.req_skill = [
                    i.find(".//RequiredSkill").text if i.find(".//RequiredSkill") is not None else ""
                    for i in unit.findall(".//RequiredSkills")
                ]
                particular_function.knowledge = [
                    i.find(".//NecessaryKnowledge").text if i.find(".//NecessaryKnowledge") is not None else ""
                    for i in unit.findall(".//NecessaryKnowledges")
                ]
                general_functions[-1].particular_functions.append(particular_function)

        return title, reg_number, codePS, goal, list_okz, list_okved, general_functions
    except Exception as e:
        print(f"Ошибка при парсинге XML: {e}")
        return None


def download_xml(fn):
    url = 'https://profstandart.rosmintrud.ru/obshchiy-informatsionnyy-blok/natsionalnyy-reestr-professionalnykh-standartov/reestr-professionalnykh-standartov/wservGenXMLSave.php'
    headers = {'User-Agent': 'Mozilla/5.0'}
    data = {'fn[]': fn, 'save': 'Скачать в XML'}

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        content = response.content
    else:
        print("Ошибка:", response.status_code)
        content = None

    return content


def fn_parser(url):
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    fn_list=[]

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        form = soup.find('form', {'name': 'SaveXML'})

        if form:
            elements = form.find_all('input', {'name': 'fn[]'})
            fn_list = [element['value'] for element in elements]
        else:
            print("Такой формы нет")
    else:
        print("Ошибка:", response.status_code)
    return fn_list


def all_fns():
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://profstandart.rosmintrud.ru/obshchiy-informatsionnyy-blok/natsionalnyy-reestr-professionalnykh-standartov/reestr-professionalnykh-standartov/'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        div = soup.find('div', {'class': 'bx_pagination_page'})

        if div:
            elements = div.find_all('li')
            element = elements[-2].text
        else:
            print("Такой div нет")
            element = 0
    else:
        print("Ошибка:", response.status_code)
        element = 0

    list_of_fn = []
    list_of_fn.append(fn_parser('https://profstandart.rosmintrud.ru/obshchiy-informatsionnyy-blok/natsionalnyy-reestr-professionalnykh-standartov/reestr-professionalnykh-standartov/'))
    for i in range(2, int(element)+1):
        list_of_fn.append(fn_parser('https://profstandart.rosmintrud.ru/obshchiy-informatsionnyy-blok/natsionalnyy-reestr-professionalnykh-standartov/reestr-professionalnykh-standartov/?PAGEN_1=' + str(i) + '&SIZEN_1=20'))
    merged = [element for each_list in list_of_fn for element in each_list]
    return merged


a = download_xml('124707')
# # path1 = 'E:/ЗаровняевАйсен/Курсовая/ProfessionalStandarts_1.xml'
# # path2 = 'E:/ЗаровняевАйсен/Курсовая/ProfessionalStandarts_4.xml'
title, reg_number, codePS, goal, list_okz, list_okved, generalized_functions = parse_xml(a)
print("Наименование:", title)
print("Регистрационный номер:", reg_number)
print("Код ПС:", codePS)
print("Цель:", goal)
print("Лист ОКЗ:", list_okz)
print("Лист ОКВЭД:", list_okved)
# # print("Трудовые функции")
# # for i in generalized_functions:
# #     print(i.name)
# #     for j in i.particular_functions:
# #         print('\t',j.name)
standarts = []
vse_fn = all_fns()
# print(vse_fn)
# print(len(vse_fn))
for fn in vse_fn:
    print("В процессе ", fn)
    title, reg_number, codePS, goal, list_okz, list_okved, generalized_functions = parse_xml(download_xml(fn))
    standarts.append(ProfStandart(title,reg_number,codePS,goal, list_okz,list_okved, generalized_functions ))
    print("Добавлен ", fn)
print(len(standarts))