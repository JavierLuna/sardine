# Sardine language grammar

Here is the grammar used by `sardine`, defined in a EBNF-like syntax:

```
# Whitespace and comments will be ignored

S := <declaration>+
declaration := <repository_declaration>|<stack_declaration>
repository_declaration := <use><repository_name>(<as><alias>)?
stack_declaration := <load><stack_name>(<from>(<alias>|<repository_name>))?(<as><alias>)?
comment := #.+
repository_name := '([A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+)'
stack_name := '([A-Za-z0-9_.-]+)'
alias := [A-Za-z0-9_.-]+
use := [Uu]se
load := [Ll]oad
as := as
from := from
```