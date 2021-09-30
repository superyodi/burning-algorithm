

import java.io.BufferedReader
import java.io.InputStreamReader


// 백준 설탕배달
lateinit var dp : Array<Int>
var N = 0


fun main() {
    var br = BufferedReader(InputStreamReader(System.`in`))
    N = br.readLine().toInt()
    dp = Array(N +1) { N }


    recur(0, 0)
    if(dp[N] == N) println(-1)
    else println(dp[N])

}

fun recur(total: Int, cnt: Int) {
    if(total > N) return
    if(dp[total] <= cnt) return
    dp[total] = cnt
    if(total == N) return

    recur(total + 5, cnt + 1)
    recur(total + 3, cnt + 1)
}