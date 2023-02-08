# Compute the total price of the stock.
# Where the total price is the sum of the price of an item
# multiplied by the quantity of this exact item


stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

print(stock)
tpftp_b = stock["banana"] * prices["banana"]
print(f"banana X", stock["banana"], " = " f"{tpftp_b}")
tpftp_a = stock["apple"] * prices["apple"]
print(f"apple X", stock["apple"], " = " f"{tpftp_a}")
tpftp_o = stock["orange"] * prices["orange"]
print(f"orange X", stock["orange"], " = " f"{tpftp_o}")
tpftp_p = stock["pear"] * prices["pear"]
print(f"pear X", stock["pear"], " = " f"{tpftp_p}")
total_price = tpftp_b + tpftp_a + tpftp_o + tpftp_p
print(f"total price - {total_price}")
