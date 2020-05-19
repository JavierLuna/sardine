# The sardinerc file

This file is used to declare all the repositories and stacks you want sardine to be aware of.

An example of a `.sardinerc` file could be:

```
Use 'JavierLuna/sardine-stacks'

Load 'spark'
Load 'postgresql' as 'postgre'
Load 'mongodb' as 'mongo'
```

This will tell `sardine` to use [JavierLuna/sardine-stacks](https://github.com/JavierLuna/sardine-stacks) 
as our default repository, and from it to load the following stacks:

* `spark`
* `postgresql`, aliased as `postgre`
* `mongodb`, aliased as `mongo`

## Location

By default, `sardine` will look for the `.sardinerc` file in `~/.config/sardine/.sardinerc`, 
but you can change that path by setting the environment variable `SARDINE_RC_PATH`:

```bash
export SARDINE_RC_PATH=~/.sardinerc 
```