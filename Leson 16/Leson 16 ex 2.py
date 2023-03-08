from mathematician import Mathematician

math = Mathematician()

nums = [1, 2, 3, 4, 5]
squares = math.square_nums(nums)
print(squares)  # [1, 4, 9, 16, 25]

nums = [1, -2, 3, -4, 5]
negatives = math.remove_positives(nums)
print(negatives)  # [-2, -4]

years = [2000, 2001, 2004, 2005, 2008, 2010]
leap_years = math.filter_leaps(years)
print(leap_years)  # [2000, 2004, 2008]
