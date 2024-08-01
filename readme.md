# Ôn thi HSG K12 2024-2025

## Tính số Fibonacci
### Cho số n biết F0 = 0, F1 = 1, F2 = F1+F0... Fn=Fn-2+Fn-1: [link code](https://github.com/ianTuG/hsg/blob/main/fibonacci.py)
Input: n là số nguyên dương </br>
Output: giá trị của Fn

## Tìm số Ra-one
## Định nghĩa: Số Ra-one là số mà hiệu của tổng các chữ số ở vị trí chẵn và vị trí lẻ bằng 1: [link code](https://github.com/ianTuG/hsg/blob/main/raone.py)
Input: a, b là 2 số nguyên dương [a, b] (a < b)</br>
Output: số lượng số Ra-one ở trong đoạn [a,b]</br>
### Ví dụ:</br>
234563 là số Ra-one: (6+4+2)-(3+5+3)=1</br>
123456 không phải số Ra-one: (5+3+1)-(6+4+2) ≠ 1

## Tìm số Lucifer
## Định nghĩa số Lucifer: là số mà hiệu giữa tổng các chữ số ở vị trí chẵn và tổng các chữ số ở vị trí lẻ là một số nguyên tố: [link code](https://github.com/ianTuG/hsg/blob/main/lucifer.py)
Input: a, b là số nguyên dương (a<b)</br>
Output: Số lượng số Lucifer có trong đoạn [a,b]
### Ví dụ:
20314210 là số Lucifer vì: (1+4+3+2) - (0+2+1+0) = 10-7=3 là 1 số nguyên tố
## Tổng lớn nhất: [link code](https://github.com/ianTuG/hsg/blob/main/maxsum.py)
Input: 1 số nguyên dương n (3 ≤ n ≤ 10^14)<br>
Output: số nguyên dương m (1 ≤ m < n-1) để tổng GCD(m,n)+m đạt max. GCD(m,n) là ước chung lớn nhất của m và n. Nếu có nhiều m thoả mãn thì trả lại giá trị m lớn nhất.<br>
|Sample input|Sample output|
|:----------:|:-----------:|
|      15    |      12     |
### Giới hạn
• 60% số test ứng với n ≤ 10^4<br>
• 40% số test ứng với n ≤ 10^14
