from project.hero import Hero
from project.elf import Elf
from project.soul_master import SoulMaster
from project.blade_knight import BladeKnight

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
soul_master = SoulMaster("SM", 15)
print(soul_master)
print(soul_master.level)

blade_kn = BladeKnight("Albert", 110)
print(blade_kn.level, blade_kn.username)
print(blade_kn)