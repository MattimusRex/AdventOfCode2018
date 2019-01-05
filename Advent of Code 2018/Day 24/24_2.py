import sys

class Group:
    def __init__(self, id, num_of_units, unit_hp, initiative, attack_dmg, attack_type, weaknesses, immunities, side):
        self.id = id
        self.num_of_units = num_of_units
        self.unit_hp = unit_hp
        self.initiative = initiative
        self.attack_dmg = attack_dmg
        self.attack_type = attack_type
        self.weaknesses = weaknesses
        self.immunities = immunities
        self.side = side
        self.target = None
        self.attacker = None
        self.dead = False

    def attack(self, target):
        if target is None or target.dead == True:
            return
        eff_pow = self.get_effective_power()
        if self.attack_type in target.weaknesses:
            eff_pow *= 2

        units_killed = min(eff_pow // target.unit_hp, target.num_of_units)
        #print(f"{self.side} Group {self.id} attacks {target.side} group {target.id} dealing {eff_pow} damage and killing {units_killed} units")

        target.num_of_units -= units_killed
        if target.num_of_units < 0:
            target.num_of_units = 0
        if target.num_of_units == 0:
            target.dead = True

    def get_effective_power(self):
        return self.num_of_units * self.attack_dmg
    
    def get_target(self, target_list):
        eff_pow = self.get_effective_power()
        targets = []
        max_dmg = -1
        for group in target_list:
            dmg = eff_pow
            if self.attack_type in group.weaknesses:
                dmg *= 2
            elif self.attack_type in group.immunities:
                continue
            if dmg == max_dmg:
                targets.append(group)
            elif dmg > max_dmg:
                max_dmg = dmg
                targets = []
                targets.append(group)

        if len(targets) > 0:
            if len(targets) > 1:
                temp = []
                max_eff_pow = -1
                for target in targets:
                    if target.get_effective_power() > max_eff_pow:
                        temp = []
                        temp.append(target)
                        max_eff_pow = target.get_effective_power()
                    elif target.get_effective_power() == max_eff_pow:
                        temp.append(target)
                targets = temp
            if len(targets) > 1:
                target = max(targets, key=lambda group: group.initiative)
            else:
                target = targets[0]
            target.attacker = self
            return target
        else:
            return None
    
    def print(self):
        print(f"Side: {self.side} ID: {self.id} # Units: {self.num_of_units}")

####TEST DATA####
# boost = 1570
# immune_system = []
# group = Group(1, 17, 5390, 2, 4507 + boost, 'fire', ['radiation', 'bludgeoning'], [], 'immune')
# immune_system.append(group)
# group = Group(2, 989, 1274, 3, 25 + boost, 'slashing', ['bludgeoning', 'slashing'], ['fire'], 'immune')
# immune_system.append(group)

# infection = []
# group = Group(1, 801, 4706, 1, 116, 'bludgeoning', ['radiation'], [], 'infection')
# infection.append(group)
# group = Group(2, 4485, 2961, 4, 12, 'slashing', ['fire', 'cold'], ['radiation'], 'infection')
# infection.append(group)

#####REAL DATA####
#(self, id, num_of_units, unit_hp, initiative, attack_dmg, attack_type, weaknesses, immunities, side):

boost = 34
immune_system = []
group = Group(1, 8808, 5616, 10, 5 + boost, 'bludgeoning', ['radiation'], ['cold'], 'immune')
immune_system.append(group)
group = Group(2, 900, 13511, 20, 107 + boost, 'radiation', ['radiation'], [], 'immune')
immune_system.append(group)
group = Group(3, 581, 10346, 14, 140 + boost, 'fire', ['radiation'], ['slashing'], 'immune')
immune_system.append(group)
group = Group(4, 57, 9991, 4, 1690 + boost, 'fire', ['bludgeoning'], ['slashing', 'radiation', 'fire'], 'immune')
immune_system.append(group)
group = Group(5, 4074, 6549, 2, 15 + boost, 'radiation', ['fire'], [], 'immune')
immune_system.append(group)
group = Group(6, 929, 5404, 16, 45 + boost, 'fire', [], ['bludgeoning', 'radiation'], 'immune')
immune_system.append(group)
group = Group(7, 2196, 3186, 11, 10 + boost, 'fire', ['fire'], ['radiation'], 'immune')
immune_system.append(group)
group = Group(8, 4420, 9691, 7, 21 + boost, 'fire', ['radiation'], ['fire'], 'immune')
immune_system.append(group)
group = Group(9, 3978, 2306, 12, 4 + boost, 'fire', ['cold', 'radiation'], [], 'immune')
immune_system.append(group)
group = Group(10, 1284, 4487, 19, 32 + boost, 'slashing', ['radiation', 'bludgeoning'], [], 'immune')
immune_system.append(group)

infection = []
group = Group(1, 4262, 23427, 8, 9, 'slashing', ['slashing'], ['fire'], 'infection')
infection.append(group)
group = Group(2, 217, 9837, 1, 73, 'bludgeoning', ['bludgeoning'], [], 'infection')
infection.append(group)
group = Group(3, 5497, 33578, 17, 11, 'slashing', ['cold', 'radiation'], [], 'infection')
infection.append(group)
group = Group(4, 866, 41604, 15, 76, 'radiation', ['cold'], [], 'infection')
infection.append(group)
group = Group(5, 1823, 19652, 13, 20, 'slashing', ['fire', 'cold'], [], 'infection')
infection.append(group)
group = Group(6, 2044, 23512, 9, 22, 'slashing', ['cold'], [], 'infection')
infection.append(group)
group = Group(7, 373, 40861, 18, 215, 'slashing', [], ['cold'], 'infection')
infection.append(group)
group = Group(8, 5427, 43538, 5, 15, 'slashing', ['bludgeoning'], ['radiation'], 'infection')
infection.append(group)
group = Group(9, 3098, 19840, 3, 12, 'radiation', ['bludgeoning', 'cold'], [], 'infection')
infection.append(group)
group = Group(10, 785, 14669, 6, 30, 'fire', [], [], 'infection')
infection.append(group)


round = 0
while len(immune_system) > 0 and len(infection) > 0:
    all_groups = infection + immune_system
    all_groups = sorted(all_groups, key=lambda group: group.initiative, reverse=True)
    all_groups = sorted(all_groups, key=lambda group: group.get_effective_power(), reverse=True)

    for group in all_groups:
        if group.side == 'immune':
            target_list = [x for x in infection if x.attacker is None]
        else:
            target_list = [x for x in immune_system if x.attacker is None]
        group.target = group.get_target(target_list)

    
    all_groups = sorted(all_groups, key=lambda group: group.initiative, reverse=True)
    for group in all_groups:
        if group.dead == False:
            group.attack(group.target)
    
    for group in all_groups:
        group.attacker = None
        group.target = None

    immune_system = [x for x in immune_system if x.dead == False]
    infection = [x for x in infection if x.dead == False]

if len(immune_system) > 0:
    winning_army = immune_system
else:
    winning_army = infection

units_remaining = 0
for group in winning_army:
    group.print()
    units_remaining += group.num_of_units

print(winning_army[0].side)
print(units_remaining)

