#The main file - game is played here
import main
import random
import os
import sys
import time

update_stats = '[\'' + player_level + '\',\'' + const_level + '\',\'' + research_level + '\']\n' + power + '\n' + troop_power + '\n' + building_power + '\n' + research_power + '\n' + player_power + '\n' + quest_power + '\n' + '[\'' + castle_level + '\',\'' + vault_level + '\',\'' + academy_level + '\',\'' + barracks_level + '\',\'' + archery_level + '\',\'' + stable_level + '\',\'' + helipad_level + '\',\'' + workshop_level + '\',\']'
['01','00','00','00','00','00','00','00'] bld.basic
['00','00','00','00','00','00','00','00'] bld.prd
['00','00','00','00','00','00'] rsc.inf
['00','00','00','00','00','00'] rsc.arch
['00','00','00','00','00','00'] rsc.cav
['00','00','00','00','00','00'] rsc.air
['00','00','00','00','00'] rsc.sei
['00','00','00','00','00','00'] rsc.arm
00
00
00
00
00
00
00
00
00
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def loadgame():
    print('Loading...')
    time.sleep(0.3)
    print('Loading... 7%')
    time.sleep(0.1)
    print('Loading... 16%')
    time.sleep(0.05)
    print('Loading... 23%')
    time.sleep(0.2)
    print('Loading... 47%')
    time.sleep(0.1)
    print('Loading... 63%')
    time.sleep(0.3)
    print('Loading... 78%')
    time.sleep(0.05)
    print('Loading... 90%')
    time.sleep(0.2)
    print('Loading... 99%')
    time.sleep(0.2)
    cls()
    print('--- Save file loaded ---')

# def passive_stats():

# def infantry_attack_buffs(inf_offense,inf_defense,inf_health,inf_morale,inf_crit_dmg,inf_crit_def):

