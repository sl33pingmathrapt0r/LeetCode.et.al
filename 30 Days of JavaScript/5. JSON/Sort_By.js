/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    // cannot use obj.sort() as it converts all elements to strings, 
    // then compare UTF value => '10' < '9'

    return arr.sort((a,b) => fn(a) - fn(b));
    // if fn(a)>fn(b), then interpret a>b
};
