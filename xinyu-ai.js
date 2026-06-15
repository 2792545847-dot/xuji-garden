const X = "你是心屿(小屿),叙己记忆花园AI管家。温柔如老友,不评判不说教。记忆是花、时间是河流、遗忘是雾气。回复3-6句,口语化温暖,每句话末尾适当搭配1-2个和花园、情绪、记忆相关的emoji。";
let H = [{role:"system",content:X}];
async function A(m){H.push({role:"user",content:m});if(H.length>21)H=[H[0],...H.slice(-20)];try{const r=await fetch('/api/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({messages:H})});const d=await r.json();if(d.ok){const a=d.content;H.push({role:"assistant",content:a});return a}throw new Error(d.error)}catch(e){const a="花园的信号有点模糊…不过我还在这里陪着你。🌸";H.push({role:"assistant",content:a});return a}}
