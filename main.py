import file_operations
from faker import Faker
import random
import os


def generate_runic_skills(skills_list, letters_mapping):
    runic_skills = []
    for skill in skills_list:
        runic_skill = skill
        for key, value in letters_mapping.items():
            runic_skill = runic_skill.replace(key, value)
        runic_skills.append(runic_skill)
    return runic_skills


def create_character_card(fake, skills, letters_mapping, card_number):
    
    skills_list = random.sample(skills, 3)
    
    runic_skills = generate_runic_skills(skills_list, letters_mapping)
    
    context = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "town": fake.city(),
        "job": fake.job(),
        "strength": random.randint(3, 18),
        "agility": random.randint(3, 18),
        "endurance": random.randint(3, 18),
        "intelligence": random.randint(3, 18),
        "luck": random.randint(3, 18),
        "skill_1": runic_skills[0],
        "skill_2": runic_skills[1],
        "skill_3": runic_skills[2]
    }
    
    return context


def main():
    fake = Faker("ru_RU")

    skills = [
    "Стремительный прыжок", 
    "Электрический выстрел", 
    "Ледяной удар",
    "Стремительный удар", 
    "Кислотный взгляд", 
    "Тайный побег",
    "Ледяной выстрел", 
    "Огненный заряд"
    ]

    letters_mapping = {
        'а': 'а͠', 
        'б': 'б̋', 
        'в': 'в͒͠',
        'г': 'г͒͠', 
        'д': 'д̋', 
        'е': 'е͠',
        'ё': 'ё͒͠', 
        'ж': 'ж͒', 
        'з': 'з̋̋͠',
        'и': 'и', 
        'й': 'й͒͠', 
        'к': 'к̋̋',
        'л': 'л̋͠', 
        'м': 'м͒͠', 
        'н': 'н͒',
        'о': 'о̋', 
        'п': 'п̋͠', 
        'р': 'р̋͠',
        'с': 'с͒', 
        'т': 'т͒', 
        'у': 'у͒͠',
        'ф': 'ф̋̋͠', 
        'х': 'х͒͠', 
        'ц': 'ц̋',
        'ч': 'ч̋͠', 
        'ш': 'ш͒͠', 
        'щ': 'щ̋',
        'ъ': 'ъ̋͠', 
        'ы': 'ы̋͠', 
        'ь': 'ь̋',
        'э': 'э͒͠͠', 
        'ю': 'ю̋͠', 
        'я': 'я̋',
        'А': 'А͠', 
        'Б': 'Б̋', 
        'В': 'В͒͠',
        'Г': 'Г͒͠', 
        'Д': 'Д̋', 
        'Е': 'Е',
        'Ё': 'Ё͒͠', 
        'Ж': 'Ж͒', 
        'З': 'З̋̋͠',
        'И': 'И', 
        'Й': 'Й͒͠', 
        'К': 'К̋̋',
        'Л': 'Л̋͠', 
        'М': 'М͒͠', 
        'Н': 'Н͒',
        'О': 'О̋', 
        'П': 'П̋͠', 
        'Р': 'Р̋͠',
        'С': 'С͒', 
        'Т': 'Т͒', 
        'У': 'У͒͠',
        'Ф': 'Ф̋̋͠', 
        'Х': 'Х͒͠', 
        'Ц': 'Ц̋',
        'Ч': 'Ч̋͠', 
        'Ш': 'Ш͒͠', 
        'Щ': 'Щ̋',
        'Ъ': 'Ъ̋͠', 
        'Ы': 'Ы̋͠', 
        'Ь': 'Ь̋',
        'Э': 'Э͒͠͠', 
        'Ю': 'Ю̋͠', 
        'Я': 'Я̋',
        ' ': ' '
    }

    if not os.path.exists('results'):
        os.makedirs('results')

    for i in range(10):
        context = create_character_card(fake, skills, letters_mapping, i)
        
        output_filename = "result_{}.svg".format(i + 1)
        output_path = os.path.join('results', output_filename)
        
        file_operations.render_template("charsheet.svg", output_path, context)


if __name__ == '__main__':
    main()