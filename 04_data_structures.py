# 4. 데이터 구조 (Data Structures - List/Dictionary)

# 리스트 (List): 순서가 있는 목록
colors = ["red", "green", "blue"]
print(f"기존 색상: {colors}")

colors.append("yellow")  # 추가
print(f"추가 후: {colors}")

colors[1] = "emerald"    # 수정
print(f"수정 후: {colors}")

# 딕셔너리 (Dictionary): 키(Key)와 값(Value)의 쌍
user = {
    "id": "antigravity",
    "level": 10,
    "active": True
}

print(f"\n유저 ID: {user['id']}")
print(f"유저 레벨: {user.get('level')}")

# 새로운 키-값 추가
user["exp"] = 500
print(f"전체 정보: {user}")
