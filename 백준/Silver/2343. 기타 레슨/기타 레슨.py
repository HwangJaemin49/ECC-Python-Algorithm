# 블루레이 크기 중 최소를 출력
# -> 블루레이 크기를 탐색한다
# 블루레이 크기의 최솟값은 받은 원소의 최댓값
# 블루레이 크기의 최댓값은 모든 원소의 합
# 이 범위 내에서 이진 탐색 실행


N, M = map(int, input().split())
times = list(map(int, input().split()))

start = max(times)
end = sum(times)

while(start <= end) :
    mid = (start + end) // 2
    total = 0
    count = 1
    for time in times:
        if (total + time) > mid:
            count += 1
            total = 0
        total += time
    if count <= M:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1
print(ans)

