/*
코딩테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 네트워크

https://school.programmers.co.kr/learn/courses/30/lessons/43162
 */
package programmers

class Network {
    lateinit var graph: Array<MutableList<Int>>
    lateinit var visited: IntArray
    var result = 0

    fun solution(n: Int, computers: Array<IntArray>): Int {
        graph = Array(n + 1) { mutableListOf() }
        visited = IntArray(n + 1) { 0 }
        for (i in computers.indices) {
            for (j in computers[i].indices) {
                if (i == j) continue
                if (computers[i][j] == 1)
                    graph[i + 1].add(j + 1)
            }
        }

        for (i in 1..n) {
            if (visited[i] != 0) continue
            result += 1
            dfs(i)
        }
        return result
    }

    private fun dfs(x: Int) {
        for (y in graph[x]) {
            if (visited[y] == 0) {
                visited[y] = 1
                dfs(y)
            }
        }
    }
}