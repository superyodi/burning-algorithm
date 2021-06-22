package problem_solving

class Solution01 {
    fun twoSum(nums: IntArray, target: Int): IntArray {

        val numMap = mutableMapOf<Int, Int>()

        for (i in nums.indices) {
            numMap[nums[i]] = i
        }

        for (i in nums.indices) {
            if(numMap.contains(target-nums[i])) {
                if(numMap[target-nums[i]] != i) return intArrayOf(i, numMap[target-nums[i]]!!)
            }
        }

        return IntArray(5, {0})


    }
}
