### 문자열(string)

> 컴퓨터에서의 문자표현

* 각 문자에 대해 대응되는 숫자를 정해놓고, 이것을 메모리에 저장하는 방법을 사용한다.
* 영어가 대소문자 합쳐서 52 이므로 6(64가지) 비트면 모두 표현할 수 있다.
  * => *코드체계*
* ASCII(American Standard Code for Information Interchange) : 문자 인코딩 표준이 제정됨(1967년)
  * 7bit 인코딩으로 128문자를 표현하며 33개의 출력 불가능한 제어 문자들과 공백을 비롯한 95개의 출력 가능한 문자들로 이루어져 있다.
  * 확장 아스키: 표준 문자 이외의 악센트 문자, 도형 문자, 특수 문자, 특수 기호 등 부가적인 문제를 128개를 추가할 수 있게 하는 부호

* 유니코드도 다시 character set으로 분류된다
  * UCS-2(Universal Character Set 2)
  * UCS-4(Universal Character Set 4)
    * 유니코드를 저장하는 변수의 크기를 정의
    * 그러나 바이트 순서에 대해 표준화하지 못했음
    * 따라서 유니코드의 적당한 외부 인코딩이 필요하게 됨

* 유니코드 인코딩(UTF: Unicode Transformation Format)



> 문자열 비교

* c => strcmp() 함수를 제공
* Java => 에서는 equals() 메소드 제공
  * 문자열 비교에서 == 연산은 메모리 참조가 같은지를 묻는 것
* **python** => **==** 연산자와 **is** 연산자를 제공한다
  * == 연산자는 내부적으로 특수 메서드 __eq\_\_() 를 호출


```python
a = 'abc'
b = 'ab'
c = 'de'
d = 'Abc'

print(a>b) #=> True; b가 a보다 빠르니? yes!! 
print(a<b) #=> False; a가 b보다 빠르니? no!!
print(a>d) #=> True; d에 대문자가 있니? yes
print(a<d) #=> False; a에 대문자가 있니? no

'''
사전에 나와있는 순서대로 비교한다!
한글도 비교 가능
'''
kor_a = '가나다'
kor_b = '다나가'
print(kor_a < kor_b) #=> True; '가' 가 '다' 보다 빠르다!
```



```python
# int()와 같은 atoi()함수 만들기
def atoi(s):
    i = 0 # 10진수로 변환해서 저장해 놓은 자리
    for x in s:
        i = i*10 + ord(x) - ord('0')
        #ord(x) => x에 대한 ASCII코드 출력
    return i
```



> 패턴 매칭

* 고지식한 알고리즘 (Brute Force)
  * 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일히 비교하는 방식으로 동작
  * 시간 복잡도
    * 최악의 경우: 텍스트의 모든 위치에서 패턴을 비교해야 하므로 O(MN)
  * KMP 알고리즘
    * 불일치가 발생한 앞 부분에 대해 다시 비교하지 않고 매칭을 수행
    * 시간 복잡도: O(M+N)