product = {'name': '컴퓨터', 'price': 1200000}

product["재고"] = 100

product["price"] = 1150000

print("수정된 딕셔너리 내용:")
for key, value in product.items():
    print(f"  {key}: {value}")   

  #f-string을 쓰는 습관을 조금 더 들일 것
