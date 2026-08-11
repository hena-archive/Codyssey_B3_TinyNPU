# 입력 부분 공부
def LearnInput():
    # 기본 인풋
    input_str = input()
    print("입력 받은 값:", input_str)
    print("입력 받은 타입:", type(input_str))

    # 입력 안내문 보기
    name = input("이름을 입력하세요: ")
    print("안녕하세요,", name)

    # 타입 변환하기
    num = int(input("숫자를 입력하세요.: "))
    print("입력 받은 값:", num)
    print("입력 받은 타입:", type(num))

    # 여러 값을 한 번에 입력받기
    num1, num2 = input("입력 2개 받기: ").split()
    print(num1, type(num1))
    print(num2, type(num2))

    # map(함수, 반복가능한_자료)
    # int가 함수라고?
    m1, m2, m3 = map(int, input("map?!?").split())
    print(m1, m2, m3)

def print_npu_simulator_menu():
    print("=== Mini NPU Simulator ===")
    print()
    print("[모드 선택]")
    print("1. 사용자 입력 (3x3)")
    print("2. data.json 분석")


def main():
    print_npu_simulator_menu()
    
    choice = input("선택: ")

    print("선택한 모드:", choice)

    # 간단한 입력 받아보기




# main 실행
if __name__ == "__main__":
    # 테스트 코드
    LearnInput()

    # 실제 실행될 코드
    # main()
