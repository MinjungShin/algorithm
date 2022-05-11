package baekjoon.trie

import java.io.BufferedReader
import java.io.File
import java.io.InputStreamReader

// 시간초과 나서 확인불가~~

private val file = File("input.txt")

private class Node(var childNode: MutableMap<Char, Node> = hashMapOf(), var isFinished: Boolean = false)

private class Trie(var rootNode: Node = Node()) {

    fun insert(x: String) {
        var root = rootNode

        for(ch in x) {
            if (root.childNode.containsKey(ch).not()) root.childNode[ch] = Node()
            root = root.childNode[ch] ?: return
        }
        root.isFinished = true
    }

    fun search(x: String): Boolean {
        var root = rootNode

        for (ch in x) {
            if (root.childNode.containsKey(ch)) root = root.childNode[ch] ?: return false
            else return false
        }
        return root.isFinished
    }
}

private fun main() = with(BufferedReader(InputStreamReader(file.inputStream()))) {
    val (n, m) = readLine().split(" ").map { it.toInt() }
    val trie = Trie(Node())
    var result = 0

    for (i in 0 until n) {
        val tmp = readLine()
        trie.insert(tmp)
    }
    for (i in 0 until m) {
        val tmp = readLine()
        if (trie.search(tmp)) result += 1
    }

    println(result)
}