class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary, max_salary = salary[0], salary[0]
        count = -2
        all_s = 0
        for s in salary:
            if s < min_salary:
                min_salary = s
            if s > max_salary:
                max_salary = s
            all_s += s
            count += 1

        return (all_s - min_salary - max_salary) / count
