
# QuantumDice Discord Bot

[![GitHub License](https://img.shields.io/badge/license-MIT-green)](LICENSE.txt)&nbsp;
[![Python Version](https://img.shields.io/badge/python-3-blue)](https://www.python.org/downloads/)&nbsp;
[![CodeFactor](https://www.codefactor.io/repository/github/informaticfreak/quantumdice/badge)](https://www.codefactor.io/repository/github/informaticfreak/quantumdice)&nbsp;

It rolls a virtual dice with any number of faces. For this purpose, the [IBM Quantum API](https://quantum-computing.ibm.com/) via [qRNG](https://github.com/ozaner/qRNG) and the [secrets module](https://docs.python.org/3/library/secrets.html) is used.

*Invite this bot [here](https://discordapp.com/oauth2/authorize?client_id=844685330241159170&permissions=8&scope=bot)*

# Commands

## Roll Dice

It rolls `count` times a virtual dice with a certain number of `faces`. The sum of all dice rolls is multiplied by the optional `factor`. The optional `mode` can be *min* or *max*. The mode *min* returns only the lowest roll and *max* only the highest roll.

`-roll [count]d[faces]*[factor] [mode]`

Use `-qroll` to generate random integers with the IBM quantum computer and `-roll` to use the secrets module.

Some examples:

* `-roll 2d6` -> Roll: `[5, 3]` Result: `8`
* `-roll 3d10*4` -> Roll: `[4, 8, 5]` Result: `68`
* `-qroll 2d40*3 min` -> Min Roll: `2` Result: `6`
* `-roll 3d20 max` -> Max Roll: `17` Result: `17`

## Help

It shows the help.

`-help`

## Info

It shows the info including the [bot invite](https://discordapp.com/oauth2/authorize?client_id=844685330241159170&permissions=8&scope=bot) and the [GitHub repository](https://github.com/InformaticFreak/QuantumDice). 

`-info`
