from mathematician import Mathematician

math = Mathematician()

nums = [1, 2, 3, 4, 5]
squares = math.square_nums(nums)
print(squares)

nums = [1, -2, 3, -4, 5]
negatives = math.remove_positives(nums)
print(negatives)

years = [2000, 2001, 2004, 2005, 2008, 2010]
leap_years = math.filter_leaps(years)
print(leap_years)
