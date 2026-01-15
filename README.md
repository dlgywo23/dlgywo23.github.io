# 🐍 파이썬 기초 실력 점검 퀴즈 (10문제)

생성된 5개의 샘플 코드 내용을 바탕으로 만든 퀴즈입니다. 정답은 가장 아래에 있습니다.

---

### **[1-2] 변수와 데이터 타입**

**Q1. 다음 중 파이썬의 데이터 타입과 값이 잘못 연결된 것은?**
1) `age = 25` -> 정수 (int)
2) `name = "Alice"` -> 문자열 (str)
3) `height = 180` -> 실수 (float)
4) `is_ready = True` -> 불리언 (bool)

**Q2. `print(type(3.14))`의 출력 결과는 무엇인가요?**

---

### **[3-4] 조건문 (Conditionals)**

**Q3. 다음 코드의 실행 결과는 무엇인가요?**
```python
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")
```

**Q4. 파이썬에서 "값이 같음"을 비교할 때 사용하는 연산자는?**
1) `=`
2) `==`
3) `===`
4) `!=`

---

### **[5-6] 반복문 (Loops)**

**Q5. `range(1, 5)`는 어떤 숫자들을 생성하나요?**
1) 1, 2, 3, 4, 5
2) 0, 1, 2, 3, 4
3) 1, 2, 3, 4
4) 1, 3, 5

**Q6. 다음 코드의 최종 `total` 값은?**
```python
total = 0
for i in [1, 2, 3]:
    total = total + i
```

---

### **[7-8] 데이터 구조 (List & Dictionary)**

**Q7. `colors = ["red", "green"]` 리스트에 "blue"를 마지막에 추가하는 함수는?**
1) `colors.add("blue")`
2) `colors.push("blue")`
3) `colors.append("blue")`
4) `colors.insert("blue")`

**Q8. 딕셔너리 `user = {"name": "Tom", "age": 20}`에서 'Tom'이라는 값을 가져오기 위한 코드는?**

---

### **[9-10] 함수 (Functions)**

**Q9. 다음 코드의 출력 결과는?**
```python
def multiply(a, b):
    return a * b

result = multiply(3, 4)
print(result)
```

**Q10. 함수에서 결과값을 호출한 곳으로 되돌려줄 때 사용하는 키워드는?**

---

<br><br><br><br><br>

## 📌 정답지

1.  **3번** (`180`은 소수점이 없으므로 정수입니다. 실수는 `180.0`처럼 표현됩니다.)
2.  **<class 'float'>**
3.  **B** (85는 90보다 작고 80보다 크거나 같으므로 `elif` 문이 실행됩니다.)
4.  **2번** (`==`)
5.  **3번** (시작 값은 포함, 끝 값은 미포함입니다.)
6.  **6** (1+2+3)
7.  **3번** (`append`)
8.  **user["name"]** 또는 **user.get("name")**
9.  **12**
10. **return**
