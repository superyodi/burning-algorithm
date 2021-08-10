import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Integer.*


// 백준 - 가장 큰 정사각형

var N = 0
var M = 0

lateinit var dp : Array<IntArray>

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {

    readLine().split(" ").let {
        N = it[0].toInt()
        M = it[1].toInt()
    }
    dp = Array(N) { IntArray(M) { 0} }

    for(i in 0 until N) {
        readLine().toString()
                .toList()
                .map{
                    it.toInt() - 48
                }.let {
                    dp[i] = it.toIntArray()
                }
    }
    var maxVal = 0

    if(N == 1 || M == 1) {
        dp.forEach {
            maxVal += it.sum()
        }
        if(maxVal == 0) println("0")
        else println("1")
    }

    else {
        maxVal = if(dp[0][0] + dp[0][1] + dp[1][0] == 0) 0 else 1
        for(x in 1 until N)
            for(y in 1 until M) {
                if(dp[x][y] != 0) {
                    dp[x][y] = min(dp[x-1][y-1], min(dp[x-1][y], dp[x][y-1])) + 1
                    maxVal = max(dp[x][y], maxVal)
                }
            }
        println(maxVal * maxVal)
    }




}



/*

4 4
0100
0111
1111
1110

4 4
1111
0111
1110
0010

4 4
0000
0000
0000
0000

4 4
1111
1111
0000
0000


 */