import random
import penslonLotteryCrol

# 연금복권 번호 뽑기
# 조 1~5 까지 존재
# 번호는 1 ~ 10(0) 번까지 존재
# 조는 어차피 1~5조 모두 구매하기때문에 구할 필요가 없다.
# 번호는 가중치를 이용해서 뽑히지 않는 번호가 좀 더 잘 뽑히도록 한다.

# 번호생성기
# numbers : 가용 번호 범위
# weights_list : 가중치 배열
# num : 뽑고자 하는 번호 갯수
def choiceNumber(numbers, weights_list, num):
    random.seed()
    return random.choices(numbers, weights=weights_list, k=num)

# 가중치 계산기
# 넘어온 가중치를 계산해서 많은 가중치를 가진것이 적게 뽑히도록 가중치를 조절한다.
# weights_list : 가중치 배열
def calcWeights(weights_list):
    rtns = []
    for n in weights_list:
        if n != 0:
            n = -n + 100 * 0.8
        else:
            n = n + 100
        rtns.append(n)
    return rtns


numbers = list(range(0, 10))

# 가중치 적용(0번부터 당첨횟수를 적어준다.)
print("추출 리스트(가중치 적용) - 십만단위: ", sorted(choiceNumber(numbers, calcWeights(penslonLotteryCrol.getWinningNumberReturnArr(1)), 1)))
# 가중치 적용(0번부터 당첨횟수를 적어준다.)
print("추출 리스트(가중치 적용) - 만단위: ", sorted(choiceNumber(numbers, calcWeights(penslonLotteryCrol.getWinningNumberReturnArr(2)), 1)))
# 가중치 적용(0번부터 당첨횟수를 적어준다.)
print("추출 리스트(가중치 적용) - 천단위: ", sorted(choiceNumber(numbers, calcWeights(penslonLotteryCrol.getWinningNumberReturnArr(3)), 1)))
# 가중치 적용(0번부터 당첨횟수를 적어준다.)
print("추출 리스트(가중치 적용) - 백단위: ", sorted(choiceNumber(numbers, calcWeights(penslonLotteryCrol.getWinningNumberReturnArr(4)), 1)))
# 가중치 적용(0번부터 당첨횟수를 적어준다.)
print("추출 리스트(가중치 적용) - 십단위: ", sorted(choiceNumber(numbers, calcWeights(penslonLotteryCrol.getWinningNumberReturnArr(5)), 1)))
# 가중치 적용(0번부터 당첨횟수를 적어준다.)
print("추출 리스트(가중치 적용) - 일단위: ", sorted(choiceNumber(numbers, calcWeights(penslonLotteryCrol.getWinningNumberReturnArr(6)), 1)))