def research_buffs_inf():
    loadgame()
    f = open('savedata.txt','rt')
    lines = f.readlines()
    infantry_buffs,archer_buffs,cavalry_buffs,airbourne_buffs,seige_buffs,army_buffs = lines[10],lines[11],lines[12],lines[13],lines[14],lines[15]
    checked,checked2,checked3,checked4,checked5,checked6 = 0,0,0,0,0,0
    infdmgchecked,infdefchecked,infhpchecked,infmoralechecked,infcritdmgchecked,infcritdefchecked,archdmgchecked,archdefchecked,archhpchecked,archmoralechecked,archcritdmgchecked,archcritdefchecked,cavdmgchecked,cavdefchecked,cavhpchecked,cavmoralechecked,cavcritdmgchecked,cavcritdefchecked,airdmgchecked,airdefchecked,airhpchecked,airmoralechecked,aircritdmgchecked,aircritdefchecked,seidmgchecked,seidefchecked,seihpchecked,seicritdmgchecked,seicritdefchecked,armydmgchecked,armydefchecked,armyhpchecked,armymoralechecked,armycritdmgchecked,armycritdefchecked = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    while checked != 6:
        tester = random.randint(0,9)
        tester10 = '10'
        if ('0' + str(tester)) in infantry_buffs:
            if ('0' + str(tester)) in infantry_buffs[1:4] and infdmgchecked != True:
                inf_dmg = (tester + tester) * tester
                checked = checked + 1
                infdmgchecked = True
            elif ('0' + str(tester)) in infantry_buffs[5:9] and infdefchecked != True:
                inf_def = ((tester + tester) * tester) / 2
                checked = checked + 1
                infdefchecked = True
            elif ('0' + str(tester)) in infantry_buffs[10:14] and infhpchecked != True:
                inf_HP = (tester + tester) * tester
                checked = checked + 1
                infhpchecked = True
            elif ('0' + str(tester)) in infantry_buffs[15:19] and infmoralechecked != True:
                inf_morale = (tester + tester) * tester
                checked = checked + 1
                infmoralechecked = True
            elif ('0' + str(tester)) in infantry_buffs[20:24] and infcritdmgchecked != True:
                inf_crit_dmg = (tester + tester) * tester
                checked = checked + 1
                infcritdmgchecked = True
            elif ('0' + str(tester)) in infantry_buffs[25:29] and infcritdefchecked != True:
                inf_crit_def = (tester + tester) * tester
                checked = checked + 1
                infcritdefchecked = True
        elif str(tester10) in infantry_buffs:
            if str(tester10) in infantry_buffs[1:4] and infdmgchecked != True:
                inf_dmg = 200
                checked = checked + 1
                infdmgchecked = True
            elif str(tester10) in infantry_buffs[5:9] and infdefchecked != True:
                inf_def = 95
                checked = checked + 1
                infdefchecked = True
            elif str(tester10) in infantry_buffs[10:14] and infhpchecked != True:
                inf_HP = 200
                checked = checked + 1
                infhpchecked = True
            elif str(tester10) in infantry_buffs[15:19] and infmoralechecked != True:
                inf_morale = 200
                checked = checked + 1
                infmoralechecked = True
            elif str(tester10) in infantry_buffs[20:24] and infcritdmgchecked != True:
                inf_crit_dmg = 400
                checked = checked + 1
                infcritdmgchecked = True
            elif str(tester10) in infantry_buffs[25:29] and infcritdefchecked != True:
                inf_crit_def = 190
                checked = checked + 1
                infcritdefchecked = True
    while checked2 != 6:
        tester2 = random.randint(0,9)
        tester2_10 = 10
        if ('0' + str(tester2)) in archer_buffs:
            if ('0' + str(tester2)) in archer_buffs[1:4] and archdmgchecked != True:
                arch_dmg = (tester2 + tester2) * tester2
                checked2 = checked2 + 1
                archdmgchecked = True
            elif ('0' + str(tester2)) in archer_buffs[5:9] and archdefchecked != True:
                arch_def = ((tester2 + tester2) * tester2) / 2
                checked2 = checked2 + 1
                archdefchecked = True
            elif ('0' + str(tester2)) in archer_buffs[10:14] and archhpchecked != True:
                arch_HP = (tester2 + tester2) * tester2
                checked2 = checked2 + 1
                archhpchecked = True
            elif ('0' + str(tester2)) in archer_buffs[15:19] and archmoralechecked != True:
                arch_morale = (tester2 + tester2) * tester2
                checked2 = checked2 + 1
                archmoralechecked = True
            elif ('0' + str(tester2)) in archer_buffs[20:24] and archcritdmgchecked != True:
                arch_crit_dmg = (tester2 + tester2) * tester2
                checked2 = checked2 + 1
                archcritdmgchecked = True
            elif ('0' + str(tester2)) in archer_buffs[25:29] and archcritdefchecked != True:
                arch_crit_def = (tester2 + tester2) * tester2
                checked2 = checked2 + 1
                archcritdefchecked = True
        elif str(tester2_10) in archer_buffs:
            if str(tester2_10) in archer_buffs[1:4] and archdmgchecked != True:
                arch_dmg = 200
                checked2 = checked2 + 1
                archdmgchecked = True
            elif str(tester2_10) in archer_buffs[5:9] and archdefchecked != True:
                arch_def = 95
                checked2 = checked2 + 1
                archdefchecked = True
            elif str(tester2_10) in archer_buffs[10:14] and archhpchecked != True:
                arch_HP = 200
                checked2 = checked2 + 1
                archhpchecked = True
            elif str(tester2_10) in archer_buffs[15:19] and archmoralechecked != True:
                arch_morale = 200
                checked2 = checked2 + 1
                archmoralechecked = True
            elif str(tester2_10) in archer_buffs[20:24] and archcritdmgchecked != True:
                arch_crit_dmg = 400
                checked2 = checked2 + 1
                archcritdmgchecked = True
            elif str(tester2_10) in archer_buffs[25:29] and archcritdefchecked != True:
                arch_crit_def = 190
                checked2 = checked2 + 1
                archcritdefchecked = True
    while checked3 != 6:
        tester3 = random.randint(0,9)
        tester3_10 = 10
        if ('0' + str(tester3)) in cavalry_buffs:
            if ('0' + str(tester3)) in cavalry_buffs[1:4] and cavdmgchecked != True:
                cav_dmg = (tester3 + tester3) * tester3
                checked3 = checked3 + 1
                cavdmgchecked = True
            elif ('0' + str(tester3)) in cavalry_buffs[5:9] and cavdefchecked != True:
                cav_def = ((tester3 + tester3) * tester3) / 2
                checked3 = checked3 + 1
                cavdefchecked = True
            elif ('0' + str(tester3)) in cavalry_buffs[10:14] and cavhpchecked != True:
                cav_HP = (tester3 + tester3) * tester3
                checked3 = checked3 + 1
                cavhpchecked = True
            elif ('0' + str(tester3)) in cavalry_buffs[15:19] and cavmoralechecked != True:
                cav_morale = (tester3 + tester3) * tester3
                checked3 = checked3 + 1
                cavmoralechecked = True
            elif ('0' + str(tester3)) in cavalry_buffs[20:24] and cavcritdmgchecked != True:
                cav_crit_dmg = (tester3 + tester3) * tester3
                checked3 = checked3 + 1
                cavcritdmgchecked = True
            elif ('0' + str(tester3)) in cavalry_buffs[25:29] and cavcritdefchecked != True:
                cav_crit_def = (tester3 + tester3) * tester3
                checked3 = checked3 + 1
                cavcritdefchecked = True
        elif str(tester3_10) in cavalry_buffs:
            if str(tester3_10) in cavalry_buffs[1:4] and cavdmgchecked != True:
                cav_dmg = 200
                checked3 = checked3 + 1
                cavdmgchecked = True
            elif str(tester3_10) in cavalry_buffs[5:9] and cavdefchecked != True:
                cav_def = 95
                checked3 = checked3 + 1
                cavdefchecked = True
            elif str(tester3_10) in cavalry_buffs[10:14] and cavhpchecked != True:
                cav_HP = 200
                checked3 = checked3 + 1
                cavhpchecked = True
            elif str(tester3_10) in cavalry_buffs[15:19] and cavmoralechecked != True:
                cav_morale = 200
                checked3 = checked3 + 1
                cavmoralechecked = True
            elif str(tester3_10) in cavalry_buffs[20:24] and cavcritdmgchecked != True:
                cav_crit_dmg = 400
                checked3 = checked3 + 1
                cavcritdmgchecked = True
            elif str(tester3_10) in cavalry_buffs[25:29] and cavcritdefchecked != True:
                cav_crit_def = 190
                checked3 = checked3 + 1
                cavcritdefchecked = True
    while checked4 != 6:
        tester4 = random.randint(0,9)
        tester4_10 = 10
        if ('0' + str(tester4)) in airbourne_buffs:
            if ('0' + str(tester4)) in airbourne_buffs[1:4] and airdmgchecked != True:
                air_dmg = (tester4 + tester4) * tester4
                checked4 = checked4 + 1
                airdmgchecked = True
            elif ('0' + str(tester4)) in airbourne_buffs[5:9] and airdefchecked != True:
                air_def = ((tester4 + tester4) * tester4) / 2
                checked4 = checked4 + 1
                airdefchecked = True
            elif ('0' + str(tester4)) in airbourne_buffs[10:14] and airhpchecked != True:
                air_HP = (tester4 + tester4) * tester4
                checked4 = checked4 + 1
                airhpchecked = True
            elif ('0' + str(tester4)) in airbourne_buffs[15:19] and airmoralechecked != True:
                air_morale = (tester4 + tester4) * tester4
                checked4 = checked4 + 1
                airmoralechecked = True
            elif ('0' + str(tester4)) in airbourne_buffs[20:24] and aircritdmgchecked != True:
                air_crit_dmg = (tester4 + tester4) * tester4
                checked4 = checked4 + 1
                aircritdmgchecked = True
            elif ('0' + str(tester4)) in airbourne_buffs[25:29] and aircritdefchecked != True:
                air_crit_def = (tester4 + tester4) * tester4
                checked4 = checked4 + 1
                aircritdefchecked = True
        elif str(tester4_10) in airbourne_buffs:
            if str(tester4_10) in airbourne_buffs[1:4] and airdmgchecked != True:
                air_dmg = 200
                checked4 = checked4 + 1
                airdmgchecked = True
            elif str(tester4_10) in airbourne_buffs[5:9] and airdefchecked != True:
                air_def = 95
                checked4 = checked4 + 1
                airdefchecked = True
            elif str(tester4_10) in airbourne_buffs[10:14] and airhpchecked != True:
                air_HP = 200
                checked4 = checked4 + 1
                airhpchecked = True
            elif str(tester4_10) in airbourne_buffs[15:19] and airmoralechecked != True:
                air_morale = 200
                checked4 = checked4 + 1
                airmoralechecked = True
            elif str(tester4_10) in airbourne_buffs[20:24] and aircritdmgchecked != True:
                air_crit_dmg = 400
                checked4 = checked4 + 1
                aircritdmgchecked = True
            elif str(tester4_10) in airbourne_buffs[25:29] and aircritdefchecked != True:
                air_crit_def = 190
                checked4 = checked4 + 1
                aircritdefchecked = True
    while checked5 != 5:
        tester5 = random.randint(0,9)
        tester5_10 = 10
        if ('0' + str(tester5)) in seige_buffs:
            if ('0' + str(tester5)) in seige_buffs[1:4] and seidmgchecked != True:
                sei_dmg = (tester5 + tester5) * tester5
                checked5 = checked5 + 1
                seidmgchecked = True
            elif ('0' + str(tester5)) in seige_buffs[5:9] and seidefchecked != True:
                sei_def = ((tester5 + tester5) * tester5) / 2
                checked5 = checked5 + 1
                seidefchecked = True
            elif ('0' + str(tester5)) in seige_buffs[10:14] and seihpchecked != True:
                sei_HP = (tester5 + tester5) * tester5
                checked5 = checked5 + 1
                seihpchecked = True
            elif ('0' + str(tester5)) in seige_buffs[15:19] and seicritdmgchecked != True:
                sei_crit_dmg = (tester5 + tester5) * tester5
                checked5 = checked5 + 1
                seicritdmgchecked = True
            elif ('0' + str(tester5)) in seige_buffs[20:24] and seicritdefchecked != True:
                sei_crit_def = (tester5 + tester5) * tester5
                checked5 = checked5 + 1
                seicritdefchecked = True
        elif str(tester5_10) in seige_buffs:
            if str(tester5_10) in seige_buffs[1:4] and seidmgchecked != True:
                sei_dmg = 200
                checked5 = checked5 + 1
                seidmgchecked = True
            elif str(tester5_10) in seige_buffs[5:9] and seidefchecked != True:
                sei_def = 95
                checked5 = checked5 + 1
                seidefchecked = True
            elif str(tester5_10) in seige_buffs[10:14] and seihpchecked != True:
                sei_HP = 200
                checked5 = checked5 + 1
                seihpchecked = True
            elif str(tester5_10) in seige_buffs[15:19] and seicritdmgchecked != True:
                sei_crit_dmg = 400
                checked5 = checked5 + 1
                seicritdmgchecked = True
            elif str(tester5_10) in seige_buffs[20:24] and seicritdefchecked != True:
                sei_crit_def = 190
                checked5 = checked5 + 1
                seicritdefchecked = True
    while checked6 != 6:
        tester6 = random.randint(0,9)
        tester6_10 = 10
        if ('0' + str(tester6)) in army_buffs:
            if ('0' + str(tester6)) in army_buffs[1:4] and armydmgchecked != True:
                army_dmg = (tester6 + tester6) * tester6
                checked6 = checked6 + 1
                armydmgchecked = True
            elif ('0' + str(tester6)) in army_buffs[5:9] and armydefchecked != True:
                army_def = ((tester6 + tester6) * tester6) / 2
                checked6 = checked6 + 1
                armydefchecked = True
            elif ('0' + str(tester6)) in army_buffs[10:14] and armyhpchecked != True:
                army_HP = (tester6 + tester6) * tester6
                checked6 = checked6 + 1
                armyhpchecked = True
            elif ('0' + str(tester6)) in army_buffs[15:19] and armymoralechecked != True:
                army_morale = (tester6 + tester6) * tester6
                checked6 = checked6 + 1
                armymoralechecked = True
            elif ('0' + str(tester6)) in army_buffs[20:24] and armycritdmgchecked != True:
                army_crit_dmg = (tester6 + tester6) * tester6
                checked6 = checked6 + 1
                armycritdmgchecked = True
            elif ('0' + str(tester6)) in army_buffs[25:29] and armycritdefchecked != True:
                army_crit_def = (tester6 + tester6) * tester6
                checked6 = checked6 + 1
                armycritdefchecked = True
        elif str(tester6_10) in army_buffs:
            if str(tester6_10) in army_buffs[1:4] and armydmgchecked != True:
                army_dmg = 200
                checked6 = checked6 + 1
                armydmgchecked = True
            elif str(tester6_10) in army_buffs[5:9] and armydefchecked != True:
                army_def = 95
                checked6 = checked6 + 1
                armydefchecked = True
            elif str(tester6_10) in army_buffs[10:14] and armyhpchecked != True:
                army_HP = 200
                checked6 = checked6 + 1
                armyhpchecked = True
            elif str(tester6_10) in army_buffs[15:19] and armymoralechecked != True:
                army_morale = 200
                checked6 = checked6 + 1
                armymoralechecked = True
            elif str(tester6_10) in army_buffs[20:24] and armycritdmgchecked != True:
                army_crit_dmg = 400
                checked6 = checked6 + 1
                armycritdmgchecked = True
            elif str(tester6_10) in army_buffs[25:29] and armycritdefchecked != True:
                army_crit_def = 190
                checked6 = checked6 + 1
                armycritdefchecked = True
    return(lines,inf_dmg,inf_def,inf_HP,inf_morale,inf_crit_dmg,inf_crit_def,arch_dmg,arch_def,arch_HP,arch_morale,arch_crit_dmg,arch_crit_def,cav_dmg,cav_def,cav_HP,cav_morale,cav_crit_dmg,cav_crit_def,air_dmg,air_def,air_HP,air_morale,air_crit_dmg,air_crit_def,sei_dmg,sei_def,sei_HP,sei_crit_dmg,sei_crit_def,army_dmg,army_def,army_HP,army_morale,army_crit_dmg,army_crit_def)
            # 1:4 5:9 10:14 15:19 20:24 25:29

