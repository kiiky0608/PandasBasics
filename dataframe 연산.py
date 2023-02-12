# 파일 명 : dataframe 연산.py
# 설명 : dataframe 연산 익히기 
#       - 데이터프레임의 브로드캐스팅, 필터링 사용법 익히기
# 최초 작성일 : 2023년 2월 12일
# 최초 작성작 : 김호성
# 변경 이력
#   - 없음 

# ================
# import 부분 start
from pandas import DataFrame
import pandas as pd
import pyupbit
# import 부분 end
# ================

# ================
# 함수정의 부분 start

# 함수정의 부분 end
# ================

# ================
# 프로그램 실행 부분 start

# 브로드케스팅프
#   - 하나의 연산이 한 클럼의 모든 데이터에 적용됨
print("브로드캐스팅 예제")
df = pyupbit.get_ohlcv(ticker="KRW-BTC")
print(df['open'])
df['open']+100
print(df['open'])           # 100을 더하더라도 원본 값에는 영향을 주지 않는 것을 확인 할수 있다
print(df['open'] + 100)     # 100을 더한 값을 사용하기 위해서는 새로운 변수에 값을 할당 필요
print("")

# 데이터프레임 필터링
#   - 비교 연산자의 결과는 Boolean 값을 갖고있는 시리즈 객체임
#       . 예) 종가가 고가 보다 높았던 거래일만 필터링 해보기
print("데이터 필터링")
cond = df['close'] > df['open']
print(cond)
print("종가가 시작가 보다 높은 날")
print(df[cond])
print("데이터 행과 열 수")
print(df[cond].shape)
print(type(df[cond].shape))
print("")

# 컬럼 시프트
#   - 데이터프레임의 연산은 기본적으로 같은 인덱스에 있는 컬럼과 컬럼 사이에 적용됨
#       . df['high'] - df['low'] 기본적으로는 하나의 행을 기준으로 연산이 된다.
#       . 당일 저가와 전일 저가를 빼려면 어떻게 해야하는가?
#   - df['컬럼명].shift(1)
#       . 특정 컬럼의 데이터를 아래로 하나씩 이동
#       . df['close_shift1'] = df['close'].shift(1)
print("컬럼시프트")
df['close_shift1'] = df['close'].shift(1)
print(df)
close_diff1 = df['close'] - df['close_shift1']
print("당일 종가와 전일 종가 차이 :")
print(close_diff1)


# 프로그램 실행 부분 end
# ================