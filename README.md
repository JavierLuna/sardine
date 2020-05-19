# Sardine

Manage your snippet-like docker composes.

## What is sardine?

I make heavy use of docker for really trivial stuff when developing.
I don't like to install a postgresql database or a mysql one for a specific project,
so I end up spinning a docker container with that database or component and then remove it once I'm done.

This is clean and really useful, but I have to copy and paste commands every time I want to spin the database I want,
or create several aliases.

But what If I want a spark cluster? Then I'll have to mess around docker-compose, and maintain a `docker-compose.yml` file.

What a mess!

What if I could just do: `sardine run spark` or `sardine run postgres`?

That'd be awesome right? :)