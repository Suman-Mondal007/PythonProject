# import numpy as np
# zeros_arr = np.zeros((2, 3))
# ones_arr = np.ones((2, 3))
# const_arr = np.full((2, 3), 5)
#
# print("Zeros Array:\n", zeros_arr)
# print("Ones Array:\n", ones_arr)
# print("Constant Array:\n", const_arr)
#
#
# even_numbers = np.arange(10, 51, 2)
# print("Even numbers:", even_numbers)


import numpy as np

# np.random.seed(42)  # for reproducibility (optional)
# arr = np.random.randint(10, 101, size=(4, 5))
# print("Random 2D Array:\n", arr)

# Create 3x3 array with random values between 0 and 10
# random_arr = np.random.randint(0, 10, (3, 3))
# print("\nRandom 3x3 Array:\n", random_arr)
#
# # Extract first two rows and first two columns
# sub_array = random_arr[:2, :2]
#
# print("\nFirst two rows & columns:\n", sub_array)
#
# # Extract last row
# last_row = random_arr[-1, :]
# print("Last row:", last_row)



# arr = np.array([5, 2, 9, 1, 7])
#
# sorted_asc = np.sort(arr)[::-1]
# print("\nSorted Array (Ascending):", sorted_asc)


# import numpy as np
#
# # 1D array
# arr1 = np.array([1, 2, 3, 4, 5])
#
# # 2D array
# arr2 = np.array([[1, 2, 3],
#                  [4, 5, 6]])
#
# # 3D array
# arr3 = np.array([[[1, 2], [3, 4]],
#                  [[5, 6], [7, 8]]])
#
# # Display properties
# print("1D Array:", arr1)
# print("Shape:", arr1.shape, "Size:", arr1.size, "Dimensions:", arr1.ndim)
#
# print("\n2D Array:\n", arr2)
# print("Shape:", arr2.shape, "Size:", arr2.size, "Dimensions:", arr2.ndim)
#
# print("\n3D Array:\n", arr3)
# print("Shape:", arr3.shape, "Size:", arr3.size, "Dimensions:", arr3.ndim)
class Employee:
    def __init__(self, name, basic_salary, hra, da):
        self.name = name
        self.basic_salary = basic_salary
        self.hra = hra
        self.da = da
    def gross_salary(self):
        return self.basic_salary + self.hra + self.da
emp1 = Employee("Suman", basic_salary=30000, hra=5000, da=2000)
print(f"Employee Name: {emp1.name}")
print(f"Gross Salary: {emp1.gross_salary()}")
