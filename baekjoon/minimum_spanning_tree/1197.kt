package baekjoon.minimum_spanning_tree

import java.io.BufferedReader
import java.io.File
import java.io.InputStreamReader

private val file = File("input.txt")
private var parent = mutableListOf<Int>()
private var edges = mutableListOf<List<Int>>()
private var result = 0

fun main() = with(BufferedReader(InputStreamReader(file.inputStream()))) {
    val (v, e) = readLine().split(" ").map { it.toInt() }
    parent = MutableList(v + 1) { it } // 부모를 자기 자신으로 초기화

    for (i in 0 until e) {
        edges.add(readLine().split(" ").map { it.toInt() })
    }
    edges.sortBy { it[2] } // 가중치를 기준으로 오름차순 정렬

    for (x in edges) { // x[0]: 정점 1, x[1]: 정점 2, x[2]: 가중치
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