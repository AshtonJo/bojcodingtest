let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let n = Number(input[0]);
let arr = [];

// 각각 나이,이름 순으로 정보 입력받기
for(let i=1; i<=n; i++) {
    let age = Number(input[i].split(" ")[0]);
    let name = input[i].split(" ")[1];
    arr.push([age, name]); //배열에 넣기
}
// 오름차순
arr.sort((a, b)=> a[0] - b[0]);

let answer = "";
for(let item of arr) {
    answer += item[0] + " " + item[1] + "\n";
}
console.log(answer);
