class Solution:
    def minRefuelStops(
        self, target: int, startFuel: int, stations: List[List[int]]
    ) -> int:
        stops = 0
        heapq.heapify(stations)

        fuel_heap = []

        distance = startFuel
        while True:
            if distance >= target:
                return stops
            while stations and distance >= stations[0][0]:
                heappush(fuel_heap, -heappop(stations)[1])
            if not fuel_heap:
                return -1
            distance -= heappop(fuel_heap)
            stops += 1
