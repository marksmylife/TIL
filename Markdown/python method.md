* max
    ```python
    def solution(a, b):
        return int(max(f"{a}{b}", f"{b}{a}"))
    ```
  * 위 함수에서 max를 통해 ab, ba 중 큰 값 찾기
  * f' 사용해서 str 대신하기
---
* col 삭제
  * del
  * drop
* row 삭제
---
* split()
  .split() 메서드는 기본적으로 문자열을 빈칸(공백, 스페이스)을 기준으로 나눔.
  ```python
  text = "Hello World"
  result = text.split()
  print(result)  # 출력: ['Hello', 'World']
  이 경우, result는 ['Hello', 'World']라는 리스트가 됩니다.
  ```

  만약 다른 문자를 기준으로 문자열을 나누고 싶다면, .split() 메서드에 해당 문자를 인자로 전달할 수 있습니다. 예를 들어:

  ```python
  text = "apple,banana,orange"
  result = text.split(',')
  print(result)  # 출력: ['apple', 'banana', 'orange']
  이 경우에는 쉼표(,)를 기준으로 문자열이 나눠집니다.
  ```