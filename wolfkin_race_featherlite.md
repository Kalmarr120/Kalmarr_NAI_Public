# Wolfkin Race in Featherlite

_This was originally a submission to Rinter's AID character wiki. For now, I am copying my submission directly, but I will update it with the conversion to NAI version featherlite and the reasoning for why. I speak to it in the main research document._ 

## AID Featherlite Submission

The primary purpose of this is to create a race of friendly and peaceful wolf-like humanoids, with few human physical characteristics. The purpose was also to achieve this in the most accurate way possible.

I have tackled the problem of anthropomorphic wolves a few times, and noted that AID has difficulty understanding how to differentiate a race of very wolf-like people from other common tropes such as werewolves and humans with animal ears/tails. In addition to this, due to the aggressive behaviours normally exhibited by werewolves and other wolf-like humanoids, it is difficult to force the AI to successfully adopt a friendlier demeanor. 

**Breakdown**

`•define wolfkin: Lupinebody muzzleBeastkinThey peaceful tribal`
* `define` appears to rely a bit more on the details in the entry rather than just using `wolfkin`. It is optional. 
* `Lupinebody` is used to ensure that type of `Beastkin` is wolf-like, and that the wolf-like appearance applies to the entire body. In this example `Lupine` would apply to both `body` and `muzzle` as an adjective.
* `muzzle` is used to ensure that the AI understands that the creature in question is not human. Without `muzzle` but keeping the rest the same, the AI often assumes that the creature has a wolf body but a human face, or reverts to the above example of a human with wolf ears and tail.
* `Beastkin` is used to denote a race of anthropomorphic beasts generally--see the main featherlite wiki.
* `They peaceful` is used to override the AI's assumptions that wolf-like beings will be aggressive and warlike. The pronoun also helps lengthen the entry.
* `tribal` is not difficult to define for the AI and needs no additional assistance, and does what is needed.

`•wolfkin behavior: expressivetail&ears They friendlyopen`
* `behavior` after the name of a race was noted to be a strong way of enforcing certain racial quircks like how they express themselves. I found it had that effect as well. 
* `expressivetail&ears` is relatively self-explanatory. If you say something to a wolfkin that induces emotion, the AI will very often note the response of their ears or tail. 
* `They friendlyopen` is used to, again, override the tendency of the AI to denote wolf-like beings as aggressive, and works well in conjunction with `peaceful` above. It is used here to apply as a broad racial behavioural characteristic.

## NAI Featherlite Conversion

_To be completed_
