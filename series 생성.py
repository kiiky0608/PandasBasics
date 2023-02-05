# 파일 명 : series 생성.py
# 설명 : series 사용법  익히기 
#       - series 란? numpy를 기반으로 만들어진 1차원 데이터를 위한 구조
#       - 임포트 방식
#           1번 방식 : from pandas import Series
#                       Series()
#                       DataFrame()
#           2번 방식 : import pandas as pd
#                       pd.Series()
#                       pd.DataFrame()     
# 최초 작성일 : 2023년 2월 5일
# 최초 작성작 : 김호성
# 변경 이력
#   - 없음 

# ================
# import 부분 start
from pandas import Series
# import 부분 end
# ================


# ================
# 함수정의 부분 start

# 함수 이름 : SeriesBasics
# 최초 작성일 : 2023년 2월 5일
# 최초 작성자 : 김호성
# 내용 : Series 기초 익히기
# 입력 : 없음
# 출력 : 없음
# 기타 :
# 변경 이력
#   - 없음
def SeriesBasics():
    data = [100, 200, 300]
    index = ["BTC", "XRP", "ETH"]

    s = Series(data=data, index=index)     # Series 클래스의 생성자가 호출되어어 s라는 개체가 생성

    print(type(s))
    print("인덱스 ""데이터")
    print(s)
    print("여기에 보이지는 않지만 행번호 0, 1, 2가 존재한다.")

    print("index 출력")
    print(s.index)
    print(type(s.index))
    print("pandas에서 object 타입은 문자열을 의마한다.")

    print("value 출력")
    print(s.values)
    print(type(s.values))

    print("인덱스 수행")
    print(s.index[1])
    print(s.values[1])

# 함수 이름 : Exercise_1
# 최초 작성일 : 2023년 2월 5일
# 최초 작성자 : 김호성
# 내용 : 연습문제 1
#       - 판다스 시리즈 객체 생성         
# 입력 : 없음
# 출력 : 없음
# 기타 :
# 변경 이력
#   - 없음
def Exercise_1():
    index = ["메로나", "누가바", "빠삐코"]
    data = [500, 800, 200]
    e1 = Series(data=data, index=index)

    print(type(e1))
    print(e1)
# 함수정의 부분 end
# ================

# ================
# 프로그램 실행 부분 start

# SeriesBasics()
Exercise_1()

# 프로그램 실행 부분 end
# ================