import wolframalpha

appid = "642Q4J-E5E9RP93XH";

def onstart():
    client = wolframalpha.Client(appid)
    res = client.query
    for pod in res.pods:
        do_something_with(pod)
    answer = next(res.results).text
    
   return Response(answer)