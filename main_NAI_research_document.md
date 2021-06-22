# Format and Customization Research

_Note: going to move this to a research document in the main repository. Will leave wiki for finalized suggestions after this initial research phase is over._

As a former EWI AID user, finding the best formats to inject context and exploring the ability to inject items into specific places in the context are an important part of my NAI user experience. This page contains information I have learned through testing or the work of others.

Note that my preferred use case is detailed Lorebook Entries injected relatively close to the context. You can shift your use of `Insertion Position` to be similar to your use in EWI.

Testing will not always be described in significant detail, e.g. always including percentage of success/failure for certain things. At this stage, my goal is to test general ways of improving output.

## Lorebook Settings

The Lorebook has incredibly helpful settings for use in context injection. It is extremely customizable. These are the settings I have found to be the most useful and why. I also address some testing completed.

### Priority

I have updated my suggestion to use `-200` for `Priority`. Instead, I recommend the following, proposed by OPVAM (and updated June 21):

| Position | Priority | Reserve | Type                                    |
| -------- | -------- | ------- | --------------------------------------- |
| -12      | -100     | 200     | Memory                                  |
| -10      | -200     | 100     | Lore: Concepts                          |
| -10      | -300     | 100     | Lore: Races                             |
| -10      | -400     | 100     | Lore: Places                            |
| -10      | -500     | 100     | Lore: Factions                          |
| -8       | -600     | 200     | Lore: Story Overview (forced active)    |
| -6       | -700     | 100     | Lore: Characters                        |
| -4       | -800     | 200     | Author's Note                           |
| 0        | 0        | 512     | Story                                   |

From OPVAM (_New from June 22, 2021_):
> Pretty much breaking your author's notes into 2 parts.  Story Overview (used to be called Editor's Note) would contain high-level story plot, style, genre, theme etc.. Then you can use your Author's note to steer the story.  For example if you wanted an action story with bits of romance your AN would contain this most of the time [ Writing Style: exciting.  Genre: action] then change it to [ Genre: romance.] or something like that.

**Older information:**

From NAI:

> Priority Entries are ordered by priority before context is built. Entries with higher priority will reserve and use tokens first. If two entries share the same priority there is no guarantee which will go first.

In the default Advanced Context Menu, the `Priority` for `Story`, `Author's Note`, and `Memory` are:
> **Story:** 0<br/>**Author's Notes:** -400<br/>**Memory:** 800

In practice, this means that `Author's Note` is placed at the front, then `Story`, then `Memory`. With the default `Priority` setting of 400 for Entries, the result puts Entries at the very back just in front of `Memory`. This leads to an especially problematic scenario when the higher tier `2048` tokens of mostly story overwhelms the context.

OPVAM suggested that `Priority` for Lorebook Entries should be set to `0` to avoid placing them in the back of the context with `Memory`. Upon testing, `0` worked. However, there was a side effect. Due to `0` being the same `Priority` as `Story`, I found that sometimes the `Story` and Entries would conflict with where they entered the context. Some generations would put all of the Entries at the very front, literally in front of the output. Others would split an output into two and put them in different parts of the context.

My solution to this problem was to set the `Priority` to **`-200.`** This places the entries essentially where directed by the `Injection` setting, as it sets Entries to a higher priority than `Story` or `Memory`.

### Insertion

My current recommended `Insertion` setting for entries is based on usage of `[t=x]` in EWI. Replace `[t=x]` with `-x`. For example, if you used `[t=9]` as a key for something such as `Theme:`, you could make a similar entry in NAI with `Insertion: -9`.

From NAI:

> The location the entry will be inserted into the context. 0 is the very top of the context, 1 is one unit down, 2 is two units down etc. Negative numbers will count from the bottom of the context starting with -1 at the very bottom, making -2 one unit up, -3 two units up etc.
Insertion

Default `Insertion` settings for `Story`, `Author Note`, and `Memory` are as follows:
>**Story:** -1<br/>**Author Note:** -4<br/>**Memory:** 0

Injection of Entries into context is also controlled by `Insertion`. Insertion appears to be similar to EWI. Testing will be needed to see what `Insertion` positions will be helpful given the difference in model. In addition, confirmation of the similarity between EWI's `[t]` and `Insertion` by someone with a more in-depth understanding of EWI will be helpful.

**Will expand on this later.**

## Format Testing

_June 22, 2021 update_: As mentioned below, with `[ ]` instead of `•`, Featherlite appears to work. Further testing is needed, but results have so far been promising.

Format testing so far is showing that use of encapsulation `[ .]` appears to work well, and works when combined with caveman. E.g.: `[ Mark age 30 male tall he skilled knight.]`

Monky research in NAI Discord suggests that keeping lines to 20 tokens then separating new lines seems to work well.
* I have confirmed that 20 tokens or less for new lines appears to be preferable for entries. Reinforcing entries with names on each line is important.

### Current To-do for Format Testing

* **1. `[ ]` Prose Format**

So far the current preference, with caveman type prose. See above.

* **2. `{ }` Prose Format**

Initial testing did not show `{ }` as superior to `[ ]`. Will need to devote further time to review, but unlikely to continue. So far this method of encapsulation appears to have been dropped by serious testers, outside of JSON.

* **3. Featherlite**

*June 22 2021 update*:

Revising previous notes about issues with Featherlite. Featherlite appears to be promising especially with `[ ]` encapsulation rather than `•`. So far, results have been highly accurate, with few leaks. Only one major leak of the format in over 100 tests. There were some leaks between entries--such as replacing once character's eye colour with another.

Earlier testing of Featherlite, specifically using OPVAM's positioning, has seen some success. In 40 generations break testing wolfkin, there were no serious leaks of formatting, and only one compressed word. While the outputs made a little less sense than the alternative caveman formatting, there may be an opportunity for word choice adjustment. Additional testing with alternative words will be needed.

* **4. Futureman**

TBC

* **5. Cat[nip]**

TBC

* **6. JSON/Python-like**

TBC

### Miscellaneous

From NAI Server:

>Birb suggests formatting along the lines of `{Alice; age: 25; hair: black; eyes: blue; speech(Alice): Valley girl.}`. Another suggestion is to use `,` with multiple values. _(June 22, 2021: This may be out of date based on recent research)._

Tested Birb's suggested formatting. Some issues with intra-mixing entry information, but no significant leakage outside. Will want to test with different separators. `≡` could be viable. Will also test with `< >` encapsulation, similar to Cat<nip>, e.g. `hair<black& short>`. Results will be described here.

## Story Settings

From Monky (NAID):

>For 2.7b/Calliope, top k of 45 and nucleus sampling of 0.875 seem to be the strongest tweaks for consistency from WI without delving into uncreative/not looping. Haven't been able to nail down how many tokens Calliope can sustain for yet.

Additional information will need to be added here. Currently, I am using Jarel's generation settings (available on NAI discord).

## Other Testing

### Signposts

Testing injection of signposts, `<<•>>>>`, in various places in the context.

During attempted break testing and play testing, I have not seen a noticeable effect from using signposts. Of interest, the AI seems to at least partially be aware of them as story breakers. `<<•>>>>` leaked relatively frequently, but when it did it was almost universally placed at a point breaking the story into a new section.

Research on signposts will be held until I am able to fully understand the effect of the available settings on output.

### "Director" Entries

There appears to be some potential benefit with "director" entries, which are short entries telling the AI what to do. These include things like:

```
[ Do: take the book]
```

```
[ Describe in prose]
```

I have not conducted enough research into this to comment on its usefulness at this time. Some people on NAI discord report usefulness from this.
