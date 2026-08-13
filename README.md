# Tiny NPC
- [x] Python 3.8 이상인지 확인
    - [x] image 첨부
    - [x] 명령어 및 코드 실행 결과 첨부

- [x] 외부 라이브러리 사용 확인(NumPy, pandas)
    - [x] image 첨부
    - [x] 명령어 및 코드 실행 결과 첨부

- [x] 표준 라이브러리 사용 확인(json, time 등)
    - [x] image 첨부
    - [x] 명령어 및 코드 실행 결과 첨부


- [ ] 실행 방법
- [ ] 구현 요약
- [ ] 결과 리포트

grep -R -E "^(import|from) " --include="*.py" .

## 파이썬 버전 확인

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

## 외부 라이브러리 사용 확인

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


## 표준 라이브러리 사용 확인

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