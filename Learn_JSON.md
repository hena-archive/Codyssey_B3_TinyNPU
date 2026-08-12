# JSON 기초

Python에서 `data.json` 파일을 읽고 쓰기 위해 JSON의 기본적인 구조와 문법을 알아본다.

---

## 1. JSON이란?

**JSON (JavaScript Object Notation)**은 데이터를 저장하거나 주고받기 위한 데이터 형식이다.

예를 들어 학생 정보를 저장한다면 다음과 같이 작성할 수 있다.

```json
{
  "name": "철수",
  "age": 20,
  "score": 95
}
```

주요 특징텍스트 기반: 
- 언어에 독립적이어서 거의 모든 프로그래밍 언어에서 지원합니다.

가벼운 구조: 
- XML에 비해 오버헤드가 적어 전송 속도가 빠릅니다.

주석 미지원: 
- 데이터 교환에 초점을 맞춰 주석을 허용하지 않습니다

JSON의 기본적인 형태는 다음과 같다.

```text
"키": 값
```

예:

```json
"name": "철수"
"age": 20
"score": 95
```

---

## 2. JSON의 핵심 기호

| 기호 | 이름 | 의미 | 예시 |
|---|---|---|---|
| `{ }` | 객체(Object) | 데이터를 Key-Value 형태로 저장 | `{"name": "철수"}` |
| `[ ]` | 배열(Array) | 여러 데이터를 순서대로 저장 | `["철수", "영희"]` |
| `:` | 콜론 | Key와 Value를 연결 | `"name": "철수"` |
| `,` | 쉼표 | 여러 데이터를 구분 | `"name": "철수", "age": 20` |
| `"` | 큰따옴표 | 문자열을 표시 | `"hello"` |


### `{ }` 객체(Object)

`{}`는 Key와 Value를 이용해서 데이터를 관리하는 구조이다.

```json
{
  "name": "철수",
  "age": 20,
  "score": 95
}
```

- 위 코드에 해당하는 설명
    | Key | Value |
    |---|---|
    | `name` | `"철수"` |
    | `age` | `20` |
    | `score` | `95` |

- Python에서는 `dict`와 비슷하다.

```python
student = {
    "name": "철수",
    "age": 20,
    "score": 95
}
```

| JSON | Python |
|---|---|
| 객체(Object) | `dict` |
| `{}` | `{}` |
| Key-Value | Key-Value |

---

### `[ ]` 배열(Array)

`[]`는 여러 데이터를 순서대로 저장할 때 사용한다.

```json
[
  "철수",
  "영희",
  "민수"
]
```

Python에서는 `list`와 비슷하다.

```python
students = [
    "철수",
    "영희",
    "민수"
]
```

| JSON | Python |
|---|---|
| 배열(Array) | `list` |
| `[]` | `[]` |

---

### 객체 vs 배열
- 이름을 붙여서 데이터를 관리한다.
```json
{
  "name": "철수",
  "age": 20
}

name → 철수
age  → 20
```

- 여러 데이터를 순서대로 관리한다.

```json
[
  "철수",
  "영희",
  "민수"
]

0 → 철수
1 → 영희
2 → 민수
```

| 구조 | 목적 |
|---|---|
| `{}` | 이름(Key)을 이용해서 데이터 관리 |
| `[]` | 여러 데이터를 순서대로 관리 |

---

## 객체 안에 배열 넣기

JSON에서는 `{}`와 `[]`를 조합해서 사용할 수 있다.

```json
{
  "students": [
    "철수",
    "영희",
    "민수"
  ]
}
```

구조:

```text
객체 {}
 │
 └── students
       │
       └── 배열 []
             ├── 철수
             ├── 영희
             └── 민수
```

Python:

```python
data = {
    "students": [
        "철수",
        "영희",
        "민수"
    ]
}
```

---

## 7. 배열 안에 객체 넣기

실제 JSON에서는 배열 안에 객체를 넣는 형태도 많이 사용한다.

```json
[
  {
    "name": "철수",
    "age": 20
  },
  {
    "name": "영희",
    "age": 21
  }
]
```

