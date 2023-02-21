import GLOBS

#################################################################################################
# Required
__sorcerer_level = 9
__warlock_level = 3
__days_without_sleep = 14
__hours_per_day_QRing = 10

__toggle_insert_level5_spells = False
#################################################################################################


#################################################################################################
sorceryLevel_toPoints_dict = {
    1: 0,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    11: 11,
    12: 12,
    13: 13,
    14: 14,
    15: 15,
    16: 16,
    17: 17,
    18: 18,
    19: 19,
    20: 20
}

warlockLevel_toSlotLevel_dict = {
    1: 1,
    2: 1,
    3: 2,
    4: 2,
    5: 3,
    6: 3,
    7: 4,
    8: 4,
    9: 5,
    10: 5,
    11: 5,
    12: 5,
    13: 5,
    14: 5,
    15: 5,
    16: 5,
    17: 5,
    18: 5,
    19: 5,
    20: 5
}
#################################################################################################
__maxSorcPoints = sorceryLevel_toPoints_dict[__sorcerer_level]
__startingSorcPoints = __maxSorcPoints
__sorcPointsPerWarlockSlot = warlockLevel_toSlotLevel_dict[__warlock_level]
__timeInHours = __days_without_sleep * __hours_per_day_QRing
#################################################################################################