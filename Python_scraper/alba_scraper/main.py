import os
from scrap_brands import get_brand_infos, scrap_brands

os.system("clear")

brand_infos = get_brand_infos()
scrap_brands(brand_infos)
