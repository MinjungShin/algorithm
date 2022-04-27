package baekjoon.divide_and_conquer

import java.io.BufferedReader
import java.io.File
import java.io.InputStreamReader

private val file = File("input.txt").inputStream()
private var n = 0
private var arr = mutableListOf<List<Int>>()
private var result = mutableListOf<Int>()

private fun solution(x: Int, y: Int, n: Int) {
    val tmp = arr[x][y]

    for (i in x until x + n) {
        for (j in y until y + n) {
            if (arr[i][j] != tmp) {
                solution(x, y, n / 2)
                solution(x, y + n / 2, n / 2)
                solution(x + n / 2, y, n / 2)
                solution(x + n / 2, y + n / 2, n / 2)
                return
            }
        }
    }

    if (tmp == 0) result.add(0)
    else result.add(1)
}

fun main() = with(BufferedReader(InputStreamReader(file))) {
    n = readLine().toInt()
    for (i in 0 until n) {
        val tmp = readLine().split(" ").map { it.toInt() }
        arr.add(tmp)
    }

    solution(0, 0, n)
    println(result.count { it == 0 })
    print(result.count { it == 1 })
}
