// 중복 요소를 가진 배열 생성
const myArray = [1, 2, 3, 4, 5, 3, 6, 7, 8, 9, 2];

// 유일한 요소를 저장하기 위한 빈 객체 생성
const uniqueElements = {};

// 원본 배열을 순회하며 유일한 요소를 uniqueElements 객체에 추가
for (const element of myArray) {
  uniqueElements[element] = true;
}

// 중복이 제거된 새로운 배열 생성
const uniqueArray1 = [];
for (const element in uniqueElements) {
  uniqueArray1.push(Number(element));
}

// 중복이 제거된 배열 출력
console.log(uniqueArray1);

//문자열 배열에서 중복 제거하기
const numbers = [1, 2, 3, 4, 5, 1, 2, 6, 7, 8];
const uniqueNumbers = {};
const uniqueArray2 = [];

for (const num of numbers) {
  uniqueNumbers[num] = true;
}

for (const num in uniqueNumbers) {
  uniqueArray2.push(Number(num));
}

console.log(uniqueArray2);


//불리언 배열에서 중복 제거하기
const boolValues = [true, false, true, true, false];
const uniqueValues3 = {};
const uniqueArray3 = [];

for (const value of boolValues) {
  uniqueValues3[value] = true;
}

for (const value in uniqueValues3) {
  uniqueArray3.push(value === 'true');
}

console.log(uniqueArray3);

//객체 배열에서 중복 제거하기
const students = [
    { name: 'Alice', age: 25 },
    { name: 'Bob', age: 30 },
    { name: 'Alice', age: 25 },
    { name: 'Charlie', age: 22 },
  ];
  
const uniqueStudents = {};
const uniqueArray4 = [];

for (const student of students) {
const key = `${student.name}-${student.age}`;
uniqueStudents[key] = student;
}

for (const key in uniqueStudents) {
uniqueArray4.push(uniqueStudents[key]);
}

console.log(uniqueArray4);

//다양한 데이터 유형을 갖는 배열에서 중복 제거하기
const mixedData = [1, 'apple', true, 'banana', 1, 2, true, 'orange', 3];
const uniqueValues5 = {};
const uniqueArray5 = [];

for (const data of mixedData) {
  const key = typeof data === 'string' ? data : JSON.stringify(data);
  uniqueValues5[key] = data;
}

for (const key in uniqueValues5) {
  uniqueArray5.push(uniqueValues5[key]);
}

console.log(uniqueArray5);

// [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
// [ 1, 2, 3, 4, 5, 6, 7, 8 ]
// [ true, false ]
// [ { name: 'Alice', age: 25 },
//   { name: 'Bob', age: 30 },
//   { name: 'Charlie', age: 22 } ]
// [ 1, 2, 3, 'apple', true, 'banana', 'orange' ]
