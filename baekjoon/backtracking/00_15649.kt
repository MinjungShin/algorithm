package baekjoon.backtracking

import java.io.BufferedReader
import java.io.InputStreamReader

private var n = 0
private var m = 0
private var visited = mutableListOf<Int>()
private var result = mutableListOf<Int>()

fun dfs(depth: Int) {
    if (depth == m) {
        println(result.joinToString(" "))
        return
    }
    if (depth >= n || result.size > m) return

    for (i in 1..n) {
        if (visited[i] == 0) {
            visited[i] = 1
            result.add(i)
            dfs(depth + 1)
            visited[i] = 0
            result.removeLast()
        }
    }
}

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val tmp = readLine().split(" ").map { it.toInt() }
    n = tmp[0]
    m = tmp[1]
    visited = MutableList(n + 1) { 0 }

    dfs(0)
}


