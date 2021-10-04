import java.util.*

// 승률, 이긴횟수, 몸무게, idx
data class Person(val a: Float, val b: Int, val c: Int, val d: Int) : Comparable<Person> {
    override fun compareTo(other: Person) = compareValuesBy(this, other, { it.a * -1 }, { it.b * -1}, {it.c * -1}, {it.d})
}


class SolutionWeek6 {
    fun solution(weights: IntArray, head2head: Array<String>): IntArray {
        var answer = mutableListOf<Int>()
        val pq = PriorityQueue<Person>()

        for(i in weights.indices) {
            var totalCnt = 0
            var winCnt = 0
            var loseCnt = 0
            var weightsCnt = 0
            for(j in weights.indices) {
                when(head2head[i][j]) {
                    'W' -> {
                        totalCnt++
                        winCnt++
                        if(weights[i] < weights[j]) weightsCnt ++

                    }
                    'L' -> {
                        totalCnt++
                        loseCnt++
                    }
                    else -> {}
                }
            }
            val winRating : Float = if (totalCnt == 0) 0f else winCnt.toFloat() / totalCnt.toFloat()
            pq.add(Person(winRating, weightsCnt, weights[i], i+1))
        }

        while (pq.size > 0) {
            answer.add(pq.poll().d)
        }
        return answer.toIntArray()
    }
}

fun main() {

    val weights = intArrayOf(50, 82, 75, 120)
    val h2h = arrayOf("NLWL","WNLL","LWNW","WWLN")
    val sol = SolutionWeek6()
    sol.solution(weights, h2h).forEach { print("$it ") }

}