import sys
import json
import i3msg as i3
import os

filename = '.ws.txt'

try:
    with open(filename, 'r') as f:
        mode = 'restore'
        old = json.loads(f.read())
except IOError:
    mode = 'hide'

if mode == 'hide':
    outputs = i3.send(i3.GET_OUTPUTS)
    currentWorkspaces = {}

    for output in outputs:
        name = output['name']
        workspace = output['current_workspace']
        print(name)
        if workspace is not None:
            currentWorkspaces[name] = workspace
            i3.send(i3.RUN_COMMAND, 'workspace ' + workspace)
            i3.send(i3.RUN_COMMAND, 'workspace ' + output['name'])
    
    f = open(filename, 'w')
    f.write(json.dumps(currentWorkspaces))
    f.close()
elif mode == 'restore':
    outputs = i3.send(i3.GET_OUTPUTS)

    for output in outputs:
        name = output['name']
        workspace = output['current_workspace']
        print(name)
        if workspace is not None and old.get(name) is not None:
            i3.send(i3.RUN_COMMAND, 'workspace ' + workspace)
            i3.send(i3.RUN_COMMAND, 'workspace ' + old.get(name))

    os.remove(filename)
else:
    print('Error... Invalid mode')    
    sys.exit(1)

sys.exit(0)