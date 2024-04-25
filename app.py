import random
import datetime

def coin_flip_simulation():

    n = int(input("동전을 던질 횟수를 입력하세요: "))   #동전 던질 횟수 입력받아서 n에 저장
    heads_count = 0
    tails_count = 0

    time = datetime.datetime.now()  # 로그 파일명 중복 방지용 시각 기록
    formatted_time = time.strftime('%Y-%m-%d %H:%M:%S') # 원하는 시각 포맷으로 변경
    
    with open(f"logs/코인 토스 결과 기록_{formatted_time}.log", "w") as file:   # 로깅 시작
        for i in range(1, n + 1):   # 코인 토스 n 만큼 반복
            flip = random.choice(['앞면', '뒷면'])  # random 모듈로 코인 토스 시작
            if flip == '앞면':
                heads_count += 1
            else:
                tails_count += 1
            file.write(f"{i}번째 던짐: {flip}\n")   # 코인 토스 회차와 결과 로깅
            print(f"{i}번째 던짐: {flip}\n")    # 코인 토스 회차와 결과 출력
        
        empirical_probability_heads = heads_count / n # 앞면 확률 계산
        empirical_probability_tails = tails_count / n # 뒷면 확률 계산
        
        file.write(f"통계적 확률 (앞면): {empirical_probability_heads:.5f} / 수학적 확률: 0.500000\n")  # 앞면 확률 로깅
        file.write(f"통계적 확률 (뒷면): {empirical_probability_tails:.5f} / 수학적 확률: 0.500000\n")  # 뒷면 확률 로깅
        print(f"통계적 확률 (앞면): {empirical_probability_heads:.5f} / 수학적 확률: 0.500000\n")   # 앞면 결과 출력
        print(f"통계적 확률 (뒷면): {empirical_probability_tails:.5f} / 수학적 확률: 0.500000\n")   # 뒷면 결과 출력

# 시뮬레이션 시작
if __name__ == '__main__':
    coin_flip_simulation()