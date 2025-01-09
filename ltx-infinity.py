import json
import time
import datetime
import random
from urllib import request, parse
import sys

START_TIME = time.time()

def queue_prompt(prompt_workflow):
    p = {"prompt": prompt_workflow}
    data = json.dumps(p).encode('utf-8')
    req =  request.Request("http://127.0.0.1:8188/prompt", data=data)
    request.urlopen(req)  

def free_mem():
    p = {"free_memory": True, "unload_models": True}
    data = json.dumps(p).encode('utf-8')
    req =  request.Request("http://127.0.0.1:8188/api/free", data=data)
    request.urlopen(req)    

def wait_for_queue():
    is_complete = False
    while not is_complete:
        time.sleep(5)
        req = request.Request("http://127.0.0.1:8188/queue")
        response = request.urlopen(req)
        body = json.loads(response.read().decode('utf-8'))
        queue_length = len(body['queue_pending']) + len(body['queue_running'])
        is_complete = queue_length == 0
    time.sleep(1)
    
init_start_time = time.time()
print("Creating init image")
queue_prompt(json.load(open('ltx-infinity-init.json')))
wait_for_queue()
free_mem()
print("Generated init image in " + str(datetime.timedelta(seconds=(time.time() - init_start_time))))

i = 0
while i < 600:
  segment_start_time = time.time()
  i += 1
  print("Generating segment #" + str(i))
  prompt = json.load(open('ltx-infinity-sdxl-unsampling.json'))
  prompt["655"]["inputs"]["noise_seed"] = random.randint(0, 100000000)
  queue_prompt(prompt)
  wait_for_queue()
  free_mem()
  print("Generated segment #" + str(i) + " in " + str(datetime.timedelta(seconds=(time.time() - segment_start_time))))