/*
코딩테스트 연습 > 완전탐색 > 카펫

https://school.programmers.co.kr/learn/courses/30/lessons/42842
 */
package programmers

class Carpet {
    fun solution(brown: Int, yellow: Int): IntArray {
        var answer = intArrayOf()
        for (i in 1..yellow) {
            val j = yellow / i
            if (i * j != yellow) continue

            val cal = (i + 2) * (j + 2) - yellow
            if (cal == brown) {
                answer = intArrayOf(j + 2, i + 2)
                break
            }
        }

        return answer
    }
}
