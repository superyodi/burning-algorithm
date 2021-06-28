package string




class Solution {
    fun solution(s: String): Int {
        var cnt = 0

        // generate
        var arr = s.toMutableList()

        for(i in s.indices) {
            val ch = arr.removeAt(0)
            arr.add(ch)
            arr.forEach{
                println(it)
            }

            if(check(arr)) cnt++
        }

        return cnt
    }



    // check
    fun check(arr: MutableList<Char>): Boolean {

        var stack = mutableListOf<Char>()


        for(i in arr.indices) {
            when(arr[i]) {
                '}' -> {
                    if (stack.size == 0) return false
                    if (stack[stack.size - 1] == '{') {
                        stack.removeAt(stack.size - 1)
                    } else stack.add(arr[i])
                }
                ']' -> {
                    if (stack.size == 0) return false
                    if (stack[stack.size - 1] == '[') {
                        stack.removeAt(stack.size - 1)
                    } else stack.add(arr[i])
                }
                ')' -> {
                    if (stack.size == 0) return false
                    if (stack[stack.size - 1] == '(') {
                        stack.removeAt(stack.size - 1)
                    } else stack.add(arr[i])
                }
                else -> stack.add(arr[i])
            }

        }
        if(stack.size == 0) return true
        return false
    }
}