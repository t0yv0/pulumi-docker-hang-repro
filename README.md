Example courtesy of @sstuddard.

Pulumi hangs with:

```
pulumi up --yes
```

Editing Dockerfile removes the hang:

```
# Uncomment the following to make it work
#ARG DEBIAN_FRONTEND=noninteractive
```

So it would appear that Pulumi is waiting indefinitely for a Docker command.

Full discussion of the issue here:

https://github.com/pulumi/pulumi/issues/7074
