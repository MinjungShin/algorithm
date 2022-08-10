/*
11656. 접미사 배열

https://www.acmicpc.net/problem/11656
 */

package baekjoon

import java.io.BufferedReader
import java.io.FileInputStream
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(FileInputStream("input.txt")))) {
    val string = readLine()
    val array = Array(string.length) { "" }

    string.forEachIndexed { idx, _ ->
        array[idx] = string.substring(idx)
    }

    array.sort()
    array.forEach {
        println(it)
    }
}