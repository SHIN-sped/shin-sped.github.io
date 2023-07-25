// 케이스 1: 변수를 초기화하지 않고 사용하기
let x;
console.log(x === null); // false (x는 undefined이므로 null이 아님)

// 케이스 2: 변수에 null 값 할당하기
let y = null;
console.log(y === null); // true (y는 null이므로 null)

// 케이스 3: 함수에서 값을 반환하지 않고 호출하기
function foo() {}
console.log(foo() === undefined); // true (foo 함수는 반환값이 없으므로 undefined)

// 케이스 4: 객체의 프로퍼티에 접근하기
const person = { name: 'Alice', age: 30 };
console.log(person.address === undefined); // true (person 객체에 address 프로퍼티가 없으므로 undefined)

// 케이스 5: 배열의 요소에 접근하기
const arr = [1, 2, 3];
console.log(arr[3] === undefined); // true (arr 배열에 4번째 요소가 없으므로 undefined)

// 케이스 6: 함수의 매개변수를 전달하지 않고 호출하기
function bar(x) {
  console.log(x === undefined);
}
bar(); // true (bar 함수에 매개변수를 전달하지 않았으므로 x는 undefined)