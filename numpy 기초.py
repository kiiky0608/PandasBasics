# 파일 명 : numpy 기초.py
# 설명 : numpy 기본 사용법 익히는 예제
# 최초 작성일 : 2023년 2월 5일
# 최초 작성작 : 김호성
# 변경 이력
#   - 없음 

# ================
# import 부분 start
import numpy as np  # import numpy를 np라는 이름으로 가져온다.
# import 부분 end
# ================

# ================
# 함수정의 부분 start

# 함수 이름 : NummpyTestNone
# 최초 작성일 : 2023년 2월 5일
# 최초 작성자 : 김호성
# 내용 : Nummpy를 사용하지 않고 기존 파이썬 문법으로 동작
#       data 리스트의 값을 10 곱하기
# 입력 : 없음
# 출력 : 없음
# 기타 :
# 변경 이력
#   - 없음
def NummpyTestNone():
    print("="*30)
    print("Numpy를 사용하지 않고 기존 파이썬 문법을 활용하여 data 리스트 값에 10을 곱하기 Start")
    print("")
    data = [1, 2, 3, 4]
    result = []

    for i in data:
        result.append(i * 10)
    
    print(result)

    print("")
    print("Numpy를 사용하지 않고 기존 파이썬 문법을 활용하여 data 리스트 값에 10을 곱하기 End")
    print("="*30)

# 함수 이름 : NummpyTest
# 최조 작성일 : 2023년 2월 5일
# 최초 작성자 : 김호성
# 내용 : Nummpy 테스트
#       for문을 사용하지 않고 간단히 구현
# 입력 : 없음
# 출력 : 없음
# 기타 : numpy import 필요
# 변경 이력
#   -
def NummpyTest():
    print("="*30)
    print("Numpy를 활용하여 data 리스트 값에 10을 곱하기 Start")
    print("")
    
    data = [1, 2, 3, 4]
    arr = np.array(data)    # numpy의 array에 리스트 값을 넘겨주고 출력 결과를 arr에서 받는다. 
                            # 그결과 numpy 안에 ndarray 클래스의 개체가 생성됨
                            # 파이썬 리스트 타입이 numpy의 ndarray 클래스 타입으로 변환

    arr10 = arr * 10        # arr 값에 10을 곱한다.

    print(arr10)

    print("")
    print("Numpy를 활용하여 data 리스트 값에 10을 곱하기 End")
    print("*"*30)

    print("*"*30)
    print("Numpy를 활용하여 n차원의 데이터를 표현하기 Start")
    print("")
    
    price = [                       
        [100, 80, 70, 90],
        [120, 110, 100, 110]
    ]
    print("price리스트의 1행 인덱싱")
    print(price[0]) # 위와 같이 price 리스트를 생성하면 인덱싱 할경우 행단위로 가져올 수 밖에 없다. 

    arr = np.array(price)
    print("arr[1,2] : ", arr[1,2])
    print("arr[1][2] : ", arr[1][2])

    # 넘파이 슬라이싱의 경우 행 ➡︎ 열 순으로 접근
    print("arr의 1열 : ", arr[:, 0]) 
    print("arr의 2행 : ", arr[1, :])

    print("")
    print("Numpy를 활용하여 n차원의 데이터를 표현하기 End")
    print("="*30)

# 함수정의 부분 end
# ================

# ================
# 프로그램 실행 부분 start
NummpyTestNone()
NummpyTest()

# 프로그램 실행 부분 end
# ================