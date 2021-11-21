class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        step = 0
        water = capacity

        for i, plant in enumerate(plants):
            if water < plant:
                step += i * 2
                water = capacity

            step += 1
            water -= plant

        return step