구조:

```text
배열 []
 │
 ├── 객체 {}
 │    ├── name
 │    └── age
 │
 └── 객체 {}
      ├── name
      └── age
```

Python:

```python
students = [
    {
        "name": "철수",
        "age": 20
    },
    {
        "name": "영희",
        "age": 21
    }
]
```

---

## 8. JSON의 데이터 타입

| JSON 타입 | 예시 | 설명 |
|---|---|---|
| 문자열(String) | `"철수"` | 문자 데이터 |
| 숫자(Number) | `20` | 숫자 데이터 |
| 참(Boolean) | `true` | 참 |
| 거짓(Boolean) | `false` | 거짓 |
| null | `null` | 값이 없음 |
| 객체(Object) | `{...}` | Key-Value 구조 |
| 배열(Array) | `[...]` | 여러 데이터를 저장 |

### 문자열

```json
{
  "name": "철수"
}
```

`"철수"`는 문자열이다.

### 숫자

```json
{
  "age": 20
}
```

`20`은 숫자다.

### Boolean

```json
{
  "student": true
}
```

```json
{
  "student": false
}
```

### null

```json
{
  "nickname": null
}
```

Python의 `None`과 비슷하다.

| JSON | Python |
|---|---|
| `null` | `None` |

---

## JSON과 Python의 대응 관계

| JSON | Python |
|---|---|
| Object | `dict` |
| Array | `list` |
| String | `str` |
| Number | `int`, `float` |
| `true` | `True` |
| `false` | `False` |
| `null` | `None` |

---

## JSON에서 주의할 문법

### Key와 Value 사이에는 `:`

```json
{
  "name": "철수"
}
```

```text
"name" : "철수"
   ↑        ↑
  Key     Value
```

### 여러 데이터를 구분할 때 `,`

```json
{
  "name": "철수",
  "age": 20,
  "score": 95
}
```

### 마지막 데이터 뒤에는 쉼표를 붙이지 않는다

올바른 JSON:

```json
{
  "name": "철수",
  "age": 20
}
```

잘못된 JSON:

```json
{
  "name": "철수",
  "age": 20,
}
```

## Python에서 JSON 파일 읽기

`data.json` 파일이 다음과 같다고 가정한다.

### data.json

```json
{
  "name": "철수",
  "age": 20
}
```

Python:

```python
import json

with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(data)
```

결과:

```text
{'name': '철수', 'age': 20}
```

### 핵심

```python
data = json.load(file)
```

의미:

```text
data.json
    ↓
json.load()
    ↓
Python dict
```

---

## 읽은 데이터 사용하기

`json.load()`를 통해 가져온 `data`는 Python의 `dict`이므로 일반적인 딕셔너리처럼 사용할 수 있다.

```python
print(data["name"])
```

결과:

```text
철수
```

```python
print(data["age"])
```

결과:

```text
20
```

## Python 데이터를 JSON 파일에 저장하기

이번에는 반대 방향이다.

```python
import json

data = {
    "name": "영희",
    "age": 25
}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)
```

실행하면 `data.json`에 다음과 같이 저장된다.

```json
{
  "name": "영희",
  "age": 25
}
```

### 핵심

```python
json.dump(data, file)
```

의미:

```text
Python dict
    ↓
json.dump()
    ↓
data.json
```

---

### `ensure_ascii=False`
한글을 JSON에 저장할 때 자주 사용하는 옵션이다.

```python
json.dump(
    data,
    file,
    ensure_ascii=False
)
```

한글을 그대로 저장할 수 있다.

```json
{
  "name": "철수"
}
```

---

### `indent=2`

JSON을 보기 좋게 정렬해주는 옵션이다.

```python
json.dump(
    data,
    file,
    ensure_ascii=False,
    indent=2
)
```

### `indent`가 없는 경우

```json
{"name":"철수","age":20,"score":95}
```

데이터 자체가 달라지는 것은 아니고 사람이 읽기 편하게 만들어주는 옵션이다.