def game():
    lines,inf_dmg,inf_def,inf_HP,inf_morale,inf_crit_dmg,inf_crit_def,arch_dmg,arch_def,arch_HP,arch_morale,arch_crit_dmg,arch_crit_def,cav_dmg,cav_def,cav_HP,cav_morale,cav_crit_dmg,cav_crit_def,air_dmg,air_def,air_HP,air_morale,air_crit_dmg,air_crit_def,sei_dmg,sei_def,sei_HP,sei_crit_dmg,sei_crit_def,army_dmg,army_def,army_HP,army_morale,army_crit_dmg,army_crit_def = research_buffs_inf()
    time.sleep(1)
    cls()
    p = True
    while p == True:
        q = input('What would you like to do?\n\nm - Map\n\nc - Go to castle\n\na - Attack\n\n> ')
        if q == 'c':
            return lines,inf_dmg,inf_def,inf_HP,inf_morale,inf_crit_dmg,inf_crit_def,arch_dmg,arch_def,arch_HP,arch_morale,arch_crit_dmg,arch_crit_def,cav_dmg,cav_def,cav_HP,cav_morale,cav_crit_dmg,cav_crit_def,air_dmg,air_def,air_HP,air_morale,air_crit_dmg,air_crit_def,sei_dmg,sei_def,sei_HP,sei_crit_dmg,sei_crit_def,army_dmg,army_def,army_HP,army_morale,army_crit_dmg,army_crit_def
            p = False
        else:
            print('That is not a valid option.')
            cls()

