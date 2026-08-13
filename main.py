import time

# 입력 부분 공부
def LearnInput():
    '''입출력 테스트 부부'''

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


filter_a = []
filter_b = []


# npu 메뉴 출력 부분
def print_npu_simulator_menu():
    print("=== Mini NPU Simulator ===")
    print("[모드 선택]")
    print("1. 사용자 입력 (3x3)")
    print("2. data.json 분석")


# 
def PrintInputFilterHeader():
    print("#----------------------------------------")
    print("# [1] 필터 입력")
    print("#----------------------------------------")


def PrintInputFilter(filter_type):
    filter_type = filter_type.upper()

    if not (filter_type == 'A' or filter_type == 'B'):
        print("PrintInputFilter error")
        return

    print("필터 ", filter_type, "(3줄 입력, 공백 구분)")


def CreateMatrix(matrix, num = 3):
    # 초기화
    if len(matrix) > 0:
        matrix = []

    while len(matrix) < num:
        # 인풋 받기
        row = input()

        # 에러 체크
        try:
            numbers = row.split()
            numbers = [float(x) for x in numbers]
            if len(numbers) != num:
                print(f"오류: {num}개의 숫자를 입력해야 합니다.")
                continue
            matrix.append(numbers)
        except ValueError:
            print("오류: 숫자만 입력해주세요")

def PrintInputPattern():
    print("#---------------------------------------")
    print("# [2] 패턴 입력")
    print("#---------------------------------------")
    print("패턴 (3줄 입력, 공백 구분)")


def GetScore(filter, pattern, num = 3):
    total = 0.0
    for i in range(num):
        for j in range(num):
            total += filter[i][j] * pattern[i][j]

    return total


def PrintMAC(score_a, score_b, avg_runtime, judgment_type):
    print("#---------------------------------------")
    print("# [3] MAC 결과")
    print("#---------------------------------------")
    print("A 점수:", score_a)
    print("B 점수:", score_b)
    print("연산 시간(평균/10회):", avg_runtime, "ms")

    match judgment_type:
        case 0:
            print("판정: A")
        case 1:
            print("판정: B")
        case 2:
            print("판정 불가")
    

def CalculateNpuSimilarity(score_a, score_b):
    judge_type = 3

    diff = abs(score_a - score_b)

    if diff < 1e-9:
        judge_type = 2
    elif score_a > score_b:
        judge_type = 0
    else:
        judge_type = 1

    return judge_type


def PrintUserInputMatrix(name, matrix):
    print("=" * 30)
    print(f"name이 {name}인 matrix 출력")
    print("=" * 30)
    for i in range(3):
        for j in range(3):
            print(matrix[i][j], end = " ")
        print()
    print()
    print()

def UserInput():
    # 1-1. 필터 입력 헤더 출력
    PrintInputFilterHeader()

    # 1-2. 필터 A 입력 받기
    PrintInputFilter('A')
    CreateMatrix(filter_a)

    # 1-3. 필터 B 입력 받기
    PrintInputFilter('B')
    CreateMatrix(filter_b)

    # 2-1. 패턴 입력 헤더 출력
    PrintInputPattern()

    # 2-2. 패턴 입력 받기
    pattern = []
    CreateMatrix(pattern)

    # User Input 확인 부분으로 변경
    PrintUserInputMatrix("filter_a", filter_a)
    PrintUserInputMatrix("filter_b",filter_b)
    PrintUserInputMatrix("pattern",pattern)

    # 3-1 각 점수 계산하기
    score = []
    score.append(GetScore(filter_a, pattern))
    score.append(GetScore(filter_b, pattern))


    start = time.perf_counter()

    for _ in range(10):
        GetScore(filter_a, pattern)
        GetScore(filter_b, pattern)

    end = time.perf_counter()

    avg_runtime = (end - start) / 10 * 1000

    # 3-2 판단하기
    judge = CalculateNpuSimilarity(score[0], score[1])

    PrintMAC(score[0], score[1], avg_runtime, judge)

import json

