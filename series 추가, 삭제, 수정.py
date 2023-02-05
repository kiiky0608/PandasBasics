# 파일 명 : series 추가, 삭제, 수정.py
# 설명 : series 추가, 삭제, 수정 사용법 익히기 
#       -    
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

# 함수정의 부분 end
# ================

# ================
# 프로그램 실행 부분 start

data = [100,  200, 300]
index = ["월", "화", "수"]

s = Series(data=data, index=index)

# Series에 값 추가
#   - 딕셔러니와 유사한 방식으로 값 추가 가능
#       . s.loc[인덱스] = 값
print("인덱스 목요일에 400 값 추가")
s.loc["목"] = 400
print(s)

# Series 삭제   
#   - drop 메서드
#       . 원본은 유지하고 값이 삭제된 시리즈 객체를 리턴
#       . s.drop('인덱스')
#       . s.drop(['인덱스1', '인덱스2'])
print("원본은 유지하고 값이 삭제된 시리즈 객체를 리턴")
s1 = s.drop('월')   # 원본은 유지되고 월요일 데이터가 없어진 새로운 시리즈 개체가 s1에 리턴
print("s1 출력")
print(s1)

print("s 데이터 목요일 값을 삭제")
s.drop('목', inplace=True)  # 원본 데이터를 없애고 싶을 때는 inplace=true를 설정
print(s)

# Series 수정
#   - Series의 행번호 또는 인덱스를 사용하여 value를 수정
print("iloc를 활용하여 첫번째 행렬 값을 1000으로 수정")
s.iloc[0] = 1000
print(s)
print("loc를 활용하여 수요일 인덱스 행 값을 3000으로 수정")
s.loc['수'] = 3000
print(s)

# 프로그램 실행 부분 end
# ================