def construction(construction_time, type):
    print('a')
    f = open('savedata.txt','rt')
    lines = f.readlines()
    buildings = lines[8]
    const = lines[16]
    type = int(type)
    const_spd,const_spd2,const_spd3 = (int(const[2:4]) - 10),(int(const[7:9]) - 10),(int(const[12:14]) - 10)
    print(const_spd3)
    if const_spd + const_spd2 + const_spd3 == 0:
        final_time = construction_time
        time.sleep(final_time)
        print('Construction complete!')
        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 1:
        final_time = (construction_time / 100) * 99.3
        time.sleep(final_time)
        print('Construction complete!')
        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 2:
        final_time = (construction_time / 100) * 98.5
        time.sleep(final_time)
        print('Construction complete!')
        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 3:
        final_time = (construction_time / 100) * 97.6
        time.sleep(final_time)
        print('Construction complete!')
        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 4:
        final_time = (construction_time / 100) * 96.6
        time.sleep(final_time)
        print('Construction complete!')
        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 5:
        final_time = (construction_time / 100) * 95.5
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 6:
        final_time = (construction_time / 100) * 94.3
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 7:
        final_time = (construction_time / 100) * 93
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 8:
        final_time = (construction_time / 100) * 91.6
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 9:
        final_time = (construction_time / 100) * 90.1
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 10:
        final_time = (construction_time / 100) * 88.5
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 11:
        final_time = (construction_time / 100) * 86.8
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 12:
        final_time = (construction_time / 100) * 85
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 13:
        final_time = (construction_time / 100) * 83
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 14:
        final_time = (construction_time / 100) * 80.5
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 15:
        final_time = (construction_time / 100) * 77.5
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 16:
        final_time = (construction_time / 100) * 74
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 17:
        final_time = (construction_time / 100) * 70
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 17:
        final_time = (construction_time / 100) * 65.5
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 18:
        final_time = (construction_time / 100) * 60.5
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 19:
        final_time = (construction_time / 100) * 65
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 20:
        final_time = (construction_time / 100) * 59
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 21:
        final_time = (construction_time / 100) * 52.5
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 22:
        final_time = (construction_time / 100) * 45.5
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 23:
        final_time = (construction_time / 100) * 38
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 24:
        final_time = (construction_time / 100) * 30
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 25:
        final_time = (construction_time / 100) * 23.5
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 26:
        final_time = (construction_time / 100) * 18
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 27:
        final_time = (construction_time / 100) * 13.5
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 28:
        final_time = (construction_time / 100) * 10
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 29:
        final_time = (construction_time / 100) * 7.5
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1
    elif const_spd + const_spd2 + const_spd3 == 30:
        final_time = (construction_time / 100) * 5
        time.sleep(final_time)
        print('Construction complete!')

        type = type + 1




