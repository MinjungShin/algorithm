package baekjoon.divide_and_conquer

import java.io.BufferedReader
import java.io.File
import java.io.InputStreamReader

private val file = File("input.txt").inputStream()
private var n = 0
private var arr = mutableListOf<List<Int>>()

private fun solution(x: Int, y: Int, n: Int): Int {
    val mid = n / 2
    if (n == 2) {
        var result = listOf(arr[x][y], arr[x + 1][y], arr[x][y + 1], arr[x + 1][y + 1])
        result = result.sortedDescending()
        return result[1]
    }

    val a = solution(x, y, mid)
    val b = solution(x + mid, y, mid)
    val c = solution(x, y + mid, mid)
    val d = solution(x + mid, y + mid, mid)
    var result = listOf(a, b, c, d)
    result = result.sortedDescending()
    return result[1]
}

fun main() = with(BufferedReader(InputStreamReader(file))) {
    n = readLine().toInt()
    for (i in 0 until n) {
        val tmp = readLine().split(" ").map { it.toInt() }
        arr.add(tmp)
    }

    print(solution(0, 0, n))
}
