# entropy

## made this for me, if you'd like to improve anything feel free to do so. cmds and install instructions are down below

## cmds
    # make sure you have developer mode enabled to copy ids, if you don't already go to settings > advanced > enable developer mode
    
    # purge messages from bottom to top
    .p (will use current channel) OR .p snowflake (dm/group/channel)

    # purge messages from top to bottom
    .pold (will use current channel) OR .pold snowflake (dm/group/channel)

    # purge messages before snowflake (message id, e.g: 1049011454973579274) - will not delete the message id used if it's yours
    .pbefore channel snowflake

    # purge messages after snowflake (message id, e.g: 1049011454973579274) - will not delete the message id used if it's yours
    .pafter channel snowflake

    # purge messages between snowflakes (message id, e.g: 1049011454973579274) - will not delete the message id used if it's yours
    .pinbetween channel snowflake1 snowflake2

## install

download python (3.10+): https://www.python.org/downloads/release/python-3109/

download git (windows): https://git-scm.com/download/win

download selfcord:

    # Windows
    py -3.10 -m pip install git+https://github.com/dolfies/discord.py-self@renamed#egg=selfcord.py[voice]

    # Linux/macOS
    python3.10 -m pip install git+https://github.com/dolfies/discord.py-self@renamed#egg=selfcord.py[voice]

python3.10 or above is **required**, you can use different versions by doing `py -3.10` or `python3.10`

**after you're done installing python/git/selfcord:**

    git clone https://github.com/apathy/entropy-discord-purger

code snippet to get token from console (browser or discord client):
        
    (webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()


edit `entropy.py` and change `token_here` to your token

once you're done editing, **start entropy**:

    # Windows
    py -3.10 entropy.py

    # Linux/macOS
    python3.10 entropy.py

## dependencies
https://github.com/dolfies/discord.py-self
