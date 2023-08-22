import json

def file_open():
    with open('C:\ProgramData\cour3\operations\operations.json', encoding='utf-8') as file:
        operations = json.load(file)
        return operations


