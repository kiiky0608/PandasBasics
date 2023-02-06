# 파일 명 : dataframe 생성.py
# 설명 : dataframe 사용법  익히기 
#       - Dataframe 란? 2차원 표에서 컬럼 단위로 데이터를 표현
#       - import 방식
#           from pandas import DataFrame
# 최초 작성일 : 2023년 2월 6일
# 최초 작성작 : 김호성
# 변경 이력
#   - 없음 

# ================
# import 부분 start
from pandas import DataFrame
# import 부분 end
# ================

# ================
# 함수정의 부분 start

# 함수 이름 : Exercise_1
# 최초 작성일 : 2023년 2월 6일
# 최초 작성자 : 김호성
# 내용 : 연습문제 1
#       - 2차원 데이터를 데이터 프레임으로 표현         
# 입력 : 없음
# 출력 : 없음
# 기타 :
# 변경 이력
#   - 없음
def Exercise_1():
    print("연습문제 1")
    data = [
        [980, 990, 920, 930],
        [200, 300, 180, 180],
        [300, 500, 300, 400]
    ]
    index = ['비트코인', '리플', '이더리움']
    columns = ['시가', '고가', '저가', '종가']

    df = DataFrame(data=data, index=index, columns=columns)
    
    print(df)
# 함수정의 부분 end
# ================

# ================
# 프로그램 실행 부분 start

# DataFrame 생성 1/3
# 2차원 표에서 컬럼 단위로 데이터를 표현
#   - 컬럼명을 딕셔너리의  key로 데이터는 딕셔너리의 values로 사용
#  index  |           컬럼
#         |  종가    |   PER   |   PBR            ⬅︎ 컬럼 명 : 딕셔러니의 키
# --------------------------------------
#  NAVER   157000  |  39.88  |  4.38            
# --------------------------------------
#  삼성전자   51300  |   8.52  |  1.45            
# --------------------------------------        ⬅︎ 데이터
#  LG전자    68800  |  10.03  |  0.87              
# --------------------------------------
#  카카오    140000  | 228.38  |  2.16             
# --------------------------------------
print("DataFrame 표현 방법 1")
data = {
    '종가' : [157000, 51300, 68800, 140000],
    'PER' : [39.38, 8.52, 10.03, 228.38],
    'PBR' : [4.38, 1.45, 0.87, 2.26]
}

index = ['NAVER', '삼성전자', 'LG전자', '카카오']

df = DataFrame(data=data, index=index)

print(df)
print('')
# DataFrame 생성 2/3
#   - 2차원 표에서 로우 단위로 데이터를 리스트로 표현
#       . data, index, columns를 각각 리스트로 표현
print("DataFrame 표현 방법 2")
data = [
    [157000, 39.38, 4.38],
    [51300, 8.52, 1.45],
    [68800, 10.03, 0.87],
    [140000, 228.38, 2.26]
]

index = ['NAVER', '삼성전자', 'LG전자', '카카오']
columns = ['종가', 'PER', 'PBR']

df = DataFrame(data=data, index=index, columns=columns)

print(df)
print('')
# DataFrame 생성 3/3
# 2차원 표에서 로우 단위로 데이터를 딕셔너리로 표현
print("DataFrame 표현 방법 3")
data = [
    {'종가':157000, 'PER':39.38, 'PBR':4.38},
    {'종가':51300, 'PER':8.52, 'PBR':1.45},
    {'종가':68000, 'PER':10.03, 'PBR':0.87},
    {'종가':140000, 'PER':228.38, 'PBR':2.26}
]

index = ['NAVER', '삼성전자', 'LG전자', '카카오']

df = DataFrame(data=data, index=index)

print(df)
print('')

# 연습문제 1
Exercise_1()
# 프로그램 실행 부분 end
# ================
