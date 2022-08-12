/*
코딩테스트 연습 > 2019 KAKAO BLIND RECRUITMENT > 실패율

https://school.programmers.co.kr/learn/courses/30/lessons/42889
 */

package programmers.lv1

class FailureRate {
    fun solution(N: Int, stages: IntArray): IntArray {
        var people = stages.size
        val cntList = IntArray(N) { 0 }
        val failList = Array(N) { Failure(0, 0.0) }
        for (i in stages.indices) {
            if (stages[i] > N) continue
            cntList[stages[i] - 1]++
        }
        cntList.forEachIndexed { idx, x ->
            val rate = if (people == 0) 0.0
            else x.toDouble() / people.toDouble()

            failList[idx] = Failure(idx + 1, rate)
            people -= x
        }
        failList.sort()

        return failList.map { it.stage }.toIntArray()
    }

    data class Failure(
        val stage: Int,
        val rate: Double
    ) : Comparable<Failure> {
        override fun compareTo(other: Failure): Int {
            val diff = other.rate - this.rate
            when {
                diff == 0.0 -> return this.stage - other.stage
                diff > 0.0 -> return 1
                diff < 0.0 -> return -1
            }
            return 0
        }
    }
}
