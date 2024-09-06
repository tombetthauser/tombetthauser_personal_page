function foo () {
  let len = Math.ceil(Math.random() * 100) + 5;
  let rab = Math.floor(Math.random() * len);
  let pos = 0;

  let count = 0 

  while (pos <= len) {
    if (pos === rab) {
      return true;
      break;
    }

    if (Math.random() > 0.5) {
      rab++;
    } else {
      rab--;
    }

    if (rab > len) {
      rab -= 2;
    }

    if (rab < 0) {
      rab += 2;
    }

    count++

    if (count > 2) {
      count = 0;
      pos += 1;
    }
  }

  return false;
}

for (let i = 0; i < 50; i++) {
  const ret = foo();
  if (ret === false) {
    console.log("FAILURE");
    break;
  }
}

console.log("FINISHED")