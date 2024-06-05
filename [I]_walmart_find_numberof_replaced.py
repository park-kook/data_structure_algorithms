'''
there are n servers with ids s1, s2, ..., sn, 
and an array of strings, logs, of size m. Log format 
is "<server_id> <success/error>", the id of the server, 
and the status of the processed request. 
If a particular server id logs an error for three consecutive requests, 
it is considered faulty and is replaced with a new server with the same id. 
Given n and the array logs, find the number of times a faulty server was replaced. 
  
 
Example 1: 
Suppose n = 2 and 
logs = ["s1 error", "s1 error", "s2 error", "s1 error", "s1 error", "s2 success"]. 
s1 was replaced one time. So, output should be 1.
'''


def replaced_server(n, logs):
    error_num = {}
    replacement_num = {}
    for i in range(1,n+1):
        server_id = 's'+str(i)
        error_num[server_id] = 0
        replacement_num[server_id] = 0
        
    for log in logs:
        server_id, success = log.split(" ")
        
        if success =='error':
            error_num[server_id]+=1
            if error_num[server_id] ==3:
                error_num[server_id]=0
                replacement_num[server_id] +=1
            
        else:
            error_num[server_id]=0
    return sum(replacement_num.values())      

n = 2
# logs = ["s1 error", "s1 error", "s2 error", "s1 error", "s1 error", "s2 success"]
logs = ["s1 error", "s1 error", "s2 error", "s1 error", "s1 error", "s2 success","s1 error","s1 error"]
replaced_server(n, logs)    
