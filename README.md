# Tiny NPC
- [ ] 과제 요약 (1. 미션 소개)
- [ ] 최종 결과물 확인 (2. 최종 결과물)
  - [ ] `기능이 완성된 콘솔 애플리케이션` 존재 여부
    - [ ] 사용자 입력 (3×3)
    - [ ] JSON 데이터 분석
    - [ ] 성능 분석
  - [ ] `출력/화면(콘솔`
  - [ ] `README.md`
- [x] 과제 목표
- [ ] 기능 요구 사항 확인
  - [ ] 데이터 구조
  - [ ] 모드 1 입력 처리(3×3)
  - [ ] 모드 2 JSON 로드 및 스키마 검증(data.json)
  - [ ] 라벨 정규화(표준화) 필수 구현
  - [ ] MAC 연산 (외부 라이브러리 금지)
  - [ ] 점수 비교 정책(부동소수점/동점 처리 기준)
- [ ] 제약 사항 


- [x] Python 3.8 이상인지 확인 (6. 개발 환경 확인)
    - [x] image 첨부
    - [x] 명령어 및 코드 실행 결과 첨부

- [x] 외부 라이브러리 사용 확인(NumPy, pandas) (6. 개발 환경 확인)
    - [x] image 첨부
    - [x] 명령어 및 코드 실행 결과 첨부

- [x] 표준 라이브러리 사용 확인(json, time 등) (6. 개발 환경 확인)
    - [x] image 첨부
    - [x] 명령어 및 코드 실행 결과 첨부

- [ ] 실행 방법
- [ ] 구현 요약
- [ ] 결과 리포트

## 1. 과제 요약
MAC 연산의 핵심 원리를 직접 코드로 구현해 봅니다. 3×3부터 25×25까지 다양한 크기의 패턴을 판별하는 Mini NPU 시뮬레이터를 만들어보며 데이터 크기에 따라 연산 시간이 어떻게 변하는지 직접 계산해보고, 시뮬레이터를 만들면서 발생하는 문제들을 해결해 봅니다.

## 2. 최종 결과물

## 3. 과제 목표
- MAC(Multiply-Accumulate) 연산이 무엇이고, AI에서 왜 중요한지 설명할 수 있다.
- 입력 패턴과 필터를 곱하고 더해서 유사도(점수)를 계산하는 원리를 설명할 수 있다.
- data.json의 “키 규칙/라벨 규칙”을 해석하고, 프로그램 내부에서 라벨을 표준화(정규화)하는 이유를 설명할 수 있다.
- 부동소수점 오차가 판정에 어떤 영향을 주는지, 그리고 허용오차(epsilon) 기반 비교 정책이 필요한 이유를 설명할 수 있다.
- 크기별 연산 시간을 측정하고, 패턴 크기 증가에 따른 시간 복잡도 O(N²)를 근거와 함께 설명할 수 있다.
- 실패 케이스가 발생했을 때 원인을 “데이터/스키마 문제 vs 로직 문제 vs 수치 비교 문제”로 분리해 진단하고 개선할 수 있다.

## 6. 개발 환경 확인

### 파이썬 버전 이미지 첨부

- [파이썬 버전](images/PythonVersion.png)

### 파이썬 버전 터미널로 확인

- 명령어
    ```
    python --version
    ```

-   실행 결과
    ```
    singainnn6931@c4r2s5 Codyssey_B3_TinyNPU % python --version
    Python 3.12.13
    ```

### 외부 라이브러리 사용 이미지 첨부

- [외부 라이브러리 사용 여부](images/CheckExternalLibrary.png)

### 외부 라이브러리 사용 터미널로 확인

- 명령어
    ```
    grep -R -E "import numpy|from numpy|np\." --include="*.py" .
    ```

-   실행 결과
    ```
    singainnn6931@c4r2s5 Codyssey_B3_TinyNPU % grep -R -E "import numpy|from numpy|np\." --include="*.py" .
    singainnn6931@c4r2s5 Codyssey_B3_TinyNPU % 
    ```


### 표준 라이브러리 사용 이미지 첨부

- [표준 라이브러리 사용 여부](images/CheckExternalLibrary.png)

### 표준 라이브러리 사용 터미널로 확인

- 명령어
    ```
    grep -R -E "^(import|from) " --include="*.py" 
    ```

-   실행 결과
    ```
    singainnn6931@c4r2s5 Codyssey_B3_TinyNPU % grep -R -E "^(import|from) " --include="*.py" .
    ./main.py:import time
    ./main.py:import json
    ```



