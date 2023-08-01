// 숫자끼리 비교하는 연산과 문자끼리 비교하는 연산 중 왜 문자끼리 비교하는 연산이 
// 상대적으로 불리한지 이유에 대해서 정리해보고 샘플 코드를 구현해서 제출하기

const char1 = 'A';
const char2 = 'B';

// 관계 연산자를 사용한 비교
console.log(char1 < char2); // 출력: true

// localeCompare() 메소드를 사용한 비교
console.log(char1.localeCompare(char2)); // 출력: -1 (작다는 의미)



//문자열 길이 비교하기
const str1 = 'apple';
const str2 = 'orange';

console.log(str1.length < str2.length); // 출력: true

//알파벳 순서 비교하기:
const char3 = 'z';
const char4 = 'a';

console.log(char1 > char2); // 출력: true

//문자열 사전식 순서 비교하기:
const word1 = 'banana';
const word2 = 'apple';

console.log(word1.localeCompare(word2)); // 출력: 1 (사전식으로 더 뒤에 위치함)

//대소문자 무시하고 비교하기:
const str3 = 'Hello';
const str4 = 'hello';

console.log(str3.toLowerCase() === str4.toLowerCase()); // 출력: true

//특정 문자 포함 여부 확인하기:
const text = 'Hello, world';

console.log(text.includes('world')); // 출력: true

//문자열 뒤집기:
const reverseStr = str => str.split('').reverse().join('');
console.log(reverseStr('apple')); // 출력: elppa


//문자열 비교하여 같은 문자열 찾기:
const findCommonChars = (str1, str2) => {
    let commonChars = '';
    for (let char of str1) {
      if (str2.includes(char)) {
        commonChars += char;
      }
    }
    return commonChars;
  };
  
  console.log(findCommonChars('apple', 'banana')); // 출력: 'a'

//문자열을 배열로 변환하여 비교하기:
const arr1 = ['a', 'b', 'c'];
const arr2 = ['b', 'c', 'd'];

console.log(JSON.stringify(arr1) === JSON.stringify(arr2)); // 출력: false

//유니코드 코드 포인트 비교하기:

const char5 = 'A';
const char6 = 'a';

console.log(char3.charCodeAt(0) === char4.charCodeAt(0)); // 출력: false

//문자열 비교 결과로 숫자 값 얻기:
const result = 'apple'.localeCompare('orange');
console.log(result); // 출력: -1 (사전식으로 더 앞에 위치함)

