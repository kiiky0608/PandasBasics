# 파일 명 : dataframe 추가 삭제.py
# 설명 : dataframe 추가, 삭제 익히기 
# 최초 작성일 : 2023년 2월 11일
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

# 컬럼 추가
#   - df['컬럼명'] = 시리즈 개체
#   - 비트코인 일봉 데이터를 얻어온 후 각 거래일의 변동(range) 컬럼 추가하기
#       . range = high - low
df = pyupbit.get_ohlcv(ticker = "KRW-BTC")

print("데이터의 앞에 부분만 간단히 보고 싶을 때 head 함수 사용")
print(df.head())    # 데이터의 앞에 부분만 간단히 보고 싶을 때 head 함수 사용
print("데이터의 뒤에 부분만 간단히 보고 싶을 때 tail 함수 사용")
print(df.tail())    # 데이터의 뒤에 부분만 간단히 보고 싶을 때 tail 함수 사용
print("")

print("고가와 저가의 값을 뺀 diff 컬럼 추가")
df['diff'] = df['high'] - df['low']
print(df)
print("")

# 컬럼 삭제
#   - df.drop('컬럼명', axis=1)
#       . 원본은 그대로 유지되고 컬럼이 삭제된 새로운 데이터프레임 객체가 리턴됨
#       . axis = 1 이면 열 삭제, axis = 0 이면 행 삭제
print("diff 값 삭제")
df2 = df.drop('diff', axis = 1)
print(df2)

# 시계열 데이터와 인덱스
#   - 시계열 데이터는 인덱스가 날짜와 시간으로 구성됨
#       . 문자열로 표현된 날짜와 시간을 DatetimeIndex 타입으로 변환해서 새용해야 함
print("시계열 데이터와 인덱스")
date = "2023-2-11"
print(type(date))
index = pd.to_datetime(date)
print(type(index))
print(index)
df2.loc[index] = [100, 100, 100, 100, 100, 100]
print(df2)
print("2023년 2월 데이터만 가져오기")
print(df2.loc['2023-02'])       # 시계열 데이터의 경우 loc를 빼고 해도 된다.
print("2023년 2월 데이터만 마지막 데이터만 가져오기")
df2023_02 = df2.loc['2023-02']
s = df2023_02.iloc[-1]
print(s)       # 시계열 데이터의 경우 loc를 빼고 해도 된다.
print("open : ", s['open'])

# 로우 삭제
#   - df.drop(로우 인덱스, axis = 0)
#       . 원본은 그대로 유지되고 row가 삭제된 데이터프레임 객체가 리턴됨
print("마지막 행 삭제")
index = df2.index[-1]
df3 = df2.drop(index, axis=0)   # axis = 0을 주면 행을 삭제
print(df3)


# 프로그램 실행 부분 end
# ================