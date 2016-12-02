function deepCopy(obj1, obj2) {
  let stack = [];
  for (let key in obj2) {
    stack.push(key);
  }

  while (stack.length !== 0) {
    let top = stack.pop()

    if (typeof top == "object" && typeof top !== null) {
      for (let key in top) {
        stack.push(top[key]);
        obj1[key] = obj2[key];
      }
    } else {
      obj1[top] = obj2[top];
    }
  }

  return obj1
}

let obj1 = {'A': 1, 'B': 3, 'C': 4}
let obj2 = {'A': 2, 'B': {'b': 5}}
console.log(deepCopy(obj1, obj2));
