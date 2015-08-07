If you know some Python, it is easy to add your own computer opponent, or "brain", to Kindral, whether you are using the .exe or the source code.

## Creating a minimal brain ##

To start with, you can copy and rename an existing brain, like the pretty basic [randomBrain](randomBrain.md), and start adjusting that.

An alternative is to subclass randomBrain and override `placeArmy` and `findMove`. In that case, the skeleton would look like this:

```
import randomBrain

class Brain(randomBrain.Brain):
    #def placeArmy(self):
    # uncomment and add code to override randomBrain's placeArmy

    #def findMove(self):
    # uncomment and add code to override randomBrain's findMove
```

## Making sure Kindral sees your custom brain ##

To make the game able to use your brain script, you need to insert the name of the file in `brains\__init__.py`.

For example, if you named your customized brain `myCustomBrain.py`, the resulting init.py should look like this:

```
__all__ = ["Brain",
           "CarefulBrain",
           "randomBrain",
           "SmartBrain",
           "SurpriseBrain",
           "myCustomBrain"]  # <----- new brain added here
```