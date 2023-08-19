/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    // without using Array.map method
    var newArr= [];

    /** for (let i=0; i<arr.length; i++) {
     *      newArr[i]= fn(arr[i], i);
     *  }
     */ 
    
    arr.forEach((element, index) => {
        newArr[index]= fn(element, index);
    }) 

    return newArr;
};
