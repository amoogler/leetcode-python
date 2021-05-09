class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        year_population = collections.defaultdict(int)
        earliest_year = float(inf)

        for birth, death in logs:
            for i in range(birth, death):
                year_population[i] += 1

        max_population = max(year_population.values())

        for year in year_population.keys():
            if year_population[year] == max_population:
                earliest_year = min(earliest_year, year)

        return earliest_year
