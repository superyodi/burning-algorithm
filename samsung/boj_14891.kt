package samung

import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.pow

lateinit var gears : Array<Array<Int>>
lateinit var informs : IntArray


// 백준: 톱니바퀴 
// https://www.acmicpc.net/problem/14891
fun rotate(dir: Int, gNum: Int) {
    if(dir == 0) return

    // 시계 방향
    val gear = gears[gNum].toMutableList()
    if(dir == 1) {
        val tmp = gear.removeAt(7)
        gear.add(0, tmp)

    }
    // 반 시계 방향
    else {
        val tmp = gear.removeAt(0)
        gear.add(tmp)
    }
    gears[gNum] = gear.toTypedArray()

}

fun check(n: Int, dir: Int) {
    informs[n] = dir
    // 왼쪽
    var j = n-1
    var value = gears[n][6]
    var ndir = dir

    while(j >= 0) {
        if(gears[j][2] != value) {
            ndir *= -1
            informs[j] = ndir
            value = gears[j][6]
            j --
        }
        else break
    }
    j = n+1
    value = gears[n][2]
    ndir = dir

    // 오른쪽
    while(j < 4) {
        if(gears[j][6] != value) {
            ndir *= -1
            informs[j] = ndir
            value = gears[j][2]
            j ++
        }
        else break
    }
}


fun main() {

    var br = BufferedReader(InputStreamReader(System.`in`))
    gears = Array(4) { Array(8) { 0 } }


    for (i in 0 until 4) {
        gears[i] = br.readLine().toList().map {
            it.toString().toInt()
        }.toTypedArray()
    }

    val K = br.readLine().toInt()

    for (k in 0 until K) {
        informs = IntArray(4) {0}
        val input = br.readLine().split(" ")
        val gearNum = input[0].toInt() - 1
        val dir = input[1].toInt()

        check(gearNum, dir)

        for(i in 0 until 4) {
            rotate(informs[i], i)
        }
//        println(informs.contentToString())
//        println(gears.contentDeepToString())

    }

    var sum = 0
    for (i in 0 until 4) {
        if(gears[i][0] == 1) {
            sum += 2.0.pow(i.toDouble()).toInt()
        }
    }

    println(sum)

}