def castle():
    lines,inf_dmg,inf_def,inf_HP,inf_morale,inf_crit_dmg,inf_crit_def,arch_dmg,arch_def,arch_HP,arch_morale,arch_crit_dmg,arch_crit_def,cav_dmg,cav_def,cav_HP,cav_morale,cav_crit_dmg,cav_crit_def,air_dmg,air_def,air_HP,air_morale,air_crit_dmg,air_crit_def,sei_dmg,sei_def,sei_HP,sei_crit_dmg,sei_crit_def,army_dmg,army_def,army_HP,army_morale,army_crit_dmg,army_crit_def = game()
    cls()
    food = 100000
    timber = 100000
    stone = 100000
    metal = 100000
    silver = 60000
    gold = 20000
    buildings,buildings2 = lines[8],lines[9]
    castle_lv,vault_lv,academy_lv,barracks_lv,archery_lv,stable_lv,helipad_lv,workshop_lv = buildings[2:4],buildings[7:9],buildings[12:14],buildings[17:19],buildings[22:24],buildings[27:29],buildings[32:34],buildings[37:39]
    farm_lv,lumber_lv,quarry_lv,mine_lv,silver_lv,gold_lv,crystal_lv,overseer_lv = buildings2[2:4],buildings2[7:9],buildings2[12:14],buildings2[17:19],buildings2[22:24],buildings2[27:29],buildings2[32:34],buildings2[37:39]
    q = 'Undefined'
    looper = True
    build_choices = ['c','v','a','b','r','s','h','w','p','q']
    while looper == True:
        cls()
        q = input('c - Construct\n\nr = Research\n\nt = Train\n\nq = Leave castle\n\n> ')
        if q == 'c':
            time.sleep(1)
            cls()
            build_selection = input('---Construction tree---\n\nBasic buildings:\nCastle:' + str(castle_lv) + '\nVault:' + str(vault_lv) + '\nAcademy:' + str(academy_lv) + '\nBarracks:' + str(barracks_lv) + '\nRecon zone:' + str(archery_lv) + '\nStable:' + str(stable_lv) + '\nHelipad:' + str(helipad_lv) + '\nWorkshop:' + str(workshop_lv) + '\nType the first letter of the building you wish to upgrade, go to production buildings (p) or quit (q)\n\n> ')
            if build_selection in build_choices:
                if build_selection == 'c':
                    if workshop_lv == '00':
                        print('Prerequisites not met: Workshop [Lv1]')
                        time.sleep(1)
                elif build_selection == 'w':
                    if helipad_lv == '00':
                        print('Prerequisites not met: Helipad [Lv1]')
                        time.sleep(1)
                elif build_selection == 'h':
                    if stable_lv == '00':
                        print('Prerequisites not met: Stable [Lv1]')
                        time.sleep(1)
                elif build_selection == 's':
                    if archery_lv == '00':
                        print('Prerequisites not met: Recon zone [Lv1]')
                        time.sleep(1)
                elif build_selection == 'r':
                    if barracks_lv == '00':
                        print('Prerequisites not met: Barracks [Lv1]')
                        time.sleep(1)
                elif build_selection == 'b':
                    if academy_lv == '00':
                        print('Prerequisites not met: Academy [Lv1]')
                        time.sleep(1)
                elif build_selection == 'a':
                    if vault_lv == '00':
                        print('Prerequisites not met: Vault [Lv1]')
                        time.sleep(1)
                    elif vault_lv == '01':
                        vault_level = 1
                        print('The cost to build academy is:\n4,000 timber\n4,000 stone\n4,000 metal\n2,400 silver.')
                        time.sleep(1)
                        if timber > 4000 and stone > 4000 and metal > 4000 and silver > 2400:
                            construction_time = 4
                            cls()
                            print('Construction has begun!')
                            looper == False
                            looper = construction(4,academy_lv)
                elif build_selection == 'v':
                    if castle_lv == '01':
                        castle_level = 1
                        print('The cost to build vault is:\n5,000 timber\n2,000 stone\n5,000 metal')
                        time.sleep(1)
                        if timber > 5000 and stone > 2000 and metal > 5000:
                            construction_time = 3
                            cls()
                            print('Construction has begun!')
                            looper == False
                            looper = construction(3,vault_lv)
                elif build_selection == 'p':
                    print('Coming soon')
                elif build_selection == 'q':
                    print('a')
        elif q == 'r':
            cls()
            if research == 1 and inf_crit_dmg == 0:
                print('---Research tree---\n\n\t\tUnlock Barracks\n\t\t\t\t¦\n\t\t\t\tv\n\n\t\tInfantry Offense (Locked)')
            elif inf_dmg == 2:
                print('---Research tree---\n\n\t\tUnlock Barracks\n\t\t\t\t¦\n\t\t\t\tv\n\n\t\tInfantry Offense (Locked)')
castle()
