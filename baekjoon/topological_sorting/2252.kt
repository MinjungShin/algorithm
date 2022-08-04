/*
2252. 줄 세우기

https://www.acmicpc.net/problem/2252
 */
package baekjoon.topological_sorting

import java.io.BufferedReader
import java.io.FileInputStream
import java.io.InputStreamReader
import java.util.LinkedList
import java.util.StringTokenizer

private var n = 0
private var m = 0
private lateinit var graph: Array<MutableList<Int>>
private lateinit var indegree: IntArray
private fun main() = with(BufferedReader(InputStreamReader(FileInputStream("input.txt")))) {
    var st = StringTokenizer(readLine(), " ")
    n = st.nextToken().toInt()
    m = st.nextToken().toInt()
    graph = Array(n + 1) { mutableListOf() }
    indegree = IntArray(n + 1) { 0 }

    for (i in 0 until m) {
        st = StringTokenizer(readLine(), " ")
        val pre = st.nextToken().toInt()
        val post = st.nextToken().toInt()
        graph[pre].add(post)
        indegree[post]++
    }
    val result = solution()
    for (x in result) {
        print("$x ")
    }
}

private fun solution(): List<Int> {
    val result = mutableListOf<Int>()
    val queue = LinkedList<Int>()
    for (i in 1..n) {
        if (indegree[i] == 0) queue.offer(i)
    }

    while (queue.isNotEmpty()) {
        val cur = queue.pop()
        result.add(cur)
        for (x in graph[cur]) {
            indegree[x]--
            if (indegree[x] == 0) queue.offer(x)
        }
    }
    return result
}