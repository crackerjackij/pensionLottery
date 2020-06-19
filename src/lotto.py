import random

numbers = list(range(1,46))
print("원본 리스트: \n", numbers, "\n")

weights_list = [1]*9 + [2]*9 + [3]*9 + [4]*9 + [5]*9
print("가중치 배열: \n", weights_list, "\n")

# 가중치 미적용
numbers_even = random.sample(numbers, 6)
print("추출 리스트(가중치 없음): ", sorted(numbers_even))

# 가중치 적용
numbers_weighted = random.choices(numbers, weights=weights_list, k=6)
print("추출 리스트(가중치 적용): ", sorted(numbers_weighted))