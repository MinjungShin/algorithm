package baekjoon.trie

import java.io.BufferedReader
import java.io.File
import java.io.InputStreamReader

private val file = File("input.txt")

private fun main() = with(BufferedReader(InputStreamReader(file.inputStream()))) {
    val words = readLines()
    val map = mutableMapOf<String, Int>()

    words.forEach {
        if (map.containsKey(it)) {
            map[it] = map[it]?.plus(1) ?: return@forEach
        } else {
            map[it] = 1
        }
    }
    val sortedMap = map.toSortedMap()

    sortedMap.forEach {
        val result = it.value / words.size.toFloat() * 100
        println("${it.key} ${String.format("%.4f", result)}")
    }
}