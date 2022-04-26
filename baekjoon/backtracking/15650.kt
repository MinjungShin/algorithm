package baekjoon.backtracking

import java.io.BufferedReader
import java.io.InputStreamReader

private var n = 0
private var m = 0
private var result = mutableListOf<Int>()

private fun dfs(depth: Int) {
    if (result.size == m) {
        val string = result.joinToString(" ") { it.toString() }
        println(string)
        return
    }
    if (depth >= n || result.size > m) return

    for (i in depth + 1..n) {
        result.add(i)
        dfs(i)
        result.removeLast()
    }
}

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val tmp = readLine().split(" ").map { it.toInt() }
    n = tmp[0]
    m = tmp[1]

    dfs(0)
}
