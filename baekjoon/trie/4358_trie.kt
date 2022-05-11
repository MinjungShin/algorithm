package baekjoon.trie

import java.io.BufferedReader
import java.io.File
import java.io.InputStreamReader

private val file = File("input.txt")

private fun main() = with(BufferedReader(InputStreamReader(file.inputStream()))) {

    class Node(var childNode: MutableMap<Char, Node> = mutableMapOf(), var cnt: Int = 0)

    class Trie(var root: Node = Node()) {

        fun insert(x: String) {
            var head = root
            for(ch in x) {
                if (head.childNode.containsKey(ch).not()) head.childNode[ch] = Node()
                head = head.childNode[ch] ?: return
            }
            head.cnt += 1
        }

        fun getCnt(x: String): Int {
            var head = root
            for(ch in x) {
                if (head.childNode.containsKey(ch)) head = head.childNode[ch] ?: return 0
                else return 0
            }
            return head.cnt
        }
    }

    val trie = Trie()
    val words = readLines()
    words.forEach {
        trie.insert(it)
    }

    val sortedDistinctWords = words.distinct().sorted()
    sortedDistinctWords.forEach {
        val cnt = trie.getCnt(it)
        val result = cnt / words.size.toFloat() * 100
        println("$it ${String.format("%.4f", result)}")
    }
}
