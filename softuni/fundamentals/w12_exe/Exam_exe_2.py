#https://judge.softuni.org/Contests/Practice/Index/2303#1
import re

def barcode_validator(barcode):
    regex = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"

    for current in barcode:
        result = re.fullmatch(regex, current)

        if result:
            product_group = "".join(re.findall(r"\d", current))
            product_group = product_group if product_group else "00"
            print(f"Product group: {product_group}")
        else:
            print("Invalid barcode")

barcodes = []
num = int(input())
for i in range(num):
    cmd = input()
    barcodes.append(cmd)

barcode_validator(barcodes)



