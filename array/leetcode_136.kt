package problem_solving

import java.util.*

internal class Solution136 {
    fun singleNNumber(nums: IntArray) : Int {

        val hash_table = HashMap<Int, Int>()
        for (i in nums) {
            hash_table[i] = hash_table.getOrDefault(i, 0) + 1
        }

        for (n in nums) {
            if (hash_table[n] == 1) {
                return n
            }
        }
        return 0
    }
}


// 덧
/*
class Solution {
    fun singleNumber(nums: IntArray): Int {

        return 2 * nums.toSet().sum() - nums.sum()
    }
}

 */