# 파일 명 : dataframe 인덱싱, 슬라이싱.py
# 설명 : dataframe 인덱싱, 슬라이싱 익히기 
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

# 함수정의 부분 end
# ================

# ================
# 프로그램 실행 부분 start

# 데이터 프레임
#   - 2차원 데이터를 효과적으로 표현한 판다스 자료구조
#   - 데이터 프레임 생성시 행번호와 열번호도 생성
data = [
    [157000, 39.38, 4.38],
    [51300, 8.52, 1.45],
    [68800, 10.03, 0.87],
    [140000, 228.38, 2.26]
]

index = ['NAVER', '삼성전자', 'LG전자', '카카오']
columns = ['종가', 'PER', 'PBR']

df = DataFrame(data=data, index=index, columns=columns)

# 컬럼 선택
#   - 대괄호['컬럼명']을 통해서 단일 컬럼 선택 가능
#       . df['종가']       
#       . 컬럼을 표현하는 시리즈 타입의 객체
#           -> index는 회사 이름
#           -> value는 종가
print("컬럼 선택")
s1 = df['종가']          # 여기서 s는 시리즈 타입이 된다.
print(s1)               # 데이터 프레임은 같은 인덱스를 가지는 여러 시리즈가 모여 있는 형태 
print(type(s1))
print("")

# 멀티 걸럼 선택
#   - 컬럼을 리스트로 구성한 후 인덱싱 기호에 리스트로 전달
#       . df[['컬럼명1', '컬럼명2']]
print("멀티 컬럼 선택")
s2 = df[['종가', 'PER']]
print(s2)
print(type(s2))
print("")

# 데이터프레임에서 로우(row)를 선택할 때는 iloc나 loc 속성을 사용
#   - loc : 인덱스를 사용해서 로우를 선텍
#   - iloc : 행번호를 사용해서 로우를 선택
#   - 왜 2가지 접근 방법이 존재하는가? 상황에 따라 편리한 부분이 다르기 때문에 존재
print("인덱스를 사용해서 로우를 선텍")
print(df.loc['삼성전자'])               # df.loc['삼성전자']는 series 타입, 여기서 인덱스는 종가, PER, PBR 이다
print(type(df.loc['삼성전자']))

print("행번호를 사용해서 로우를 선택")
print(df.iloc[1])                     # # df.iloc[1]는 series 타입, 여기서 인덱스는 종가, PER, PBR 이다
print(type(df.iloc[1]))
print("")
# 멀티 로우 선택
#   - 리스트로 행번호 또는 인덱스를 표현하고 이를 iloc나 loc 속성을 사요
#       . df.iloc[[0, 1]]
#       . df.loc[['인덱스1', '인덱스2']]
print("멀티 로우 선택 - 행번호(iloc)")
print(df.iloc[[0, 1]])
print("멀티 로우 선택 - 인덱스(loc)")
print(df.loc[['NAVER', '삼성전자']])
print("")
# 로우 슬라이싱
#   - iloc, loc 속성을 사용하여 슬라이싱
#       . df.iloc[0:2]
#       . df.loc['인덱스1':'인덱스2']
print("로우 슬라이싱 - 행번호(iloc)")
print(df.iloc[0:2])
print("로우 슬라이싱 - 인덱스(loc)")
print(df.loc['NAVER':'삼성전자'])

# 프로그램 실행 부분 end
# ================