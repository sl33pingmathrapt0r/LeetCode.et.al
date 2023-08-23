/**
 * @param {Function} fn
 */
function memoize(fn) {
    const cache={};

    return function(...args) {
        const key= JSON.stringify(args);
        if (key in cache) return cache[key];

        // apply the fn into the current memoize() function object, 
        // with the same set of arguments
        cache[key]= fn.apply(this, args);
        return cache[key];
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */
