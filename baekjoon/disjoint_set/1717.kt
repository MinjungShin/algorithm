package baekjoon.disjoint_set

import java.io.BufferedReader
import java.io.File
import java.io.InputStreamReader

private val file = File("input.txt")
private var parent = mutableListOf<Int>()

fun main() = with(BufferedReader(InputStreamReader(file.inputStream()))) {
    val (n, m) = readLine().split(" ").map { it.toInt() }

    parent = MutableList(n + 1) { it }

    for (i in 0 until m) {
        val (a, b, c) = readLine().split(" ").map { it.toInt() }
        if (a == 1) {
            if (find(b) == find(c)) println("YES")
            else println("NO")
        } else union(b, c)
    }
}

private fun find(x: Int): Int {
    if (x == parent[x]) return x // x가 루트: 자기 자신 반환
    // x가 루트가 아님: 재귀를 통해 루트 찾기 -> 찾으면서 x의 부모를 find(parent[x])로 바꿔줌(루트 노드 갱신: 효율적)
    parent[x] = find(parent[x])
    return parent[x]
}

private fun union(a: Int, b: Int) {
    val x = find(a) // x의 루트 찾기
    val y = find(b) // y의 루트 찾기

    if (x == y) return // 루트가 같으므로 합칠 필요 없음
    else parent[x] = y // 합치기
}