
# version_settings() enforces a minimum Tilt version
# https://docs.tilt.dev/api.html#api.version_settings
version_settings(constraint='>=0.22.2')

# project backend (Python/Flask app)
docker_build(
    'whodat-back',
    context='.',
    dockerfile='./deploy/back.dockerfile',
    only=['./back/'],
    live_update=[
        sync('./back', '/app'),
        run(
            'pip install -r /app/requirements.txt',
            trigger=['./back/requirements.txt']
        )
    ]
)

# k8s_yaml automatically creates resources in Tilt for the entities
# and will inject any images referenced in the Tiltfile when deploying
# https://docs.tilt.dev/api.html#api.k8s_yaml
k8s_yaml('deploy/back.yaml')

# k8s_resource allows customization where necessary such as adding port forwards and labels
# https://docs.tilt.dev/api.html#api.k8s_resource
k8s_resource(
    'back',
    port_forwards='5000:5000',
    labels=['backend']
)

# k8s_yaml automatically creates resources in Tilt for the entities
# and will inject any images referenced in the Tiltfile when deploying
# https://docs.tilt.dev/api.html#api.k8s_yaml
k8s_yaml('deploy/worker.yaml')


# whodat-web is the frontend (VueJS app)
# live_update syncs changed source files to the correct place for vite to pick up
# and runs yarn (JS dependency manager) to update dependencies when changed
# if babel.config.js changes, a full rebuild is performed because it cannot be
# changed dynamically at runtime
docker_build(
    'whodat-front',
    context='.',
    dockerfile='./deploy/front.dockerfile',
    only=['./front/'],
    ignore=['./front/dist/'],
    live_update=[
        fall_back_on('./front/babel.config.js'),
        sync('./front/', '/app/'),
        run(
            'npm install',
            trigger=['./web/package.json', './web/package-lock.json']
        )
    ]
)

# k8s_yaml automatically creates resources in Tilt for the entities
# and will inject any images referenced in the Tiltfile when deploying
# https://docs.tilt.dev/api.html#api.k8s_yaml
k8s_yaml('deploy/front.yaml')

# k8s_resource allows customization where necessary such as adding port forwards and labels
# https://docs.tilt.dev/api.html#api.k8s_resource
k8s_resource(
    'front',
    port_forwards='8080:8080',
    labels=['frontend']
)

# whodat-db is the database (Postgres)
docker_build(
    'whodat-db',
    context='.',
    dockerfile='./deploy/db.dockerfile',
    only=['./db/']
)

# k8s_yaml automatically creates resources in Tilt for the entities
# and will inject any images referenced in the Tiltfile when deploying
# https://docs.tilt.dev/api.html#api.k8s_yaml
k8s_yaml('deploy/db.yaml')
k8s_resource('worker', labels=['worker'])

# k8s_resource allows customization where necessary such as adding port forwards and labels
# https://docs.tilt.dev/api.html#api.k8s_resource
k8s_resource(
    'db',
    port_forwards='5432:5432',
    labels=['database']
)

# k8s_yaml automatically creates resources in Tilt for the entities
# and will inject any images referenced in the Tiltfile when deploying
# https://docs.tilt.dev/api.html#api.k8s_yaml
k8s_yaml('deploy/rabbitmq.yaml')

# k8s_resource allows customization where necessary such as adding port forwards and labels
# https://docs.tilt.dev/api.html#api.k8s_resource
k8s_resource(
    'rabbitmq',
    port_forwards=['5672:5672', '15672:15672'],
    labels=['rabbitmq']
)

# config.main_path is the absolute path to the Tiltfile being run
# there are many Tilt-specific built-ins for manipulating paths, environment variables, parsing JSON/YAML, and more!
# https://docs.tilt.dev/api.html#modules.config.main_path
tiltfile_path = config.main_path

# print writes messages to the (Tiltfile) log in the Tilt UI
# the Tiltfile language is Starlark, a simplified Python dialect, which includes many useful built-ins
# https://github.com/bazelbuild/starlark/blob/master/spec.md#print
print("""
\033[32m\033[32mHello World from WhoDat!\033[0m

If this is your first time using Tilt and you'd like some guidance, we've got a tutorial to accompany this project:
    https://docs.tilt.dev/tutorial

If you're feeling particularly adventurous, try opening `{tiltfile}` in an editor and making some changes while Tilt is running.
What happens if you intentionally introduce a syntax error? Can you fix it?
""".format(tiltfile=tiltfile_path))
