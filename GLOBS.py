from collections import deque

currentNextSpellPoints = None
nextSpellPointsQueue = deque()

lowToHighFlag = True
toggleInsertHighSpells = False
if lowToHighFlag:
    nextSpellPointsQueue.append(2)
    if toggleInsertHighSpells:
        nextSpellPointsQueue.append(7)
    nextSpellPointsQueue.append(3)
    if toggleInsertHighSpells:
        nextSpellPointsQueue.append(7)
    nextSpellPointsQueue.append(5)
    nextSpellPointsQueue.append(6)
    nextSpellPointsQueue.append(7)

else:
    nextSpellPointsQueue.append(7)
    nextSpellPointsQueue.append(6)
    nextSpellPointsQueue.append(5)
    if toggleInsertHighSpells:
        nextSpellPointsQueue.append(7)
    nextSpellPointsQueue.append(3)
    if toggleInsertHighSpells:
        nextSpellPointsQueue.append(7)
    nextSpellPointsQueue.append(2)
