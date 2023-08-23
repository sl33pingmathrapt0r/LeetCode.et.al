/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = async function(functions) {
    // without using Promise.all

    // use a Promise chain: 
    // .then() when resolved, .catch() when rejected, .finally() regardless
    return new Promise((resolve, reject) => {
        const results=new Array(functions.length);
        let count= 0;

        functions.forEach((fn, index) => {
            fn()
            // cannot just push since promises don't resolve in given order
            .then(result => {
                results[index]=result;
                count++;
                if (count=== functions.length) resolve(results);
            })
            .catch(error => reject(error)) ;
        });
    })

};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */
