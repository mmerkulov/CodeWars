# Create a function that returns the name of the winner in a fight between two fighters.
# Each fighter takes turns attacking the other and whoever kills the other first is victorious.
# Death is defined as having health <= 0.
# Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.
# Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0.
# # You can mutate the Fighter objects.
# Your function also receives a third argument, a string, with the name of the fighter that attacks first.
import random


class Fighter(object):
    def __init__(self, nickname, health, damage_per_attack):
        self.nickname = nickname
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self):
        return "Fighter({}, {}, {})".format(self.nickname, self.health, self.damage_per_attack)

    __repr__ = __str__


def fighting(fighter1, fighter2, first_name):
    def fight_attack(fighter1, fighter2, first_punch):
        if first_punch == fighter1.nickname:
            fighter2.health = fighter2.health - fighter1.damage_per_attack
            print(
                f'У {fighter1.nickname} здоровье = {fighter1.health} и он наносит урон равный {fighter1.damage_per_attack}, '
                f'здоровье у {fighter2.nickname} становиться {fighter2.health}')
        else:
            fighter1.health = fighter1.health - fighter2.damage_per_attack
            print(
                f'У {fighter2.nickname} здоровье = {fighter2.health} и он наносит урон равный {fighter2.damage_per_attack}, '
                f'здоровье у {fighter1.nickname} становиться {fighter1.health}')

    is_stop = True

    while is_stop:

        if first_name == fighter1.nickname:
            fight_attack(fighter1, fighter2, fighter1.nickname)
            first_name = fighter2.nickname
        else:
            fight_attack(fighter1, fighter2, fighter2.nickname)
            first_name = fighter1.nickname

        if fighter1.health <= 0:
            is_stop = False
            winner = fighter2.nickname

        if fighter2.health <= 0:
            is_stop = False
            winner = fighter1.nickname

    # winner = fighter2.nickname if fighter1.health <= 0 else fighter1.nickname

    return winner


# 1
# fighter1 = Fighter(nickname='Rocky', health=10, damage_per_attack=2)
# fighter2 = Fighter(nickname='Ivan', health=6, damage_per_attack=5)
# 2
# fighter1 = Fighter(nickname='Lew', health=10, damage_per_attack=2)
# fighter2 = Fighter(nickname='Harry', health=5, damage_per_attack=4)
# print(Fighter.fighting(fighter1, fighter2, fighter2.nickname))
# 3
fighter1 = Fighter(nickname='Harald', health=20, damage_per_attack=5)
fighter2 = Fighter(nickname='Harry', health=5, damage_per_attack=4)
print(fighting(fighter1, fighter2, fighter2.nickname))
print(fighter1, fighter2)
# 4
# fighter1 = Fighter(nickname='Harald', health=20, damage_per_attack=5)
# fighter2 = Fighter(nickname='Harry', health=5, damage_per_attack=4)
# print(fighting(fighter1, fighter2, fighter1.nickname))
# 5
# fighter1 = Fighter(nickname='Jerry', health=30, damage_per_attack=3)
# fighter2 = Fighter(nickname='Harald', health=20, damage_per_attack=5)
# print(Fighter.fighting(fighter1, fighter2, fighter1.nickname))
