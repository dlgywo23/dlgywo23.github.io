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
        
        self.positions = {
            "PG": {"name": "포인트 가드 (Point Guard)", "role": "코트의 야전사령관, 경기 조율 및 패스 공급"},
            "SG": {"name": "슈팅 가드 (Shooting Guard)", "role": "주득점원, 3점슛과 돌파 능력"},
            "SF": {"name": "스몰 포워드 (Small Forward)", "role": "내외곽을 가리지 않는 다재다능한 득점원"},
            "PF": {"name": "파워 포워드 (Power Forward)", "role": "골밑 수비, 리바운드, 중거리 슛"},
            "C":  {"name": "센터 (Center)", "role": "팀의 기둥, 골밑 장악, 리바운드 및 블록슛"}
        }
        
        self.milestones = [
            (1891, "제임스 네이스미스 박사가 창안 (복숭아 바구니 사용)"),
            (1936, "베를린 올림픽 정식 종목 채택"),
            (1946, "NBA (미국 프로 농구) 출범"),
            (1992, "바르셀로나 올림픽 '림 짐(Dream Team)' 결성, 세계적 인기 폭발")
        ]

    def slow_print(self, text, delay=0.03):
        """텍스트를 타자기처럼 한 글자씩 출력하는 효과"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def show_intro(self):
        print("\n" + "="*50)
        print("          🏀  BASKETBALL INFO  🏀")
        print("="*50)
        intro_text = (
            f"농구는 각 {self.players_per_team}명으로 구성된 두 팀이\n"
            f"코트({self.court_size}) 위에서 상대방의 바스켓({self.rim_height})에 공을 넣어\n"
            f"점수를 겨루는 구기 종목입니다.\n"
            "빠른 공수 전환과 역동적인 움직임이 특징입니다."
        )
        self.slow_print(intro_text)

    def show_rules(self):
        print("\n[ 📋 기본 규칙 ]")
        rules = [
            f"1. 공격 제한 시간: {self.shot_clock} (샷 클락)",
            "2. 득점: 자유투 1점, 필드골 2점, 3점 라인 밖 3점",
            "3. 드리블: 공을 소유한 채 3걸음 이상 걸으면 안 됨 (트래블링)",
            "4. 반칙: 선수 간의 부당한 신체 접촉 금지 (5반칙 퇴장)"
        ]
        for rule in rules:
            print(f"- {rule}")
            time.sleep(0.5)

    def show_positions(self):
        print("\n[ ⛹️ 포지션 소개 ]")
        for code, info in self.positions.items():
            print(f"[{code}] {info['name']}")
            print(f"    └─ {info['role']}")
            time.sleep(0.3)
            
    def show_history(self):
        print("\n[ 📜 간략한 역사 ]")
        for year, event in self.milestones:
            print(f"{year}년: {event}")
            time.sleep(0.4)

def main():
    bball = Basketball()
    
    while True:
        print("\n" + "-"*30)
        print("어떤 정보를 확인하시겠습니까?")
        print("1. 농구란 무엇인가? (소개)")
        print("2. 포지션 설명")
        print("3. 주요 규칙")
        print("4. 역사")
        print("5. 종료")
        print("-"*30)
        
        choice = input("선택(번호 입력): ")
        
        if choice == '1':
            bball.show_intro()
        elif choice == '2':
            bball.show_positions()
        elif choice == '3':
            bball.show_rules()
        elif choice == '4':
            bball.show_history()
        elif choice == '5':
            print("프로그램을 종료합니다. 즐거운 농구 되세요! 🏀")
            break
        else:
            print("올바른 번호를 입력해주세요.")

if __name__ == "__main__":
    main()

