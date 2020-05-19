# Quick start

Once your requirements are met, you can follow this guide.

## Get latest sardine version

```
pip install sardine --user # Use your python 3.6+'s pip
```

## Configure .sardinerc

Create a `.sardinerc` file, and fill it up like:

`~/.config/sardine/.sardinerc`:

```
Use 'JavierLuna/sardine-stacks'

Load 'spark'
```

## Run spark cluster

Then, run `sardine run spark`

And voilá! We have an Apache Spark cluster at the comfort of our laptops.

Sardine will automatically download the `spark` stack from [JavierLuna/sardine-stacks](https://github.com/JavierLuna/sardine-stacks)
and will attempt to run it with `docker-compose`.