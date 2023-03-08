class Mathematician:
    def square_nums(self, nums):
        return [num ** 2 for num in nums]

    def remove_positives(self, nums):
        return [num for num in nums if num <= 0]

    def filter_leaps(self, years):
        return [year for year in years if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)]
