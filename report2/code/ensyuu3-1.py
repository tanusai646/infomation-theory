#222C1021 今村優希
#情報理論 計算機演習2

#演習3-1 互いに異なる素数を求めるプログラム
#演習3-2 実行時間の計測

import time



pq = input("pq:")
pq = int(pq)


start = time.perf_counter_ns()     #現在時刻の取得(開始)

for i in range(2, pq):
    if pq % i == 0:
        p = i
        q = int(pq / i)
        break

end = time.perf_counter_ns()       #現在時刻の取得(終了)

time_diff = end - start


print("pq =",pq)
print("p", p)
print("q", q)
print("Execution time is",time_diff/1000000000)
