/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    // without lodash's _.chunk()
    newArr=[]

    num= Math.ceil(arr.length/size);
    for (var i=0; i<num; i++) {
        newArr[i]=[];
        for (var j=0; j<size; j++) {
            index= i*size +j;
            if (index < arr.length) {
                newArr[i][j]= arr[index];
            } else break;
        }
    }

    return newArr;
};
