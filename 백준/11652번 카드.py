N = int(input())
nums = []
new_nums = []

# 숫자 입력 받기
for i in range(N):
    num = int(input())
    nums.append(num)

# 리스트 정렬
nums.sort()

# 첫 번째 숫자 초기화
cnt = 1  # 첫 숫자를 포함해서 시작
for i in range(1, N):
    if nums[i] == nums[i-1]:
        # 현재 숫자가 이전 숫자와 같다면 카운트 증가
        cnt += 1
    else:
        # 현재 숫자가 이전 숫자와 다르면 new_nums에 추가하고 카운트 초기화
        new_nums.append((cnt, nums[i-1]))
        cnt = 1  # 새로운 숫자 카운트 시작

# 마지막 숫자도 추가
new_nums.append((cnt, nums[-1]))

# 개수가 가장 큰 값을 찾고, 동일한 경우 작은 숫자를 선택
new_nums.sort(key=lambda x: (-x[0], x[1]))
print(new_nums[0][1])  # 가장 많이 등장한 숫자 출력
