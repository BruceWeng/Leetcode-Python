//1. Closure
function f() {
  let n = 42;

  // 內部函數取得變數 n
  function get(n) {
    console.log(n)
    return n;
  }

  // 另外一個內部函數也同時存取 n
  function next(n) {
    return n++;
  }

  return { get, next };
}

let o = f();
console.log(o.get(1)); // 42
o.next();
console.log(o.get()); // 43

// 2. Inner function looking for local variable n which is undefined when not passing 1
function f() {
  let n = 42;

  // 內部函數取得變數 n
  function get(n) {
    console.log(n)
    return n;
  }

  // 另外一個內部函數也同時存取 n
  function next(n) {
    return n++;
  }

  return { get, next };
}

let o = f();
console.log(o.get(1)); // 1
o.next();
console.log(o.get()); // undefined
