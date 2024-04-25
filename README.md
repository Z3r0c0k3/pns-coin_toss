# 개요

> 위 Repo는 확률과 통계 교과 연계 프로젝트로, 
> __"코인 토스 게임 기반 시행 횟수와 비례하는 통계적 확률과 수학적 확률의 근접도 상승에 관한 시뮬레이션"__ 프로젝트에 일환입니다. 

## 개발동기

확률과 통계 교과 수업에서 코인 토스를 예시로 시행 횟수가 증가하면 통계적 확률과 수학적 확률의 값의 유사도가 상승한다고 들었습니다. 

그래서 직접 해보려고 했으나 변인통제에 문제가 좀 있을 것 같다는 생각이 들어서 ~~(직접하기 귀찮아서)~~ Python으로 개발해서 결과값을 분석해봐겠다는 생각이 들었습니다. 바로 계획을 실행에 옮기게 되었습니다.

# 개발

## 개발정보

- stack(개발 언어): Python 3.12.3
- 기간: 2024.04.25(1일간 진행)
- 참여 인원: 31012 박여웅

## 기획

coin toss 게임의 핵심적인 무작위성은 Python의 PRNG(유사 난수 생성기) 모듈인, random 모듈을 사용해 구현하기로 결정했습니다.

최종적으로 로그까지 남기도록 기획 하였고, 시작하게 되었습니다.

## 개발

최종적으로 코드는 아래와 같습니다.
```python
import random
import datetime

def coin_flip_simulation():
	
	n = int(input("동전을 던질 횟수를 입력하세요: ")) #동전 던질 횟수 입력받아서 n에 저장
	heads_count = 0
	tails_count = 0
	
	time = datetime.datetime.now() # 로그 파일명 중복 방지용 시각 기록
	formatted_time = time.strftime('%Y-%m-%d %H:%M:%S') # 원하는 시각 포맷으로 변경
	
	    with open(f"logs/코인 토스 결과 기록_{formatted_time}.log", "w") as file: #로깅 시작
			for i in range(1, n + 1): # 코인 토스 n 만큼 반복
				flip = random.choice(['앞면', '뒷면']) # random 모듈로 코인 토스 시작
				if flip == '앞면':	
					heads_count += 1
				else:
					tails_count += 1
				file.write(f"{i}번째 던짐: {flip}\n") # 코인 토스 회차와 결과 로깅
				print(f"{i}번째 던짐: {flip}\n") # 코인 토스 회차와 결과 출력

			empirical_probability_heads = heads_count / n # 앞면 확률 계산
			empirical_probability_tails = tails_count / n # 뒷면 확률 계산

			file.write(f"통계적 확률 (앞면): {empirical_probability_heads:.5f} / 수학적 확률: 0.500000\n") # 앞면 확률 로깅
			file.write(f"통계적 확률 (뒷면): {empirical_probability_tails:.5f} / 수학적 확률: 0.500000\n") # 뒷면 확률 로깅
			print(f"통계적 확률 (앞면): {empirical_probability_heads:.5f} / 수학적 확률: 0.500000\n") # 앞면 결과 출력
			print(f"통계적 확률 (뒷면): {empirical_probability_tails:.5f} / 수학적 확률: 0.500000\n") # 뒷면 결과 출력

# 시뮬레이션 시작
if __name__ == '__main__':
coin_flip_simulation()

```

## 시연영상 및 로그 파일

> 로그 파일은 현재 용량이 매우 커서 열리지 않거나 느리게 열릴 수 있습니다. ~~텍스트 파일인데.. 자그마치 2.1GB....~~

https://url.zerocoke.kr/cointoss

# 느낀점

> 생각보다 너무 재미있었고, 처음으로 컴퓨터가 죽는 모습을 볼 수 있어서 흥미로웠습니다. 
> 100,000,000번 돌리다가 실패하고, 50,000,000번 돌릴 때, 근접한 값인 0.4099, 0.5011 수치가 나와서 흥미로웠고 보람찼습니다.
> 생각보다 프로그램을 잘짠것 같아서 저의 소프트웨어 개발 역량이 이전보다 높아진 것 같아 매우 좋았습니다.
> 다음에도 확률과 통계 수업시간에 탐구 해보고 싶은 내용을 탐구하고 싶다는 생각을 가져보게 되는 계기가 되었습니다.