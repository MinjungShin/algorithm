package baekjoon.minimum_spanning_tree

import java.io.BufferedReader
import java.io.File
import java.io.InputStreamReader

private val file = File("input.txt")
private var parent = mutableListOf<Int>()
private var edges = mutableListOf<List<Int>>()
private var result = 0

fun main() = with(BufferedReader(InputStreamReader(file.inputStream()))) {
    val computerCnt = readLine().toInt()
    val lineCnt = readLine().toInt()
    parent = MutableList(computerCnt + 1) { it }

    for (x in 0 until lineCnt) {
        edges.add(readLine().split(" ").map { it.toInt() })
    }

    edges.sortBy { it[2] }

    for (x in edges) {
        if (find(x[0]) != find(x[1])) {
            union(x[0], x[1])
            result += x[2]
        }
    }
    println(result)
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