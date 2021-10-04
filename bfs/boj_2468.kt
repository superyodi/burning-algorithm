package ps1001

import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Integer.max
import java.util.*

// ps1001.bfs
// 백준 안전영역

lateinit var arr : Array<IntArray>
lateinit var visited : Array<BooleanArray>
var N = 0
var minVal = 0
var maxVal = 100
var res = 0


fun main() {
    val br =  BufferedReader(InputStreamReader(System.`in`))
    N = br.readLine().toInt()

    arr = Array(N) { IntArray(N) {0} }
    visited = Array(N) { BooleanArray(N) {false} }


    for (i in 0 until N) {
        val line = br.readLine().split(' ')
        for(j in 0 until N) {
            arr[i][j] = line[j].toInt()

        }
    }

    for(h in minVal..maxVal) {
        val tmp = search(h)
        res = max(res, tmp)

    }

    println(res)


}


fun bfs(r : Int, c : Int, h : Int) {
    val queue : Queue<Pair<Int, Int>> = LinkedList()
    val dirs = arrayOf(arrayOf(0,1), arrayOf(0,-1),arrayOf(1,0),arrayOf(-1,0))
    queue.offer(Pair(r,c))

    while (queue.size > 0) {
        var r = 0; var c = 0
        queue.poll().apply {
            r = first
            c = second
        }
        if(visited[r][c]) continue
        visited[r][c] = true

        for(dir in dirs) {
            val nr = r + dir[0]
            val nc = c + dir[1]

            if(nr in 0 until N && nc in 0 until N) {
                if(!visited[nr][nc] && arr[nr][nc] > h) {
                    queue.offer(Pair(nr, nc))
                }
            }
        }

    }

}

fun search(h : Int) : Int{
    var cnt = 0
    visited = Array(N) { BooleanArray(N) {false} }

    for(i in 0 until N) {
        for(j in 0 until N) {
            if(!visited[i][j] && arr[i][j] > h) {
                cnt++
                bfs(i, j, h)
            }
        }
    }
    return cnt

}


/*
5
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
 */