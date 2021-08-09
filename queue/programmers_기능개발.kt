// 프로그래머스 - 기능개발


import kotlin.math.ceil

class Solution {
    fun solution(progresses: IntArray, speeds: IntArray): IntArray {

        var preTime = -1.0
        var answer = mutableListOf<Int>()
        var cnt = 1

        for(i in progresses.indices ) {
            val p = progresses[i]
            val s = speeds[i]
            val time = ceil((100 - p)/s.toDouble())

            if(preTime == -1.0) {
                preTime = time
                continue
            }

            if(time <= preTime) {
                cnt ++
            }
            else {
                answer.add(cnt)
                cnt = 1
                preTime = time
            }
        }

        answer.add(cnt)
        return answer.toIntArray()
    }
}