/*
선수과목 (Prerequisite)
https://www.acmicpc.net/problem/14567
위상정렬
 */

package baekjoon.topological_sorting

import java.io.BufferedReader
import java.io.File
import java.io.InputStreamReader
import java.util.*

private val file = File("input.txt")
private var n = -1
private var m = -1
private lateinit var graph: MutableList<MutableList<Int>>
private lateinit var inDegree: IntArray

private fun main() = with(BufferedReader(InputStreamReader(file.inputStream()))) {
    var st = StringTokenizer(readLine(), " ")
    n = st.nextToken().toInt()
    m = st.nextToken().toInt()
    graph = MutableList(n + 1) { mutableListOf() }
    inDegree = IntArray(n + 1) { 0 }

    for (i in 0 until m) {
        st = StringTokenizer(readLine(), " ")
        val pre = st.nextToken().toInt()
        val post = st.nextToken().toInt()
        graph[pre].add(post)
        inDegree[post] += 1
    }

    val result = solution()
    for (i in 1..n) {
        print("${result[i]} ")
    }
}

private fun solution(): IntArray {
    val result = IntArray(n + 1) { 1 }
    val queue = LinkedList<Int>()

    for (i in 1..n) {
        if (inDegree[i] == 0) queue.add(i)
    }

    while (queue.isNotEmpty()) {
        val current = queue.pop()
        for (x in graph[current]) {
            result[x] = result[current] + 1
            if (--inDegree[x] == 0) queue.add(x)
        }
    }
    return result
}