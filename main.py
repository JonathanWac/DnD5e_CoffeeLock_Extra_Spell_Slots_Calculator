import GLOBS
from collections import deque
from typing import Dict

import config


def getNextSlot( current_slot, current_sorcPoints, max_sorcPoints) -> str:
    next_slot = "2"
    if (current_sorcPoints >= 7) and (max_sorcPoints >= 7):
        next_slot = "5"
    elif (current_sorcPoints >= 6) and (max_sorcPoints >= 6):
        next_slot = "4"
    elif (current_sorcPoints >= 5) and (max_sorcPoints >= 5):
        next_slot = "3"
    elif (current_sorcPoints >= 3) and (max_sorcPoints >= 3):
        next_slot = "2"
    elif (current_sorcPoints >= 2) and (max_sorcPoints >= 2):
        next_slot = "1"
    return next_slot


def calculate_extra_mana_slots_mixture_byHours(time_in_hours: int, sorcerer_points_per_warlock_slot, max_sorcPoints):
    warlock_spell_slots = time_in_hours * 2
    total_sorcery_points = warlock_spell_slots * sorcerer_points_per_warlock_slot
    mana_slots = {"Function": "Extra Slots: Distributed", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

    sorcery_points = total_sorcery_points

    queue = deque()
    queue.append(7)
    queue.append(6)
    queue.append(5)
    queue.append(3)
    queue.append(2)

    while sorcery_points >= 2:
        next_slot_points = queue.popleft()
        while next_slot_points > sorcery_points:
            next_slot_points = queue.popleft()

        if (sorcery_points >= 7) and (max_sorcPoints >= 7) and (next_slot_points == 7):
            mana_slots[5] += 1
            sorcery_points -= 7
        elif (sorcery_points >= 6) and (max_sorcPoints >= 6) and (next_slot_points == 6):
            mana_slots[4] += 1
            sorcery_points -= 6
        elif (sorcery_points >= 5) and (max_sorcPoints >= 5) and (next_slot_points == 5):
            mana_slots[3] += 1
            sorcery_points -= 5
        elif (sorcery_points >= 3) and (max_sorcPoints >= 3) and (next_slot_points == 3):
            mana_slots[2] += 1
            sorcery_points -= 3
        elif (sorcery_points >= 2) and (max_sorcPoints >= 2) and (next_slot_points == 2):
            mana_slots[1] += 1
            sorcery_points -= 2
        queue.append(next_slot_points)

    return mana_slots, sorcery_points


def calculate_extra_mana_slots_mixture_byPoints(sorcPoints: int, max_sorcPoints: int) -> Dict[object, int]:
    mana_slots = {"Function": "Extra Slots: Distributed", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

    while sorcPoints >= 2:
        if sorcPoints <= 1:
            break

        if GLOBS.currentNextSpellPoints == 7 and sorcPoints >= 7:
            mana_slots[5] += 1
            sorcPoints -= 7
            GLOBS.currentNextSpellPoints = GLOBS.nextSpellPointsQueue.popleft()
            GLOBS.nextSpellPointsQueue.append(GLOBS.currentNextSpellPoints)
        elif GLOBS.currentNextSpellPoints == 6 and sorcPoints >= 6:
            mana_slots[4] += 1
            sorcPoints -= 6
            GLOBS.currentNextSpellPoints = GLOBS.nextSpellPointsQueue.popleft()
            GLOBS.nextSpellPointsQueue.append(GLOBS.currentNextSpellPoints)
        elif GLOBS.currentNextSpellPoints == 5 and sorcPoints >= 5:
            mana_slots[3] += 1
            sorcPoints -= 5
            GLOBS.currentNextSpellPoints = GLOBS.nextSpellPointsQueue.popleft()
            GLOBS.nextSpellPointsQueue.append(GLOBS.currentNextSpellPoints)
        elif GLOBS.currentNextSpellPoints == 3 and sorcPoints >= 3:
            mana_slots[2] += 1
            sorcPoints -= 3
            GLOBS.currentNextSpellPoints = GLOBS.nextSpellPointsQueue.popleft()
            GLOBS.nextSpellPointsQueue.append(GLOBS.currentNextSpellPoints)
        elif GLOBS.currentNextSpellPoints == 2 and sorcPoints >= 2:
            mana_slots[1] += 1
            sorcPoints -= 2
            GLOBS.currentNextSpellPoints = GLOBS.nextSpellPointsQueue.popleft()
            GLOBS.nextSpellPointsQueue.append(GLOBS.currentNextSpellPoints)
        else:
            print("None chosen...")
            break

    return mana_slots, sorcPoints


def calculate_extra_mana_slots_simple(time_in_hours: int, sorcerer_points_per_warlock_slot, max_sorcPoints):
    warlock_spell_slots = time_in_hours * 2
    total_sorcery_points = warlock_spell_slots * sorcerer_points_per_warlock_slot
    mana_slots = {"Function": "Extra Slots: Max Individual", 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

    sorcery_points = total_sorcery_points
    while (sorcery_points >= 7) and (max_sorcPoints >= 7):
        mana_slots[5] += 1
        sorcery_points -= 7
    sorcery_points = total_sorcery_points
    while (sorcery_points >= 6) and (max_sorcPoints >= 6):
        mana_slots[4] += 1
        sorcery_points -= 6
    sorcery_points = total_sorcery_points
    while (sorcery_points >= 5) and (max_sorcPoints >= 5):
        mana_slots[3] += 1
        sorcery_points -= 5
    sorcery_points = total_sorcery_points
    while (sorcery_points >= 3) and (max_sorcPoints >= 3):
        mana_slots[2] += 1
        sorcery_points -= 3
    sorcery_points = total_sorcery_points
    while (sorcery_points >= 2) and (max_sorcPoints >= 2):
        mana_slots[1] += 1
        sorcery_points -= 2
    return mana_slots


def prettyPrint(extraSpellsDict: Dict[int, int], printMessage: str = "Extra Spell Slots Generated"):
    if printMessage != "":
        print(printMessage)
    for key, val in extraSpellsDict.items():
        print(f"\tLevel {key}: {val} slots")

def printCurrentAttributes(hour: int, current_sorcpoints: int, max_sorcPoints: int, total_sorcpoints: int, extraSpellsDict):
    print(f"Hour {hour}: \n\t{current_sorcpoints}/{max_sorcPoints}pts\t->\tTotal: {total_sorcpoints}pts")
    prettyPrint(extraSpellsDict, "")


def printSorcPointsGainedMsg(hour, sorcPoints, totalSorcPoints, sorcPointsPerWarlockLvl, warlockLevelsExpended):
    print(
        f"\t {warlockLevelsExpended} Lvl{sorcPointsPerWarlockLvl} Warlock Levels expended at hour {hour}.\n"
        f"\t\tSorc points {sorcPoints - sorcPointsPerWarlockLvl*warlockLevelsExpended}+{sorcPointsPerWarlockLvl*warlockLevelsExpended} = {sorcPoints}: {sorcPoints}.\n"
        f"\t\tTotal Sorcerer points: {totalSorcPoints}.\n"
    )

def printLevelGeneratedMsg(hour, sorcPoints, totalSorcPoints, pointsExpended):
    pointsToLevelDict = {
        7:5,
        6:4,
        5:3,
        3:2,
        2:1
    }
    print(
        f"\tLevel {pointsToLevelDict[pointsExpended]} extra_spell_slot generated at hour {hour}.\n"
        f"\t\tSorc points {sorcPoints + pointsExpended}-{pointsExpended} = {sorcPoints}: {sorcPoints}.\n"
        f"\t\tTotal Sorcerer points: {totalSorcPoints}.\n"
    )


def explainEachHour_extraSpells(starting_sorcpoints: int, time_in_hours: int, sorcerer_points_per_warlock_slot: int, max_sorcPoints: int,explainBool: bool = True) -> Dict[int, int]:
    """
    A function which will explain every hour how many extra_spells_slots are generated at each hour interval
    returns: extra_spell_slots Dict[int, int]
    """
    for i in range(len(GLOBS.nextSpellPointsQueue)):
        GLOBS.currentNextSpellPoints = GLOBS.nextSpellPointsQueue.popleft()
        if GLOBS.currentNextSpellPoints <= max_sorcPoints:
            GLOBS.nextSpellPointsQueue.append(GLOBS.currentNextSpellPoints)
    GLOBS.currentNextSpellPoints = GLOBS.nextSpellPointsQueue.popleft()
    GLOBS.nextSpellPointsQueue.append(GLOBS.currentNextSpellPoints)

    # totalSorcPoints = starting_sorcpoints
    # extra_spell_slots, sorcPoints = calculate_extra_mana_slots_mixture_byPoints(starting_sorcpoints, max_sorcPoints)
    # totalSorcPoints -= sorcPoints
    sorcPoints = starting_sorcpoints
    totalSorcPoints = starting_sorcpoints
    extra_spell_slots = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0
    }

    warlock_slots = 0
    for hour in range(0, time_in_hours + 1):
        print(f"Hour {hour}")

        warlock_slots += 2
        while warlock_slots > 0 :
            """
            # This is the logic for expending the sorc points and generating extra_spell_slots
            #   according to these rules:
            #   2 sorcery-points for a level 1 extra_spell_slot, 3 sorcery-points for a level 2 extra_spell_slot,
            #   5 sorcery-points for a level 3 extra_spell_slot, 6 sorcery-points for a level 4 extra_spell_slot,
            #   7 sorcery-points for a level 5 extra_spell_slot
            """
            while True:
                if sorcPoints <= 1:
                    break
                if GLOBS.currentNextSpellPoints == 7 and sorcPoints >= 7:
                    extra_spell_slots[5] += 1
                    sorcPoints -= 7
                    GLOBS.currentNextSpellPoints = GLOBS.nextSpellPointsQueue.popleft()
                    GLOBS.nextSpellPointsQueue.append(GLOBS.currentNextSpellPoints)
                    if explainBool:
                        printLevelGeneratedMsg(hour, sorcPoints, totalSorcPoints, 7)
                elif GLOBS.currentNextSpellPoints == 6 and sorcPoints >= 6:
                    extra_spell_slots[4] += 1
                    sorcPoints -= 6
                    GLOBS.currentNextSpellPoints = GLOBS.nextSpellPointsQueue.popleft()
                    GLOBS.nextSpellPointsQueue.append(GLOBS.currentNextSpellPoints)
                    if explainBool:
                        printLevelGeneratedMsg(hour, sorcPoints, totalSorcPoints, 6)
                elif GLOBS.currentNextSpellPoints == 5 and sorcPoints >= 5:
                    extra_spell_slots[3] += 1
                    sorcPoints -= 5
                    GLOBS.currentNextSpellPoints = GLOBS.nextSpellPointsQueue.popleft()
                    GLOBS.nextSpellPointsQueue.append(GLOBS.currentNextSpellPoints)
                    if explainBool:
                        printLevelGeneratedMsg(hour, sorcPoints, totalSorcPoints, 5)
                elif GLOBS.currentNextSpellPoints == 3 and sorcPoints >= 3:
                    extra_spell_slots[2] += 1
                    sorcPoints -= 3
                    GLOBS.currentNextSpellPoints = GLOBS.nextSpellPointsQueue.popleft()
                    GLOBS.nextSpellPointsQueue.append(GLOBS.currentNextSpellPoints)
                    if explainBool:
                        printLevelGeneratedMsg(hour, sorcPoints, totalSorcPoints, 3)
                elif GLOBS.currentNextSpellPoints == 2 and sorcPoints >= 2:
                    extra_spell_slots[1] += 1
                    sorcPoints -= 2
                    GLOBS.currentNextSpellPoints = GLOBS.nextSpellPointsQueue.popleft()
                    GLOBS.nextSpellPointsQueue.append(GLOBS.currentNextSpellPoints)
                    if explainBool:
                        printLevelGeneratedMsg(hour, sorcPoints, totalSorcPoints, 2)
                else:
                    # print("None chosen...")
                    break

            if warlock_slots == 2 and (sorcPoints + (sorcerer_points_per_warlock_slot * 2)) <= max_sorcPoints:
                sorcPoints += sorcerer_points_per_warlock_slot * 2
                totalSorcPoints += sorcerer_points_per_warlock_slot * 2
                warlock_slots -= 2
                if explainBool:
                    printSorcPointsGainedMsg(hour, sorcPoints, totalSorcPoints, sorcerer_points_per_warlock_slot, 2)
            elif warlock_slots >= 1 and (sorcPoints + sorcerer_points_per_warlock_slot) <= max_sorcPoints:
                sorcPoints += sorcerer_points_per_warlock_slot
                totalSorcPoints += sorcerer_points_per_warlock_slot
                warlock_slots -= 1
                if explainBool:
                    printSorcPointsGainedMsg(hour, sorcPoints, totalSorcPoints, sorcerer_points_per_warlock_slot, 1)
            elif warlock_slots >= 1:
                # sorcPoints += sorcerer_points_per_warlock_slot
                # while not (sorcPoints + sorcerer_points_per_warlock_slot) <= max_sorcPoints:
                #     break

                sorcPoints = max_sorcPoints
                totalSorcPoints += sorcerer_points_per_warlock_slot
                warlock_slots -= 1
                if explainBool:
                    printSorcPointsGainedMsg(hour, sorcPoints, totalSorcPoints, sorcerer_points_per_warlock_slot, 1)

        if explainBool and False:
            printCurrentAttributes(hour, sorcPoints, max_sorcPoints, totalSorcPoints, extra_spell_slots)

    print(f"Total: {totalSorcPoints + sorcPoints}")

    return extra_spell_slots


if __name__ == '__main__':
    result = explainEachHour_extraSpells(config.__startingSorcPoints, config.__timeInHours, config.__sorcPointsPerWarlockSlot, config.__maxSorcPoints)
    print(f"{result}")
    prettyPrint(result)

