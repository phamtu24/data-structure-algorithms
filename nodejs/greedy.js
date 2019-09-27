const maxLines = (givenData) => {
  givenData = givenData.sort((a, b) => {
    return a[1] - b[1]; 
  });
  let answer = 0;

  for (let i = 0; i < givenData.length-1; i++ ) {
    let rightNode = givenData[i][1];
    let checkNode = givenData[i+1][0];

    if (rightNode >= checkNode) {
      answer += 1;
    }
  }
  return answer;
} 

const givenData = [[0,4],[1,3],[3,4],[4,5]];
console.log(maxLines(givenData));
