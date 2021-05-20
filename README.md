# QuantumDice Discord Bot

[![CodeFactor](https://www.codefactor.io/repository/github/informaticfreak/quantumdice/badge)](https://www.codefactor.io/repository/github/informaticfreak/quantumdice)&nbsp;

It rolls a virtual dice with any number of faces. For this purpose, the secrets module is used to generate cryptographically strong random numbers.

*Invite this bot [here](https://discordapp.com/oauth2/authorize?client_id=844685330241159170&permissions=8&scope=bot)*

## Why is no real quantum computer used?

*Unfortunately without IBM Quantum API after all, because up to 7 minutes waiting time in the job queue!!!*

As an alternative to IBM, the Built-In Python library [secrets](https://docs.python.org/3/library/secrets.html) is used:

"*The [secrets](https://docs.python.org/3/library/secrets.html) module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.*"

# Commands

## Roll Dice

It rolls `count` times a virtual dice with a certain number of `faces`. The sum of all dice rolls is multiplied by the optional `factor`.

`!roll [count]d[faces]*[factor]`

It returns for example:

* `!roll 2d6` -> Roll: `[5, 3]` Result: `8`
* `!roll 3d10*4` -> Roll: `[4, 8, 5]` Result: `68`

## Help

It shows the help.

`!help`

## Info

It shows the info including the [bot invite](https://discordapp.com/oauth2/authorize?client_id=844685330241159170&permissions=8&scope=bot) and the [GitHub repository](https://github.com/InformaticFreak/QuantumDice). 

`!info`
