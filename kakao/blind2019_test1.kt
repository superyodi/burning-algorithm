package kakao


class Solution {
    fun solution(record: Array<String>): Array<String> {
        var answer = mutableListOf<String>()

        // 1. dict { id : nick }
        // 2. 문자열 처리

        val userMap = mutableMapOf<String, String>()
        val dataList = mutableListOf<List<String>>()

        for(i in record.indices) {
            val arr = record[i].split(' ')
            when(arr[0]) {
                "Enter" -> {
                    userMap[arr[1]] = arr[2]
                    val data = listOf<String>(arr[1] ,"님이 들어왔습니다." )
                    dataList.add(data)
                }
                "Change" -> {
                    userMap[arr[1]] = arr[2]
                }
                "Leave" -> {
                    val data = listOf<String>(arr[1] ,"님이 나갔습니다." )
                    dataList.add(data)
                }
            }
        }

        for(data in dataList) {
            val name = userMap[data[0]]
            val str = name + data[1]
            println(str)
            answer.add(str)
        }

        return answer.toTypedArray()
    }
}

fun main() {
    val sol = Solution()
    sol.solution(listOf<String>("Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan").toTypedArray())
}