package baekjoon.disjoint_set

import java.io.BufferedReader
import java.io.File
import java.io.InputStreamReader

private val file = File("input.txt")
private var parent = mutableListOf<Int>()

fun main() = with(BufferedReader(InputStreamReader(file.inputStream()))) {
    val n = readLine().toInt()
    val m = readLine().toInt()

    parent = MutableList(n + 1) { it }

    for (i in 0 until n) {
        val map = readLine().split(" ").map { it.toInt() }
        for (j in map.indices) { // 한줄씩 돌면서 연결된 경우(1인 경우)는 union 실행
            if (map[j] == 1) union(i + 1, j + 1)
        }
    }

    val plan = readLine().split(" ").map { it.toInt() }
    val result = mutableSetOf<Int>()
    for (x in plan) { // 각 도시의 루트 찾아서 set에 추가
        result.add(find(x))
    }
    if (result.size == 1) println("YES")
    else println("NO")
}

private fun find(x: Int): Int {
    if (x == parent[x]) return x
    parent[x] = find(parent[x])
    return parent[x]
}

private fun union(x: Int, y: Int) {
    val a = find(x)
    val b = find(y)

    if (a == b) return
    else parent[a] = b
}