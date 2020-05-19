# Sardine language overview

Sardine offers a really simple declarative language to configure how the tool behaves.

Sardine allows you to declare repositories and stacks, and tweak how the tool interacts with them.

For a more detailed explanation, please go to:

* [Repositories](./repositories.md)
* [Stacks](./stacks.md)


## Whitespace
Sardine will ignore whitespace, but is sensitive to new lines.
Every declaration must go in their own line.

## Comments

What would be a language without comments, right?

Sardine allows one-line comments by using the `#` character:

```
# This line will be ignored
Use 'spark' # This comment will be ignored as well!
```

Comments will be completely ignored by `sardine`.