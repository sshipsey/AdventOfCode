function getFloor(input) {
	arr = input.split('');
	console.log(arr.reduce(function(prev, curr, idx) { 
		return {
			floor: (curr === '(' ? ++prev.floor : --prev.floor),
			basement_idx: ((prev.floor === -1) && (prev.basement_idx === -1)) ? (idx + 1) : prev.basement_idx
		}
	}, { floor:0, basement_idx: -1 }));
}
var input = '()(((()))(()()()((((()(((())(()(()((((((()(()(((())))((()(((()))((())(()((()()()()(((())(((((((())))()()(()(()(())(((((()()()((())(((((()()))))()(())(((())(())((((((())())))(()())))()))))()())()())((()()((()()()()(()((((((((()()())((()()(((((()(((())((())(()))()((((()((((((((())()((()())(())((()))())((((()())(((((((((((()()(((((()(()))())(((()(()))())((()(()())())())(()(((())(())())()()(()(()((()))((()))))((((()(((()))))((((()(()(()())())()(((()((((())((((()(((()()(())()()()())((()((((((()((()()))()((()))()(()()((())))(((()(((()))((()((()(()))(((()()(()(()()()))))()()(((()(((())())))))((()(((())()(()(())((()())))((((())))(()(()(()())()((()())))(((()((()(())()()((()((())(()()((())(())()))()))((()(())()))())(((((((()(()()(()(())())))))))(()((((((())((((())((())())(()()))))()(())(()())()())((())(()))))(()))(()((()))()(()((((((()()()()((((((((()(()(())((()()(()()))(())()())()((())))()))()())(((()))(())()(())()))()((()((()(()()())(())()()()((())())))((()()(()()((()(())()()())(((()(()()))))(())))(()(()())()))()()))))))()))))((((((())))())))(()(())())(()())))))(()))()))))))()((()))))()))))(()(()((()())())(()()))))(((())()))())())())(((()(()()))(())()(())(())((((((()()))))((()(()))))))(()))())(((()()(()))()())()()()())))))))))))))(())(()))(()))((()(())(()())(())())(()())(())()()(()())))()()()))(())())()))())())(())((())))))))(())))(())))))()))))((())(()(((()))))(()))()((()(())))(()())(((((()))()())()()))))()))))()))())(()(()()()))()))))))((()))))))))))()((()))((()(())((())()()(()()))()(()))))()()(()))()))(((())))(())()((())(())(()())()())())))))))())))()((())))()))(()))()()))(((((((()))())(()()))(()()(()))()(()((()())()))))))(((()()()())))(())()))()())(()()))()()))))))))(())))()))()()))))))()))()())))()(())(())))))()(())()()(()()))))())((()))))()))))(()(((((()))))))))())))())()(())()()))))(())))())()()())()()())()(()))))()))()))))))))())))((()))()))()))())))()())()()())))())))(()((())()((()))())))))())()(())((())))))))))))())()())(())())())(()))(()))()))())(()(())())()())()()(()))))(()(())))))))(())))())(())))))))())()()(())())())))(())))))()))()(()())()(()))())())))))()()(()))()))))())))))))))()))))()))))))())()())()()))))()())))())))))))))))()()))))()()(((()))()()(())()))))((()))))(()))(())())))(())()))))))(()))()))))(())())))))()))(()())))))))))))))())))))))))()((()())(()())))))))((()))))(())(())))()(()())())))())())(()()()())))()))))))())))))())()()())))))))))))()()(()))))()())()))((()())(()))))()(()))))))))))()())())(((())(()))))())()))()))()))))))()))))))(()))))()))))()(())))(())))(()))())()()(()()))()))(()()))))))))()))(()))())(()()(()(()())()()))()))))))))(())))))((()()(()))())())))))()))())(()())()()))())))()(()()()()))((())())))())()(()()))()))))))))(()))(())))()))))(()(()())(()))))()())())()))()()))())))))))))))())()))))))()))))))))())))))()))))())(()())))(())()))())())))))()()(()()())(()())))()()))(((()))(()()()))))()))))()))))((())))()((((((()()))))))())))))))))))(((()))))))))))))(())())))))())(()))))))(()))((()))())))()(()((()))()))()))))))))))())()))()(()()))))())))())(())()(()))()))())(()))()))))(()()))()()(())))))()))(())(()(()()))(()()())))))(((()))))))()))))))))))))(())(()))))()())())()()((()()))())))))(()))))())))))))()()()))))))))())))()(((()()))(())))))(((())())))))((()))()(()))(()))))(()())))(()))())))))()))))(())(())))()((()))(())())))()()))()))))))))()))(()()()(()()()(()))())(())()())(((()))(())))))))))(((()())))()()))))))))()(())(()))()((((())(())(()())))()))(((())()()()))((()))(()))())())))())))(()))())()())())(()(())())()()()(())))())(())))(())))(())()))()))(()((()))))))))())(()))))))())(()()))()()))()(()(()())))()()(()((()((((((()))(())))()()()))())()))((()()(()))())((()(()(()))(()()))))()())))()))()())))))))()()((()())(())))()))(()))(())(()))())(()(())))()()))))))(((()(((()()))()(()(())())((()()))()))()))()))()(()()()(()))((()())()(())))()()))(((())()()())(())()((()()()()(()(())(()()))()(((((()())))((())))))(()()()))))(((()(())))()))((()((()(())()(()((())))((()())()(()))(((()())()()(()))(())(((()((()())()((())()())(((()()))((()((())(()))(()())(()()()))((()))(())(()((()()())((()))(())))(())(())(())))(()())))(((((()(()(((((()())((((()(()())(())(()()(((())((()(((()()(((()()((((((())))())(()((((((()(()))()))()()((()((()))))()(()()(()((()()))))))(((((()(((((())()()()(())())))))))()))((()()(())))(())(()()()())))))(()((((())))))))()()(((()(()(()(()(()())()()()(((((((((()()())()(()))((()()()()()(((((((()())()((())()))((((((()(()(()(()())(((()(((((((()(((())(((((((((())(())())()))((()(()))(((()()())(())(()(()()(((()(())()))())))(())((((((())(()()())()()(((()(((())(()(((())(((((((()(((((((((()))(())(()(()(()))))((()))()(())())())((()(()((()()))((()()((()(())(())(()((())(((())(((()()()((((((()()(())((((())()))))(())((()(()((())))(((((()(()()())())((())())))((())((()((()()((((((())(((()()(()())())(()(()))(()(()))())())()(((((((()(((()(())()()((())((()(()()((()(()()(((((((((((())((())((((((())((()((((()(()((((()(((((((())()((()))))())()((()((((()(()(((()((()())))(())())(((()(((())((((((()(((((((((()()(())))(()(((((()((((()())))((()((()((()(()()(((())((((((((((((()(((())(()(((((()))(()()(()()()()()()((())(((((((())(((((())))))())()(()()(()(()(((()()(((((())(()((()((()(((()()((()((((())()))()((((())(())))()())(((())(())(()()((()(((()()((((((((((()()(()())())(((((((((())((((()))()()((((())(()((((()(((())())(((((((((((()((((())))(())(()(((()(((()((())(((((()((()()(()(()()((((((()((((()((()(()((()(()((((((()))))()()(((((()((()(()(())()))(())(((((((()((((()())(()((()((()(()))())))(())((()))))(((((((()()()())(()))(()()((()())()((()((()()()(()(()()))(()())(())(((((()(((((((((((()((()(((()(((((((()()((((((()(((((()(()((()(((((())((((((()))((((())((()()((())(((())()(((((()()(((((()((()(()(((((((()(((((()((()((()((())(())((())(()))()()))(()()(()(()()(((((((()(((()(((())()(((((()((((((()())((((())()((()((()(()()())(()))((((()()((((((()((()(()(()((((()((()((())((((((()(()(())((((((()((((((((((()((())()))()(()(()(((((()()()))((())))()(()((((((((((((((()(((()((((()((())((()((()(((()()(()(((()((())(()()())))()(()(()(((((()()(()(()((((()(((((())()(()(()))(((((()()(((()()(())((((((((((((((())((())(((((((((((())()()()(())()(()(()(((((((((())(((()))(()()())(()((((()(())(((((()())(())((((((((())()((((()((((((())(()((()(())(((()((((()))(((((((((()()))((((()(())()()()(())(()((())((()()))()(((())(((((())((((((()()))(((((((((()((((((())))(((((((()((()(()(())))())(()(()))()(((((()())(()))()(()(())(((()))))())()())))(((((()))())()((()(()))))((()()()((((((()))()()((((((((())((()(()(((()(()((())((()())(()((((())(()(((()()()(()(()()))())())((((((((((())())((()))()((())(())(())))())()(()()(())))())(()))(((()(()()(((()(((())))()(((()(())()((((((())()))()))()((((((()(()(((((()())))()))))())()()(((()(((((())((()()(()((()((()(()(()(())))(()()()()((()(())(((()((()))((((()))())(())))())(()))()()()())()))(((()()())()((())))(())(()()()()(()())((()(()()((((())))((()((()(())((()(()((())()(()()(((()())()()())((()))((())(((()()(())))()()))(((()((())()(((((()())(())((())()())())((((((()(()(((((()))(()(';
getFloor(input);