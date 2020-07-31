import random

# 랜덤한 로또 숫자 뽑기
# 번호는 1에서 45까지 존재

numbers = list(range(1,46))
#print("원본 리스트: \n", numbers, "\n")

# 가중치 미적용
numbers_even = random.sample(numbers, 6)
print("추출 리스트: ", sorted(numbers_even))

# 가중치 적용
#weights_list = [1]*9 + [2]*9 + [3]*9 + [4]*9 + [5]*9
#print("가중치 배열: \n", weights_list, "\n")
#numbers_weighted = random.choices(numbers, weights=weights_list, k=6)
#print("추출 리스트(가중치 적용): ", sorted(numbers_weighted))