def ReadJSON():
    # with은 스코프를 만들지 않는다. ㅋㅋ
        with open("basic.json", "r+", encoding="utf-8") as file:
            data = json.load(file)
    
    
        # 스코프 나가도 data가 되는 이유임 ㅋㅋㅋ
        print("### data 출력 ###")
        print(data)
        print("\n### data 출력 완료 ###\n")
    
        # type 출력
        print(type(data))
        print()
    
        # str 출력
        print(data['name'])
        print(type(data['name']))
        print()
    
        # int 출력
        print(data['age'])
        print(type(data['age']))
        print()
    
        # float 출력
        print(data['height'])
        print(type(data['height']))
        print()
    
        # float 출력
        print(data['student'])
        print(type(data['student']))
        print()
    
        # list - hobbies 출력
        print(data['hobbies'])
        print(type(data['hobbies']))
    
        for hobby in data['hobbies']:
            print(hobby, type(hobby))
        print()
    
        # list - score 출력
        print(data['scores'])
        print(type(data['scores']))
        for score in data['scores']:
            print(score, type(score))
        print()
    
        # dict - address 출력
        print(data['address'])
        print(type(data['address']))
        for addr in data['address']:
            print(addr, type(addr))
        print()
    
        # list 안의 dict - friends 출력
        print(data['friends'])
        print(type(data['friends']))
        for friend in data['friends']:
            print(friend, type(friend))
    
    
            # 방법 - enumerate 불가
            # for name, age, student in enumerate(friend):
            #     print(name, age, student)
    
            # 방법 - dict.items
            for key, value in friend.items():
                print(key, value)
    
            # 방법 - 직접 뽑기
            name = friend['name']
            age = friend['age']
            student = friend['student']
            print(name, age, student)
        print()
    
        # 2차원 matrix 출력
        print(data['matrix'])
        print(type(data['matrix']))
        for mat in data['matrix']:
            print(mat, type(mat))
        
        print()
    
        # dict 안에 리스트
        for idx,  skill in enumerate(data['skills']):
            print(idx, skill)
        print()

