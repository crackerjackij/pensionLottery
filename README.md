# pensionLottery
python 3.7

``` 
pip install requests
pip install bs4

python src/penslonLottery.py 
```

연금복권 번호 추출
 - 가중치 설정 가능(많이 뽑힌 번호는 확률이 낮게 추출. 아예 추출 안되는건 아님)
 - ~~매번 당첨일별로 가중치를 등록해줘야한다. 동행복권 사이트에서 당첨통계를 활용해서 넣어주면 된다.~~
 - 실행 시 동행복권 사이트에서 당첨번호를 추출해서 가중치를 부여해준다.(아래 주소가 변경되면 소스에서 변경해준다.)
   - https://www.dhlottery.co.kr/gameResult.do?method=index720
 
우리 모두 부자 됩시다.
