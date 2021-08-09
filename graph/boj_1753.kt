// 백준 - 최단거리

// 다익스트라(우선순위 큐, 인접리스트)

import java.io.*
import java.lang.Integer.min
import java.util.*

class Node(var num: Int, var weight: Int) : Comparable<Node>  {
    override operator fun compareTo(other: Node): Int {
        return weight - other.weight
    }

}

val bf = BufferedReader(InputStreamReader(System.`in`))
const val INF = Integer.MAX_VALUE
var N = 0
var M = 0
var start = 0

private lateinit var graph: Array<MutableList<Node>>
private lateinit var distance: IntArray



fun main() {
    bf.readLine().split(" ").let{
        N = it[0].toInt()
        M = it[1].toInt()
    }
    start = bf.readLine().toInt()
    distance = IntArray(N+1) {INF}


    graph = Array(N + 1){ mutableListOf<Node>()}

    for (i in 1..N) {
        graph[i] = ArrayList()
    }

    for (i in 0 until M) {
        val line = bf.readLine()
                .split(' ')
                .map { it.toInt() }
        val u = line[0]; val v = line[1]; val w =line[2]

        graph[u].add(Node(v, w))
        if(u == start) distance[v] = w
    }

    // do dijkstra
    dijkstra()

    // print
    for (i in 1..N) {
        if (distance[i] == INF)
            println("INF")
        else
            println(distance[i])
    }

}

private fun dijkstra() {
    val queue = PriorityQueue<Node>()
    val visited = BooleanArray(N+1){false}
    queue.add(Node(start, 0))
    distance[start] = 0

    while (!queue.isEmpty()) {
        val nowNode = queue.poll()
        val now = nowNode.num

        if (visited[now]) continue
        visited[now] = true

        for (node in graph[now]) {

            if (!visited[node.num]) {
                distance[node.num] = min(distance[node.num], distance[now] + node.weight)
                queue.add(Node(node.num, distance[node.num]))
            }
        }
    }
}