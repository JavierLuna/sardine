# Repositories

## Declaring repositories

Declaring a repository is useful if you want to load several stacks from a sardine repository.

```
Use '<github_username>/<repository_name>'
Use 'JavierLuna/sardine-stacks' 
```

## Aliasing repositories

Repositories can be aliased for their later reference:

```
Use 'JavierLuna/sardine-stacks' as myrepo
```

### The default repository

An unaliased repository is considered as `default`:

```
Use 'JavierLuna/sardine-stacks'
# Same as:
Use 'JavierLuna/sardine-stacks' as default
```

Be aware that you cannot use an alias twice!