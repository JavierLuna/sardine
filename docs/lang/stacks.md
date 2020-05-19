# Stacks

## Declaring stacks

For `sardine` to use a stack, you need to load it first.

```
Load 'spark'
Load '<stack_name>'
```

This will make `sardine` aware that a stack named `<stack_name>` is in the `default` repository.

## Aliasing stacks

Stacks can be aliased for convenience:

```
Load 'datastore-emulator' as datastore
Load '<stack_name>' as <alias>
```

This way, you could rename a given stack to the name of your choosing.

## Declaring stacks from different repositories

Sooner than later, you will want to load stacks from different repositories.

Sardine offers you several ways of doing it:

```
Use 'JavierLuna/sardine-stacks'
Use 'User/sardine' as user_sardine

Load 'spark' # This will load stack 'spark' from the default repository ('JavierLuna/sardine-stacks')
Load 'spark' from user_sardine # This will load stack 'spark' from the user_sardine repository ('User/sardine')
Load 'spark' from 'User2/direct-repo' # This will load stack 'spark' from the repository 'User2/direct-repo'
```

You can still use the alias:

```
Load 'spark' from 'User2/direct-repo' as spark2
```