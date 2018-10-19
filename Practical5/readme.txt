HTTP IN Node (Http Request)
- Method: GET
- URL: /querytemp

Exec Node (Red colored node with arrow at end)
- Command: vcgencmd measure_temp

Function Node (Orange color node with F at start)
- function:
str = msg.payload
str = str.substring(5,11)
msg.payload = '<h1>The current temp is ' + str + '</h1>';
return msg;

HTTP Response node
- Status code: 200


Connect all nodes sequentially.