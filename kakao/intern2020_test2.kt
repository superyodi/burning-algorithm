package kakao

// 수식 최대화

class Solution2 {
    fun solution(expression: String): Long {
        var answer: Long = 0

        var opndSet = mutableSetOf<String>()
        var expressList = mutableListOf<String>()

        // 1. 문자열 처리
        var num = ""
        for (ele in expression) {
            if (ele == '*' || ele == '-' || ele == '+') {
                opndSet.add(ele.toString())
                expressList.add(num)
                expressList.add(ele.toString())
                num = ""
            } else num += ele
        }
        expressList.add(num)

        // 2. 순열
        val orders = permutation(opndSet.toList())

        // 3. 수식 계산
        var maxNum = 0L

        for (order in orders) {
            maxNum = kotlin.math.max(maxNum, calculate(expressList, order))
        }
        return maxNum
    }

    fun calculate(express: List<String>, order : List<String>) : Long {

        var express = express
        var newExpress = mutableListOf<String>()
        for(opnd in order) {

            var i = 0
            newExpress = mutableListOf<String>()

            while(i < express.size) {
                if(express[i] == "*" || express[i] == "+" || express[i] == "-") {
                    if(express[i] == opnd) {
                        val num1 = newExpress.removeAt(newExpress.size-1).toLong()
                        val num2 = express[i+1].toLong()
                        var cal = 0L

                        when(opnd) {
                            "*" -> cal = num1 * num2
                            "+" -> cal = num1 + num2
                            "-" -> cal = num1 - num2
                        }
                        newExpress.add(cal.toString())
                        i++

                    }
                    else newExpress.add(express[i])
                }
                else newExpress.add(express[i])
                i++
            }
            express = newExpress.toList()
        }
        return kotlin.math.abs(newExpress[0].toLong())
    }

    fun <T> permutation(el: List<T>, fin: List<T> = listOf(), sub: List<T> = el): List<List<T>> {
        return if (sub.isEmpty()) listOf(fin)
        else sub.flatMap { permutation(el, fin + it, sub - it) }
    }
}

fun main() {
    val sol = Solution2()
    sol.solution("100-200*300-500+20")
}