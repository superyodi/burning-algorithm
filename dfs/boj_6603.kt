import java.io.BufferedReader
import java.io.InputStreamReader

// 백준 로또

lateinit var nums : IntArray
lateinit var visited : BooleanArray
var k = 0


fun main() {
    val br =  BufferedReader(InputStreamReader(System.`in`))


    while (true) {
        br.readLine()
                .split(' ')
                .map { it.toInt() }
                .let {
                    k = it[0]
                    if(k > 0) nums = it.subList(1, it.size).toIntArray()
                }
        if(k==0) break
        visited = BooleanArray(k) { false}

        combi(-1, 0,"")
        println()

    }
}

fun combi(idx : Int, size : Int, lotto : String) {
    if(size == 6) {
        println(lotto)
        return
    }
    for(i in idx+1 until k) {
        if(!visited[i]) {
            visited[i] = true
            combi(i, size+1, lotto+"${nums[i]} ")
            visited[i] = false
        }
    }
}
