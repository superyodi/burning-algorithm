package sort

class Solution {
    fun solution(citations: IntArray): Int {
        var answer = 0
        citations.sortDescending()
        val n = citations.size

        if(citations[0] == 0) return 0

        for(i in citations.indices) {
            if (i+1 >= citations[i]) {
                return maxOf(i, citations[i])
            }
        }

        if(citations[0] >= n) return n
        return 0
    }
}