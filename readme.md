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
## Máy quét số: [link code](https://github.com/ianTuG/hsg/blob/main/checker.py)
### Mô tả:
Hệ thống máy quét đề nhận dạng các số của một ngân hàng hiện đã bị hacker xâm nhập và làm cho chúng không thể nhận dạng được một số chữ số. Tạm gọi những chữ số mà máy quét không nhận dạng được là chữ số bị hỏng. Máy quét sẽ không nhận dạng được các số có chứa ít nhất một chữ số bị hỏng.
### Ví dụ:
Có 3 chữ số bị hỏng: 0, 1, 3 thì máy quét sẽ không nhận dạng được các số: <br>
1, 3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 30,...<br>
Để đánh giá khả năng làm việc của máy quét, đội kiểm định đưa ra yêu cầu: biết các chữ số bị hỏng và một số nguyên dương n cho trước, họ cần biết có bao nhiêu số nguyên dương không vượt quá n mà máy quét vẫn có thể nhận dạng được.<br>
<br>
- Input:<br>
• Dòng 1: Gồm 1 số nguyên dương n (n≤10^7)<br>
• Dòng 2: Gồm một xâu kí tự là các chữ số bị hỏng (len_str < 10), các chữ số bị hỏng sẽ được viết liền không có dấu cách.<br>
- Output: Số nguyên dương m duy nhất (m < n) mà máy quét có thể nhận dạng được. 

## Số chính phươngph: [link code]()
### Định nghĩa:
- Số chính phương đặc biệt là số chính phương được tạo bởi một số nguyên tố.
### Ví dụ:
- 4 = 2 x 2 là số chính phương đặc biệt <br>
- 9 = 3 x 3 là số chính phương đặc biệt <br>
- 36 = 6 x 6 không phải là số chính phương đặc biệt<br>
|input.inp|output.out|
|:-----:|:-----:|
|2 10|2|
### Nhập xuất:
- Input: 2 số nguyên dương a, b (2≤a≤b≤10^12) <br>
- Output: Trong đoạn [a..b] có bao nhiêu số chính phương đặc biệt. <br>
- Dữ liệu vào từ tệp input.inp và ghi kết quả ra ở tệp output.out
