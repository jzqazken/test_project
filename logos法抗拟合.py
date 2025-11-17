import random
import statistics

# total_total_damage = 0
# total_damage_list = []
runs = 100000
data = []
# a = float(input("直接加算："))
# b = float(input("直接乘算："))
# c = float(input("最终乘算："))
# d = float(input("攻速："))
# e = float(input("法抗："))
# f = float(input("减伤乘区："))
a = 0
b = 0
c = 0
d = 0
e = 0
f = 1
for i in range(10):
    total_total_damage = 0
    total_damage_list = []
    e = i * 0.1
    for run in range(runs):
        atk = 855 * (1 + a) * (4 + b)
        mr = e
        total_damage = 0
        elmt_hp = 1000
        elmt_count = 0
        hit_num = int(30 / (1.6 / (1 + d)) + 1)
        elmt_count_num = int(15 / (1.6 / (1 + d)) + 1)
        for hit in range(hit_num):
            if random.random() < 0.6:
                total_damage += (atk + 0.65 * atk + 165 * 2) * (1 - mr) * f * (1 + c)
                elmt_hp -= (atk + 0.65 * atk + 165 * 2) * (1 - mr) * 0.08 * f * (1 + c)
                if elmt_hp <= 0:
                    total_damage += 0.6 * atk + 12000/elmt_count_num
                    elmt_count += 1
                    if elmt_count >= elmt_count_num:
                        elmt_hp = 1000
                        elmt_count = 0
            else:
                total_damage += (atk + 165) * (1 - mr) * f * (1 + c)
                elmt_hp -= (atk + 165) * (1 - mr) * 0.08 * f * (1 + c)
                if elmt_hp <= 0:
                    total_damage += 12000/elmt_count_num
                    elmt_count += 1
                    if elmt_count >= elmt_count_num:
                        elmt_hp = 1000
                        elmt_count = 0
        while elmt_count < elmt_count_num and elmt_count != 0:
            total_damage += 12000 / elmt_count_num
            elmt_count += 1
        total_total_damage += total_damage
        total_damage_list.append(total_damage)
    mean = total_total_damage / runs
    print(mean)
    data.append(mean)
print(data)
# std_dev = statistics.stdev(total_damage_list)
# print(std_dev / mean)

# 1.08 1.5 0.7 4.1 0.575 0.81