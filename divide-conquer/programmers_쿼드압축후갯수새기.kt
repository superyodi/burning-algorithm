// 프로그래머스 >> 월간 코드 챌린지 시즌1 >>쿼드압축 후 개수 세기

class Solution {
    lateinit var answer : IntArray
    lateinit var arr : Array<IntArray>
    fun solution(arr: Array<IntArray>): IntArray {
        this.arr = arr
        answer = IntArray(2)
        divide(0, 0, arr.size)

        return answer
    }

    fun divide(x:Int, y:Int, n: Int) {

        val count = conquer(x,y,n)
        if(count != -1) {
            answer[count] ++
            return
        }
        // divide
        val size = n / 2

        divide(x, y, size)
        divide(x+size, y, size)
        divide(x, y+size, size)
        divide(x+size, y+size, size)


    }


    fun conquer(x:Int, y:Int, size: Int) : Int {

        var sumArr = 0
        for(i in x until x+size) {
            for(j in y until y+size) {
                if(arr[i][j] == 1) sumArr ++
            }
        }

        if(sumArr == 0) return 0
        else if (sumArr == size * size) return 1

        return -1
    }

}

