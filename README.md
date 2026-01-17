# 🏀 Basketball Fundamentals CLI

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Topic](https://img.shields.io/badge/Topic-Sports-FF5E00?style=for-the-badge&logo=nba&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**터미널에서 만나는 농구의 모든 것.**<br>
역사, 규칙, 포지션 정보를 인터랙티브한 CLI 환경에서 확인하세요.

---
</div>

## ✨ Features

- **Interactive Menu**: 사용자가 원하는 정보를 직접 선택하여 탐색
- **Typewriter Effect**: 타자기 효과(`slow_print`)를 통한 몰입감 있는 텍스트 출력
- **Structured Data**: `Class` 기반의 깔끔한 데이터 구조

## 🚀 Preview

```bash
------------------------------
어떤 정보를 확인하시겠습니까?
1. 농구란 무엇인가? (소개)
2. 포지션 설명
3. 주요 규칙
4. 역사
5. 종료
------------------------------
선택(번호 입력): 1

==================================================
          🏀  BASKETBALL INFO  🏀
==================================================
농구는 각 5명으로 구성된 두 팀이
코트(28m x 15m) 위에서... (타자치는 효과 중)
```

## 💻 Source Code

파이썬의 **객체 지향(OOP)** 스타일로 작성되어, 유지보수와 확장이 용이합니다.

```python
import time
import sys

class Basketball:
    """
    농구(Basketball) 종목에 대한 정보를 담고 소개하는 클래스입니다.
    """
    def __init__(self):
        self.court_size = "28m x 15m"
        self.rim_height = "3.05m"
        self.players_per_team = 5
        self.shot_clock = "24초"
        
        # 포지션 데이터 구조화
        self.positions = {
            "PG": {"name": "포인트 가드 (Point Guard)", "role": "코트의 야전사령관, 경기 조율"},
            "SG": {"name": "슈팅 가드 (Shooting Guard)", "role": "주득점원, 3점슛과 돌파"},
            "SF": {"name": "스몰 포워드 (Small Forward)", "role": "다재다능한 득점원"},
            "PF": {"name": "파워 포워드 (Power Forward)", "role": "골밑 수비 및 중거리 슛"},
            "C":  {"name": "센터 (Center)", "role": "팀의 기둥, 골밑 장악"}
        }

    # ... (생략된 메서드들)

    def slow_print(self, text, delay=0.03):
        """텍스트를 타자기처럼 한 글자씩 출력하는 심미적 효과"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

if __name__ == "__main__":
    # 인스턴스 생성 및 실행
    game = Basketball()
    game.main()
```

## 🛠️ How to Run

1. **Repository**를 클론합니다.
2. 터미널에서 아래 명령어를 실행하세요.

```bash
cd basketball_fundamentals
python basketball_info.py
```

<br>

<div align="center">
    <strong>Code is Poetry. Court is Life.</strong>
</div>
