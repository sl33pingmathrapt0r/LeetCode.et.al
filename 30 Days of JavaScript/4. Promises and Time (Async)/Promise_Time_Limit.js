/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
	return async function(...args) {
        // // Solution 1: create a new Promise to execute fn within
        // // the time limit, and throw an error if the fn fails. 
        // return new Promise((resolve, reject)=> {
        //     let timerId; 
            
        //     // run the function while timer counting down
        //     fn(...args)
        //         .then(result => resolve(result))
        //         .catch(error => reject(error))
        //         .finally( () => clearTimeout(timerId));
            
        //     // set a timeout to countdown
        //     timerId= setTimeout( () => reject('Time Limit Exceeded'), t);

        //     // Internally, a race condition has begun, 
        //     // to return resolve/reject
        // });

        // Solution 2: use Promise.race to race 2 Promises
        const originalPromise = fn(...args);
        const timeoutPromise= new Promise((_,reject) => {
            setTimeout( () => reject('Time Limit Exceeded'), t);
        });
        // 'resolve' ignored since the promise will be terminated after race

        return Promise.race([originalPromise, timeoutPromise]);
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */
