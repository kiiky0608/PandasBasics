# 파일 명 : series 연산.py
# 설명 : series 연산 사용법 익히기 
#       -      
# 최초 작성일 : 2023년 2월 6일
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

# 함수정의 부분 end
# ================

# 함수 이름 : Exercise_1
# 최조 작성일 : 2023년 2월 6일
# 최초 작성자 : 김호성
# 내용 : series 연산 연습문제 1
#           - 고가와 저가 차이가 100 이상인 날의 고가를 출력하세요.
# 입력 : 없음
# 출력 : 없음
# 기타 : 없음
# 변경 이력
#   -
def Exercise_1():
    print("연습문제 1")
    print("고가와 저가 차이가 100 이상인 날의 고가를 출력하세요.")
    저가 = Series([10, 200, 200, 400, 600])
    고가 = Series([100, 300, 400, 500, 600])
    diff = 고가 - 저가
    cond = diff >= 100
    print(고가[cond])

# 함수 이름 : Exercise_2
# 최조 작성일 : 2023년 2월 6일
# 최초 작성자 : 김호성
# 내용 : series 연산 연습문제 2
#           - 종가가 80000원 이상 90000원 미만인 날짜를 출력하세요
# 입력 : 없음
# 출력 : 없음
# 기타 : 없음
# 변경 이력
#   -
def Exercise_2():
    print("연습문제 1")
    print("종가가 80000원 이상 90000원 미만인 날짜를 출력하세요")
    data = [93000, 82400, 99100, 81000, 72300]
    index = ['05/14', '05/15', '05/16', '05/17', '05/18']
    종가 = Series(data=data, index=index)
    cond = (종가 >= 80000) & (종가 < 90000)
    s1 = 종가[cond]
    print(s1.index)
     
# ================
# 프로그램 실행 부분 start

# 브로드캐시팅(Broadcasting)
#   - 연산이 시리즈 객체의 전체 값에 적용됨
#       . 반복문을 사용하지 않음
print("연산 : s + 10 ")
s = Series([100, 200, 300])
print(s + 10)

print("연산 : high - low")
high = Series(data=[1000, 2000, 3000], index=['5/1', '5/2', '5/3'])
low = Series(data=[100, 200, 300], index=['5/1', '5/2', '5/3'])
diff = high - low
print(diff)

print("연산 : hihg - low, index가 다른 경우")
high = Series(data=[1000, 2000, 3000], index=['5/1', '5/2', '5/3'])
low = Series(data=[100, 200, 300], index=['5/1', '5/2', '5/4'])         # 안댁스가 없는 경우 연산이 수행되지 않는다.
diff = high - low
print(diff)

# 시리즈 비교 연산
#   - 비교 연산자의 결과로 Boolean 타입이 지정된 시리즈가 리턴 됨
print("시리즈 비교 연산 : s > 300")
s = Series(data=[100, 200, 300, 400, 500])
cond = s > 300
print(cond)

# 시리즈 필터링 1/2
#   - True/False 값을 통해서 True 값만 필터링 가능
#   - 시리즈 필터링을 활용하면 True로 활성화된 index 3, 4 획득 가능
#           s                          cond
#   index   |   value           index   |   value 
#     0     |    100              0     |   False
#     1     |    200              1     |   False
#     2     |    300              2     |   False
#     3     |    400              3     |   True
#     4     |    500              4     |   True
print("시리즈 필터링 : cond 리스트의 true 값만 시리즈 s개체 필터링")
s = Series(data=[100, 200, 300, 400, 500])
cond = [False, False, False, True, True]
print(s[cond])

# 시리즈 필터링 2/2
#   - 비교 연산자와 결과 시리즈를 사용하여 인덱싱하면 조건을 만족하는 데이터만 필터링 가능
print("조건을 활용하여 필터링 : 300 초과 값만 출력")
s = Series(data=[100, 200, 300, 400, 500])
cond = s > 300
print(s[cond])

# 연습문제 1
Exercise_1()

# 연습문제 2
Exercise_2()

# 프로그램 실행 부분 end
# ================