package baekjoon.prefix_sum

import java.io.BufferedReader
import java.io.File
import java.io.InputStreamReader

private val file = File("input.txt").inputStream()
private var n = 0
private var m = 0
private var arr = mutableListOf<List<Int>>()
private var cnt = 0

private fun solution(i: Int, j: Int, x: Int, y: Int, sum: Array<Array<Int>>): Int {
    return sum[x][y] - sum[i - 1][y] - sum[x][j - 1] + sum[i - 1][j - 1]
}

fun main() = with(BufferedReader(InputStreamReader(file))) {
    val tmp = readLine().split(" ").map { it.toInt() }
    n = tmp[0]
    m = tmp[1]

    arr.add(List(m + 1) { 0 })
    for (i in 0 until n) {
        val tmp1 = mutableListOf(0)
        val tmp = readLine().split(" ").map { it.toInt() }.toMutableList()
        tmp1 += tmp
        arr.add(tmp1)
    }

    val sum = Array(n + 1) { Array(m + 1) { 0 } }

    for (i in 1..n) {
        for (j in 1..m) {
            sum[i][j] = arr[i][j] + sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1]
        }
    }

    cnt = readLine().toInt()
    for (k in 0 until cnt) {
        val (i, j, x, y) = readLine().split(" ").map { it.toInt() }
        println(solution(i, j, x, y, sum))
    }
}
