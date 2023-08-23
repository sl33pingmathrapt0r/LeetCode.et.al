class EventEmitter {
    constructor() {
        this.events={};
    }

    subscribe(event, cb) {
        if (event in this.events) this.events[event].push(cb);
        else this.events[event]= [cb];

        return {
            unsubscribe: () => {
                if (Array.isArray(this.events[event])) 
                    // re-assignment required, filter() does not mutate original
                    this.events[event]=this.events[event].filter( (fn)=> !(fn=== cb) );
                return undefined;
            }
        };
    }

    emit(event, args = []) {
        const calls= this.events[event];
        const result= [];
        // the event is not removed, no need for `delete this.events[event]`
        
        if (!calls) return result;
        calls.forEach( element => result.push(element(...args)) );
        return result;
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */
