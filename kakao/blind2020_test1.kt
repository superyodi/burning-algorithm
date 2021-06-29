package kakao

import java.lang.StringBuilder
import kotlin.math.min

class Solution {
    fun slice(s: String, n: Int) : String {
        var before  = ""; var cnt  = 1
        val newStr = StringBuilder()

        for(i in s.indices step n) {
            if(i+n <= s.length) {
                var now = s.substring(i until i + n)
                if(now == before) {
                    cnt += 1
                }
                else{
                    if(cnt != 1) {
                        newStr.append(cnt.toString())
                        newStr.append(before)
                        cnt = 1
                    }
                    else newStr.append(before)
                }
                before = now
            }
            else {
                if(cnt != 1) {
                    newStr.append(cnt.toString())
                    newStr.append(before)
                    cnt = 1
                }
                else newStr.append(before)

                newStr.append(s.substring(i, s.length))
                cnt = 0
            }
        }

        if(cnt == 1) newStr.append(before)

        else if(cnt > 1) {
            newStr.append(cnt.toString())
            newStr.append(before)
        }
        return newStr.toString()
    }

    fun solution(s: String): Int {
        if(s.length < 2) return s.length
        var minCount = s.length

        for(len in s.length/2 downTo 1) {
            val newStr = slice(s, len)
            minCount = min(minCount, newStr.length)
//            println("$newStr, ${newStr.length}")
        }
//        println(minCount)
        return minCount
    }
}
fun main() {
    val s = Solution()
    s.solution("aabbaccc")
    s.solution("ababcdcdababcdcd")
    s.solution("abcabcdede")
    s.solution("abcabcabcabcdededededede")
    s.solution("xababcdcdababcdcd")
}