## 7. 제약 사항
- [ ] 구현 및 품질 기준
  - [ ] MAC 연산은 반복문으로 직접 구현
  - [ ] 모드 1 입력은 “행/열 개수, 숫자 파싱” 최소 검증을 수행하고, 오류 시 재입력을 유도한다.
  - [ ] 모드 2에서 스키마/크기 불일치가 발생해도 프로그램이 중단되지 않도록 처리한다(케이스 단위 FAIL 처리 권장).
- [ ] 제출물 확인
  - [ ] main.py
  - [ ] README.md: 실행 방법 + 결과 리포트(실패 원인 분석 + 시간 복잡도 분석)
- [ ] 재현성
    - [ ] 모드 1: 3×3 십자가 필터와 X 필터를 예시대로 입력했을 때 점수/판정/시간이 정상 출력되어야 한다.
    - [ ] 모드 2: data.json 분석 실행 시 각 케이스의 PASS/FAIL과 총합(총/통과/실패)이 일치해야 한다.
    - [ ]의도적 오류 입력(행/열 개수 불일치, 크기 불일치 등)에 대해 안내 메시지 출력 후 재입력 유도 또는 케이스 단위 FAIL 처리가 동작해야 한다.



### 실행 방법
```
git clone https://github.com/hena-archive/Codyssey_B3_TinyNPU.git

cd Codyssey_B3_TinyNPU.git

python main.py
```

### 구현 요약

```
main()
 ├─ 모드 1 : UserInput()
 │   ├─ 필터 A 입력
 │   ├─ 필터 B 입력
 │   ├─ 패턴 입력
 │   ├─ MAC 연산
 │   ├─ 점수 비교
 │   └─ 결과 출력
 │
 └─ 모드 2 : AnalyzeJSON()
     ├─ data.json 읽기
     ├─ 필터 검증 및 정규화
     ├─ 패턴 검증 및 정규화
     ├─ MAC 연산
     ├─ PASS / FAIL 판정
     └─ 결과 요약 출력

Etc
 └─ Json 입출력
```


## 결과 리포트

### 실행 결과

총 6개의 테스트 케이스를 실행했으며, 3개 모두 FAIL이 발생했다.

| Case | Cross 점수 | X 점수 | 판정 | Expected | 결과 |
|---|---:|---:|---|---|---|
| size_5_1 | 0.9 | 0.8999999999999999 | UNDECIDED | X | FAIL |
| size_13_2 | 7.499999999999997 | 7.5 | UNDECIDED | Cross | FAIL |
| size_25_1 | 4.9 | 4.899999999999999 | UNDECIDED | X | FAIL |

### 실패 원인 분석

세 테스트 케이스 모두 Cross 점수와 X 점수의 차이가 `1e-9`보다 작았다.

프로그램에서는 부동소수점 연산으로 인한 미세한 오차를 고려하기 위해 `EPSILON = 1e-9`를 사용한다.

```python
if abs(cross_score - x_score) < EPSILON:
    return "UNDECIDED"
  ```
실제 점수 차이는 다음과 같다.

size_5_1: 약 1.1 × 10^-16
size_13_2: 약 3.0 × 10^-15
size_25_1: 약 8.9 × 10^-16

모두 1e-9보다 작기 때문에 세 케이스 모두 UNDECIDED로 판정되었다.

하지만 각 케이스의 expected 값은 X, Cross, X이므로 UNDECIDED와 일치하지 않아 최종적으로 모두 FAIL 처리되었다.

따라서 이번 실패의 원인은 MAC 연산 자체가 정상적으로 계산되지 않은 것이 아니라, 두 필터의 점수가 epsilon 범위 내에서 동일하다고 판단되었지만 expected 값은 특정 필터(Cross 또는 X)를 요구하고 있기 때문이다.


### 시간 복잡도 분석

MAC 연산은 N×N 크기의 패턴과 필터를 비교하면서 모든 원소에 대해 곱셈과 덧셈을 수행한다.


```python
for i in range(len(pattern)):
    for j in range(len(pattern[i])):
        score += pattern[i][j] * filter_matrix[i][j]
```
행의 개수가 N이고 각 행마다 N개의 원소를 처리하므로 총 연산 횟수는 N²에 비례한다.

따라서 MAC 연산의 시간 복잡도는:
- O(N²)

5×5 → 25회 | 13×13 → 169회 | 25×25 → 625회 |


### 성능 측정

프로그램에서는 time.perf_counter()를 사용하여 MAC 연산 시간을 측정하고, 동일한 연산을 10회 반복하여 평균 시간을 계산한다.

또한 3×3, 5×5, 13×13, 25×25 크기에 대해 연산 시간을 비교하고 각 크기의 N² 연산 횟수를 함께 출력하도록 구현했다.