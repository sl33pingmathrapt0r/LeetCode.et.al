/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    // without using Array.filter
    newArr= []
    // Note if fn only takes 1 argument, then only the first arg will be passed
    arr.forEach((element,index) => {
        if (fn(element, index)) newArr.push(element);
    });
    return newArr;
};
