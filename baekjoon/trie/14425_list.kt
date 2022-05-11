package baekjoon.trie

import java.io.BufferedReader
import java.io.File
import java.io.InputStreamReader

private val file = File("input.txt")

private fun main() = with(BufferedReader(InputStreamReader(file.inputStream()))) {
    val (n, m) = readLine().split(" ").map { it.toInt() }
    val s = mutableListOf<String>()
    for (i in 0 until n) {
        s.add(readLine())
    }

    var result = 0
    for(i in 0 until m) {
        if (s.contains(readLine())) result += 1
    }
    println(result)
}