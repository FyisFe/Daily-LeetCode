class TravelTime:
    def __init__(self):
        self.totalTime = 0
        self.count = 0


class Travel:
    def __init__(self, stationName, ts):
        self.stationName = stationName
        self.ts = ts


class UndergroundSystem:
    def __init__(self):
        self.travelTimes = {}
        self.travels = {}

    def getKey(self, startStation, endStation):
        return startStation + "_" + endStation

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.travels[id] = Travel(stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:

        travel = self.travels[id]
        key = self.getKey(travel.stationName, stationName)
        if key not in self.travelTimes:
            travelTime = self.travelTimes[key] = TravelTime()
        else:
            travelTime = self.travelTimes[key]

        travelTime.totalTime += t - travel.ts
        travelTime.count += 1

        self.travels.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travelTime = self.travelTimes[self.getKey(startStation, endStation)]
        return travelTime.totalTime / travelTime.count
