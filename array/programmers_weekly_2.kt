import java.lang.Integer.min
import java.lang.Math.max
import java.lang.StringBuilder

class Solution {
    lateinit var scores: Array<IntArray>
    fun solution(scores: Array<IntArray>): String {
        var answer: String = ""
        this.scores = reverseTable(scores)
        answer = calGrade()

        return answer
    }

    fun reverseTable(inTable: Array<IntArray>): Array<IntArray> {
        val outTable : Array<IntArray> = Array(inTable.size) { IntArray(inTable[0].size)  }

        for (i in outTable.indices) {
            for (j in outTable[0].indices) {
                outTable[j][i] = inTable[i][j]
            }
        }

        return outTable
    }

    fun calGrade() : String{

        val sb = StringBuilder()

        for (i in scores.indices) {
            var minVal = 100
            var maxVal = 0
            var sumVal = 0
            for (j in scores[0].indices) {
                if (j == i) continue
                minVal = min(minVal, scores[i][j])
                maxVal = max(maxVal, scores[i][j])
                sumVal += scores[i][j]
            }
            var avg = 0
            var size = scores.size

            if (scores[i][i] < minVal || scores[i][i] > maxVal) {
                avg = sumVal / --size

            }
            else {
                sumVal += scores[i][i]
                avg = sumVal / size
            }
            sb.append(convert2grade(avg))
        }

        return sb.toString()

    }

    fun convert2grade(score: Int): String = when (score) {
        in 0 until 50 -> "F"
        in 50 until 70 -> "D"
        in 70 until 80 -> "C"
        in 80 until 90 -> "B"
        else -> "A"

    }
}
