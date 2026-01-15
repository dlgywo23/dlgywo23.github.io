import random
import csv
import os

# 설정
classes = 5
students_per_class = 30
output_file = "student_scores.csv"

# 데이터 생성
data = []
for ban in range(1, classes + 1):
    for no in range(1, students_per_class + 1):
        # 임의의 점수 생성
        final_exam = random.randint(40, 100)  # 기말고사 (0-100)
        perf1 = random.randint(10, 20)        # 수행평가 1 (만점 20)
        perf2 = random.randint(5, 10)         # 수행평가 2 (만점 10)
        perf3 = random.randint(5, 10)         # 수행평가 3 (만점 10)
        
        # 합계 계산 (기말 60% 반영 + 수행 40% 합산)
        total_score = (final_exam * 0.6) + perf1 + perf2 + perf3
        
        data.append({
            "반": f"{ban}반",
            "번호": no,
            "기말(100)": final_exam,
            "수행1(20)": perf1,
            "수행2(10)": perf2,
            "수행3(10)": perf3,
            "총점(100)": round(total_score, 1)
        })

# CSV 파일로 저장
with open(output_file, mode='w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print(f"총 {len(data)}명의 데이터가 '{output_file}'에 저장되었습니다.")
