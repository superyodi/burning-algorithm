// 평범한 배낭

import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Integer.max


fun main() {

    val br =  BufferedReader(InputStreamReader(System.`in`))
    var N = 0
    var K = 0

    br.readLine().split(' ').let { it ->
        N = it[0].toInt()
        K = it[1].toInt()
    }
    var ans = 0
    val W = IntArray(N)
    val V = IntArray(N)
    val dp = Array (2) {Array(K+1) {0} }
    for (i in 0 until N) {

        br.readLine().split(' ').let { it ->
            W[i] = it[0].toInt()
            V[i] = it[1].toInt()
        }

        for (limit in W[i] .. K) {
            dp[1][limit] =  max(dp[0][limit], dp[0][limit - W[i]] + V[i])
        }

        for ( w in W[i] .. K) {
            dp[0][w] = dp[1][w]
        }
    }

    print(dp[1][K])
}

/*
10 999
46 306
60 311
33 724
18 342
57 431
49 288
12 686
89 389
82 889
16 289
 */