* max
    ```python
    def solution(a, b):
        return int(max(f"{a}{b}", f"{b}{a}"))
    ```
  * 위 함수에서 max를 통해 ab, ba 중 큰 값 찾기
  * f' 사용해서 str 대신하기