/*
코딩테스트 연습 > 위클리 챌린지 > 부족한 금액 계산하기

https://school.programmers.co.kr/learn/courses/30/lessons/82612
 */

package programmers.lv1

class CalculateInsufficientMoney {
    fun solution(price: Int, money: Int, count: Int): Long {
        var sum = 0L
        for (i in 1..count) {
            sum += price * i.toLong()
        }
        val answer = sum - money

        return if (answer < 0) 0L
        else answer
    }
}