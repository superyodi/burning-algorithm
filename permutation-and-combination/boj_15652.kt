
import java.lang.StringBuilder
import java.util.*

// 백준 - N과 M
var N = 0
var M =0
var sb = StringBuilder()
lateinit var nums: IntArray

fun main() {
    val line = StringTokenizer(readLine())
    N = line.nextToken().toInt()
    M = line.nextToken().toInt()
    nums = IntArray(M)

    combination(0, 1)
    print(sb)
}

fun combination(depth: Int, start : Int) {
    if (depth == M) {
        nums.forEach {
            sb.append("$it ")
        }
        sb.append('\n')
        return
    }

    for (num in start..N) {
        nums[depth] = num
        combination(depth+1, num)
    }
}
