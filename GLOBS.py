from collections import deque

import config

currentNextSpellPoints = None
nextSpellPointsQueue = deque()

toggleInsertHighSpells = config.__toggle_insert_level5_spells
lowToHighFlag = False
if lowToHighFlag:
    nextSpellPointsQueue.append(2)
    if toggleInsertHighSpells:
        nextSpellPointsQueue.append(7)
    nextSpellPointsQueue.append(3)
    if toggleInsertHighSpells:
        nextSpellPointsQueue.append(7)
    nextSpellPointsQueue.append(5)
    if toggleInsertHighSpells:
        nextSpellPointsQueue.append(7)
    nextSpellPointsQueue.append(6)
    nextSpellPointsQueue.append(7)

else:
    nextSpellPointsQueue.append(7)
    nextSpellPointsQueue.append(6)
    if toggleInsertHighSpells:
        nextSpellPointsQueue.append(7)
    nextSpellPointsQueue.append(5)
    if toggleInsertHighSpells:
        nextSpellPointsQueue.append(7)
    nextSpellPointsQueue.append(3)
    if toggleInsertHighSpells:
        nextSpellPointsQueue.append(7)
    nextSpellPointsQueue.append(2)





#################################################################################333
