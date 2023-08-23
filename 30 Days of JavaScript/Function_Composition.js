/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
	return function(x) {
        var ans=x;
        for (var i=functions.length-1; i>=0; i--) {
            ans= functions[i](ans);
        }
        return ans;

        // OR using reduceRight, 
        /* 
            if (functions.length === 0) {
                return function(x) { return x; };
            }

            return functions.reduceRight(function(prevFn, nextFn) {
                return function(x) {
                return nextFn(prevFn(x));
                };
            });
	*/
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */
