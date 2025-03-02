function mergeSortedArrays(arr1, arr2) {
  const mergedArray = [];
  let arr1item = arr1[0];
  let arr2item = arr2[0];
  let i = 1;
  let j = 1;
  if (arr1.length < 0) {
    return arr2;
  }
  if (arr2.length < 0) {
    return arr1;
  }
  while (arr1item || arr2item) {
    if (!arr2item || arr1item < arr2item) {
      mergedArray.push(arr1item);
      arr1item = arr1[i];
      i++;
    } else {
      mergedArray.push(arr2item);
      arr2item = arr2[j];
      j++;
    }
  }

  return mergedArray;
}

console.log(mergeSortedArrays([0, 3, 4, 31], [4, 6, 30]));

// Output: [ 0,  3,  4, 4, 6, 30, 31 ]
