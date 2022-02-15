

| :exclamation:  | This is a mirror of [https://git.sr.ht/~tim-clifford/mastermind](https://git.sr.ht/~tim-clifford/mastermind). Please refrain from using GitHub's issue and PR system.  |
|----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|


# Mastermind
Classic Mastermind game written in python with tkinter

[project specification](specification.pdf)

## Getting Started

[rules](rules.txt)

### Running

    $ python3 main.py

### Modifying the game
By default there are 6 colors and the code is 4 colors long. The maximum number of attempts is 10.

This is stored as plaintext in [colors.txt](colors.txt) and can be modified easily

``` CHOICES: 4``` number of colors in the code

``` MAX ATTEMPTS: 10``` maximum attempts
``` 
#f00 red
#00f blue
#0f0 green
#ff0 yellow
#f0f pink
#ccc silver
```
colors can be added or deleted and the number of colors does not matter. The description after the hex code is ignored
 
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
