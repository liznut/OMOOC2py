from fabric.api import *
import fabric.contrib.project as project
import os

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = '.html'
env.static_path = '.static'

def serve():
    local('markdoc serve')
def reserve():
    build()
    serve()

def build():
    local('markdoc build && '
            #'ls -la && '
            'rsync -avzP4 {static_path}/media/ {deploy_path}/media/ && '
            'pwd '.format(**env)
        )

def p2cafe():
    build()
    local('pwd && '
            'cd {deploy_path} && '
            #'ls -la && '
            'git st && '
            'git add --all . && '
            'git ci -am "re-gen. by markdoc. @ Zoom.Quiet local env." && '
            'git pu && '
            #'ls && '
            'pwd '.format(**env)
          )