def WriteJSON():
    data = {
        "name": "철수",
        "age": 20,
        "hobbies":[
            "게임",
            "독서"
        ],
        "foods":{
            
        }
    }

    data['foods']['lunch'] = "막국수"

    with open("write.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=True, indent=2)

    pass

def LearnJSON():
    # 읽기
    # ReadJSON()

    # 쓰기
    WriteJSON()


def PrintJSON(data, key = ""):
    match key:
        case "":
            print(data)
        case "filters_5_c":
            print(data['filters']['size_5']['cross'])
        case "filters_5_x":
            print(data['filters']['size_5']['x'])
        case "filters_13_c":
            print(data['filters']['size_13']['cross'])
        case "filters_13_x":
            print(data['filters']['size_13']['x'])
        case "filters_25_c":
            print(data['filters']['size_25']['cross'])
        case "filters_25_x":
            print(data['filters']['size_25']['x'])


        case "filters_5_c":
            print(data['filters']['size_5']['cross'])
        case "filters_5_x":
            print(data['filters']['size_5']['x'])
        case "filters_13_c":
            print(data['filters']['size_13']['cross'])
        case "filters_13_x":
            print(data['filters']['size_13']['x'])
        case "filters_25_c":
            print(data['filters']['size_25']['cross'])
        case "filters_25_x":
            print(data['filters']['size_25']['x'])


def LoadFilters(filters):
    print("#---------------------------------------")
    print("# [1] 필터 로드")
    print("#---------------------------------------")

    normalizedFilters = {}


    for sizeName, filterData in filters.items():
        print("my Key: ", sizeName)

        strList = []
        strList = sizeName.split("_")

        # size_N 형태인지 확인하기
        flag = False
        if len(strList) != 2:
            print("x ", sizeName, " 필터 로드 실패 (Cross, X)")
        else:
            try:
                size = int(strList[1])
                name = strList[0]
                if name != "size":
                    print("x ", sizeName, " 필터 로드 실패 (Cross, X)")
                    continue

                # Todo: 살짝 애매
                if type(size) != int:
                    print("x ", sizeName, " 필터 로드 실패 (Cross, X)")
                    continue

                print("✓ ", sizeName, " 필터 로드 완료 (Cross, X)")
            except:
                print("x ", sizeName, " 필터 로드 실패 (Cross, X)")


        newFilter = {}
        # 라벨 필터링
        for filterName, matrix in filterData.items():
            if filterName == "cross":
                filterName = "Cross"
            elif filterName == "x":
                filterName = "X"
            else:
                pass
            newFilter[filterName] = matrix

        # filter 자체를 넣기
        normalizedFilters[sizeName] = newFilter


    # print (normalizedFilters)
            
    return normalizedFilters

def LoadPatterns(patterns):
    normalizedPatterns = {}
    
    
    for sizeName, patternData in patterns.items():
        

        newPattern = {}
        # 라벨 필터링
        for patternKey, originData in patternData.items():
            if patternKey == "input":
                pass

            elif patternKey == "expected":
                if originData == "x":
                    originData = "X"
                elif originData == "+":
                    originData = "Cross"
            else:
                pass
            newPattern[patternKey] = originData

        # pattern 자체를 넣기
        normalizedPatterns[sizeName] = newPattern


    # print (normalizedPatterns)
            
    return normalizedPatterns

def AnalyzePatterns(normalizeFilters, normalizePatterns):

    totalCount = 0
    successCount = 0
    fail = {}
    for patternSize, patternData in normalizePatterns.items():
        strList = patternSize.split('_')

        # 개수 체크
        if len(strList) != 3:
            print("tqtqtqtq\n\n\n\n")
            continue

        totalCount += 1
        keyName = strList[0] + "_" + strList[1]
        print ("----- ", patternSize, " -----")

        
        # 점수 계산 시작
        cross_score = mac(patternData['input'], normalizeFilters[keyName]['Cross'])
        x_score = mac(patternData['input'], normalizeFilters[keyName]['X'])
        print("Cross 점수: ", cross_score)
        print("X 점수: ", x_score)

        result = decide(cross_score, x_score)
        expected = patternData['expected']
        if result == expected:
            pf = "PASS"
            successCount += 1
        else:
            pf = "FAIL"
            if result == "UNDECIDED":
                fail[patternSize] = f"{patternSize} : 동점(UNDECIDED) 처리 규칙에 따라 FAIL"
            elif result == "Cross":
                fail[patternSize] = f"{patternSize} : Cross < +"
            else:
                fail[patternSize] = f"{patternSize} : Cross > +"
        print(f"핀장: {result} | expected: {expected} | {pf}")
        print()
    return [totalCount, successCount, fail]
    pass


def NormalizeFilter(value):
    """filter 키를 표준 라벨로 변환"""
    value = str(value).strip().lower()

    if value == "cross":
        return "Cross"

    if value == "x":
        return "X"

    return None


def AnalyzeJSON(filename = ""):

    # file 이름이 ""인 경우
    if filename == "":
        filename = "data.json"

    # with 문법은 알아둬.
    with open(filename, "r", encoding="utf-8") as fd:
        data = json.load(fd)

    # 이게 되는 이유 알아두기
    # print(data)

    AnalyzeData(data)

    # performance_test(
    #     data["filters"]
    # )
    

    # json 출력 테스트
    # PrintJSON(data, "filters_5_c")


EPSILON = 1e-9


# ==========================================
# 라벨 정규화
# ==========================================

def normalize_label(value):
    value = str(value).strip().lower()

    if value in ["+", "cross"]:
        return "Cross"

    if value == "x":
        return "X"

    return None


# ==========================================
# MAC 연산
# ==========================================

def mac(pattern, filter_matrix):
    score = 0.0

    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            score += pattern[i][j] * filter_matrix[i][j]

    return score


# ==========================================
# 판정
# ==========================================

def decide(cross_score, x_score):

    if abs(cross_score - x_score) < EPSILON:
        return "UNDECIDED"

    if cross_score > x_score:
        return "Cross"

    return "X"


# ==========================================
# JSON 불러오기
# ==========================================

def load_json(filename):

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


# ==========================================
# 패턴 하나 테스트
# ==========================================

def TestPattern(pattern_id, pattern_data, filters):

    pattern = pattern_data["input"]

    # expected 정규화
    expected = normalize_label(pattern_data["expected"])

    # 패턴 크기 확인
    size = len(pattern)

    filter_key = f"size_{size}"

    cross_filter = filters[filter_key]["cross"]
    x_filter = filters[filter_key]["x"]

    # MAC
    cross_score = mac(pattern, cross_filter)
    x_score = mac(pattern, x_filter)

    # 판정
    result = decide(cross_score, x_score)

    # PASS / FAIL
    if result == expected:
        status = "PASS"
    else:
        status = "FAIL"

    # 출력
    print(f"\n[{pattern_id}]")
    print(f"크기       : {size}x{size}")
    print(f"Cross 점수 : {cross_score}")
    print(f"X 점수     : {x_score}")
    print(f"판정       : {result}")
    print(f"Expected   : {expected}")
    print(f"결과       : {status}")

    if status == "FAIL":

        if result == "UNDECIDED":
            reason = "두 필터 점수가 epsilon 범위 내에서 동일함"
        else:
            reason = f"Expected={expected}, 실제 판정={result}"

        print(f"실패 사유  : {reason}")

    return status


# ==========================================
# 전체 데이터 분석
# ==========================================

def AnalyzeData(data):

    print ("AnalyzeData")
    filters = data["filters"]
    patterns = data["patterns"]

    total = 0
    passed = 0
    failed = 0

    # 이게 되네 ㅋㅋ
    print("=" * 60)
    print("data.json 분석 시작")
    print("=" * 60)


    # 1. 필터 로드 후 라벨 정규화된 필터로 교체
    filters = LoadFilters(filters)
    patterns = LoadPatterns(patterns)

    # 2. 패턴 분석
    summary = AnalyzePatterns(filters, patterns)


    # 4. 결과 요약
    print("총 테스트: ", summary[0], "개")
    print("통과: ", summary[1], "개")
    print("실패: ", summary[0] - summary[1], "개")

    print("실패 케이스: ")
    for key, reason in summary[2].items():
        print(key, reason)



    # for pattern_id, pattern_data in patterns.items():

    #     total += 1
    #     print("qwer:", pattern_id, pattern_data)
        # status = TestPattern(
        #     pattern_id,
        #     pattern_data,
        #     filters
        # )

        # if status == "PASS":
        #     passed += 1
        # else:
        #     failed += 1

    # # 결과 요약
    # print("\n" + "=" * 60)
    # print("결과 요약")
    # print("=" * 60)

    # print(f"전체 테스트 : {total}")
    # print(f"통과        : {passed}")
    # print(f"실패        : {failed}")


# ==========================================
# 성능 측정
# ==========================================

def measure_mac(size, filters, repeat=10):

    filter_key = f"size_{size}"

    cross_filter = filters[filter_key]["cross"]

    # 테스트용 패턴
    pattern = [
        [1.0 for _ in range(size)]
        for _ in range(size)
    ]

    total_time = 0.0

    for _ in range(repeat):

        start = time.perf_counter()

        mac(pattern, cross_filter)

        end = time.perf_counter()

        total_time += end - start

    average_time = total_time / repeat

    return average_time * 1000


# ==========================================
# 성능 분석
# ==========================================

def performance_test(filters):

    print("\n" + "=" * 60)
    print("성능 분석")
    print("=" * 60)

    print("크기(NxN) | 평균 시간(ms) | 연산 횟수(N²)")
    print("-" * 45)

    for size in [3, 5, 13, 25]:

        # 3x3 필터는 현재 JSON에 없기 때문에
        # 성능 측정용으로 별도 생성
        if size == 3:

            filter_matrix = [
                [1.0 for _ in range(3)]
                for _ in range(3)
            ]

            pattern = [
                [1.0 for _ in range(3)]
                for _ in range(3)
            ]

            total_time = 0.0

            for _ in range(10):

                start = time.perf_counter()

                mac(pattern, filter_matrix)

                end = time.perf_counter()

                total_time += end - start

            average_ms = (total_time / 10) * 1000

        else:

            average_ms = measure_mac(
                size,
                filters,
                repeat=10
            )

        operation_count = size * size

        print(
            f"{size}x{size:<5} | "
            f"{average_ms:.6f}      | "
            f"{operation_count}"
        )




# 실제 메인 함수
def main():
    # 메뉴 출력 함수 호출
    print_npu_simulator_menu()

    # 메뉴 선택
    choice = int(input("선택: "))

    # 메뉴 확인 (예외 처리 일부로 안함 - 조건 없음)
    print("선택한 모드:", choice)

    # 3.10? 이상 문법임
    match choice:
        case 1:
            UserInput()
        case 2:
            AnalyzeJSON()

# main 실행
if __name__ == "__main__":
    # 테스트 코드
    # LearnInput()

    # JSON
    # LearnJSON()

    # 실제 실행될 코드
    main()