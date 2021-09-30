

import java.io.BufferedReader
import java.io.InputStreamReader

// (stack) 백준 스택
val stack = mutableListOf<Int>()
var size = 0
fun main() {
    var br = BufferedReader(InputStreamReader(System.`in`))
    val N = br.readLine().toInt()

    for (i in 1..N) {
        val cmd = br.readLine().split(' ').toList()
        if (cmd.size == 2) {
            // push
            push(cmd[1].toInt())
        }
        else {
            when (cmd[0]) {
                "pop" -> {
                    println(pop())

                }
                "size" -> {
                    println(size)
                }
                "empty" -> {
                    if(empty()) println(1)
                    else println(0)

                }
                "top" -> {
                    if(empty()) println(-1)
                    else println(top())

                }
            }
        }
    }
}
fun push(el : Int) {
    stack.add(el)
    size++

}
fun empty() : Boolean {
    if (size == 0) {
        return true
    }
    return false
}
fun pop() : Int {
    if(!empty()) {
        val ele = stack.removeAt(size-1)
        size--
        return ele

    }
    return -1
}
fun top() : Int {
    return stack[size-1]
}


