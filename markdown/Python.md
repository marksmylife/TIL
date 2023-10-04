[매서드]
---
## 리스트(list) > 문자열(string) 변환
```
''.join<list>
```
### list_name = ['a', 'b', 'c']를 문자열(str)로 변환하면
```python
print(''.join(list_name))

결과 = abc
```

### '' 사이에 기호를 넣으면 기호로 분리됨
```python
print('|'.join(list_name))

결과 = a|b|c
```
---