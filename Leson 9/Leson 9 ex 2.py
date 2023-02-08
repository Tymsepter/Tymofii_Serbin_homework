import sys

# print the current sys.path list
print("Original sys.path:", sys.path)

# add a new directory to sys.path
sys.path.append("/New_directory")

# print the updated sys.path list
print("Updated sys.path:", sys.path)