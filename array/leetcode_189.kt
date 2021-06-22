package problem_solving

class Solution189 {
    fun rotate(nums: IntArray, k: Int): Unit {
        val tmp = IntArray(nums.size)
        val n = nums.size
        for(i in nums.indices) {

            tmp[(i+k)%n] = nums[i]
        }

        for(i in nums.indices) {
            nums[i] = tmp[i]
        }


    }
}
