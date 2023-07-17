from random import randint
from graphic_arts.start_game_banner import run_screensaver


class Character:
    def __init__(self, char_name) -> None:
        self.char_name = char_name

    def attack(self) -> str:
        pass

    def defence(self) -> str:
        pass

    def special(self) -> str:
        pass


class Warrior(Character):
    def attack(self) -> str:
        return super().attack()

    def defence(self) -> str:
        return super().defence()

    def special(self) -> str:
        return super().special()


class Mage(Character):
    def attack(self) -> str:
        return super().attack()

    def defence(self) -> str:
        return super().defence()

    def special(self) -> str:
        return super().special()


class Healer(Character):
    def attack(self) -> str:
        return super().attack()

    def defence(self) -> str:
        return super().defence()

    def special(self) -> str:
        return super().special()


def attack(char_name: str, char_class: str) -> str:
    """Start the training process.

    Matches the char_class with existing classes
    and displays the damage inflicted on the enemy.

    Args:
        char_name: The name you gave the character.
        char_class: The class you chose for your character.
    """
    if char_class == 'warrior':
        return (f'{char_name} нанёс противнику урон, равный '
                f'{5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс противнику урон, равный '
                f'{5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} нанёс противнику урон, равный '
                f'{5 + randint(-3, -1)}')
    return (f'{char_name} не нанёс урон')


def defence(char_name: str, char_class: str) -> str:
    """Start the defending process.

    Matches the char_class with existing classes
    and displays the damage blocked by the character.

    Args:
        char_name: The name you gave the character.
        char_class: The class you chose for your character.
    """
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} ед. урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} ед. урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} ед. урона')
    return (f'{char_name} ничего не блокировал')


def special(char_name: str, char_class: str) -> str:
    """Trigger the use of a special skill.

    Matches the char_class with existing classes
    and displays special skill usage.

    Args:
        char_name: The name you gave the character.
        char_class: The class you chose for your character.
    """
    if char_class == 'warrior':
        return (f'{char_name} применил специальное умение '
                f'«Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} применил специальное умение «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} применил специальное умение «Защита {10 + 30}»')
    return (f'{char_name} не применил специальное умение')


def start_training(char_name: str, char_class: str) -> str:
    """Start training process.

    Matches the char_class with existing classes
    and starts training.

    Args:
        char_name: The name you gave the character.
        char_class: The class you chose for your character.
    """
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — великий мастер ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Start process of choosing char_class."""
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, '
                           'за которого хочешь играть: Воитель — warrior, '
                           'Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
