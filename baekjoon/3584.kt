/*
가장 가까운 공통 조상

https://www.acmicpc.net/problem/3584
 */
package baekjoon

import java.io.BufferedReader
import java.io.FileInputStream
import java.io.InputStreamReader
import java.util.StringTokenizer

private var T = 0
private var n = 0
private lateinit var graph: Array<IntArray>

fun main() = with(BufferedReader(InputStreamReader(FileInputStream("input.txt")))) {
    T = readLine().toInt()
    for (t in 1..T) {
        n = readLine().toInt()
        graph = Array(n + 1) { IntArray(1) }
        for (i in 0 until n - 1) {
            val st = StringTokenizer(readLine())
            val parent = st.nextToken().toInt()
            val child = st.nextToken().toInt()
            graph[child][0] = parent
        }

        val st = StringTokenizer(readLine())
        val node1 = st.nextToken().toInt()
        val node2 = st.nextToken().toInt()
        val commonParentList = mutableListOf<Int>()

        findRoot(node1, commonParentList)
        val result = getRoot(node2, commonParentList)
        println(result)
    }

}

fun findRoot(node: Int, commonParentList: MutableList<Int>) {
    commonParentList.add(node)
    val parent = graph[node][0]
    if (parent != 0) {
        commonParentList.add(parent)
        findRoot(parent, commonParentList)
    }
}

fun getRoot(node: Int, commonParentList: List<Int>): Int {
    val parent = graph[node][0]

    return if (node in commonParentList) node
    else if (parent in commonParentList) parent
    else getRoot(parent, commonParentList)
}