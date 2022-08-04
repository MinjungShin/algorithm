/*
1005. ACM Craft

https://www.acmicpc.net/problem/1005
 */
package baekjoon.topological_sorting

import java.io.BufferedReader
import java.io.FileInputStream
import java.io.InputStreamReader
import java.lang.Math.max
import java.util.*

private var n = 0
private var k = 0
private lateinit var times: List<Int>
private lateinit var graph: Array<MutableList<Int>>
private lateinit var indegree: IntArray
private lateinit var results: IntArray
private fun main() = with(BufferedReader(InputStreamReader(FileInputStream("input.txt")))) {
    var st = StringTokenizer(readLine(), " ")
    val T = st.nextToken().toInt()
    for (t in 1..T) {
        st = StringTokenizer(readLine(), " ")
        n = st.nextToken().toInt()
        k = st.nextToken().toInt()
        times = readLine().split(" ").map { it.toInt() }

        graph = Array(n + 1) { mutableListOf() }
        indegree = IntArray(n + 1) { 0 }
        results = IntArray(n + 1) { 0 }
        for (i in 0 until k) {
            st = StringTokenizer(readLine(), " ")
            val pre = st.nextToken().toInt()
            val post = st.nextToken().toInt()
            graph[pre].add(post)
            indegree[post]++
        }
        val w = readLine().toInt()
        solution()
        println(results[w])
    }
}

private fun solution() {
    val queue = LinkedList<Int>()
    for (i in 1..n) {
        if (indegree[i] == 0) queue.offer(i)
    }

    while (queue.isNotEmpty()) {
        val cur = queue.pop()
        results[cur] += times[cur - 1]
        for (x in graph[cur]) {
            indegree[x]--
            results[x] = max(results[x], results[cur])
            if (indegree[x] == 0) queue.offer(x)
        }
    }
}

