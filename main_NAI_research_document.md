# Format and Customization Research

<details>
<summary> Contents </summary>

### Table of Contents

- [Format and Customization Research](#format-and-customization-research)
    - [Table of Contents](#table-of-contents)
  - [1. Lorebook Settings](#1-lorebook-settings)
    - [1.1 Priority](#11-priority)
    - [1.2 Insertion](#12-insertion)
  - [2. Format Testing](#2-format-testing)
    - [2.1 Featherlite](#21-featherlite)
      - [**2.1(a) Featherlite Conversion (with examples)**](#21a-featherlite-conversion-with-examples)
      - [**2.1(b) Featherlite Testing**](#21b-featherlite-testing)
    - [2.2 Current To-do for Format Testing](#22-current-to-do-for-format-testing)
      - [**2.2(a) `[ ]` Prose Format**](#22a---prose-format)
      - [**2.2(b) `{ }` Prose Format**](#22b---prose-format)
      - [**2.2(c) Futureman**](#22c-futureman)
      - [**2.2(d) Cat[nip]**](#22d-catnip)
      - [**2.2(e) JSON/Python-like**](#22e-jsonpython-like)
    - [2.3 Miscellaneous](#23-miscellaneous)
  - [3. Story Settings](#3-story-settings)
  - [4. Author's Notes (TBC)](#4-authors-notes-tbc)
    - [4.1 Writing Styles](#41-writing-styles)
    - [4.2 Genres, Themes, Etc.](#42-genres-themes-etc)
    - [4.3 Other Uses](#43-other-uses)
  - [5. Other Testing](#5-other-testing)
    - [5.1 Signposts](#51-signposts)
      - [5.1(a) `***` Signpost](#51a--signpost)
      - [5.1(b) `***` In-Entry Signpost](#51b--in-entry-signpost)
      - [5.1(c) `<<•>>>` Signpost](#51c--signpost)
    - [5.2 "Director" Entries](#52-director-entries)
    - [5.3 Scene Separators](#53-scene-separators)
      - [**5.3(a) Asterix Separator**](#53a-asterix-separator)
      - [**5.3(b) `<|endoftext|>` Separator**](#53b-endoftext-separator)

</details>
<br>

As a former EWI AID user, finding the best formats to inject context and exploring the ability to inject items into specific places in the context are an important part of my NAI user experience. This page contains information I have learned through testing or the work of others. I will try to credit the original discoverer where possible. Please feel free to reach out on Discord (Kalmarr) if you believe credit is misattributed.

Note that my preferred use case is detailed Lorebook Entries injected relatively close to the context. You can shift your use of `Insertion Position` to be similar to your use in EWI. I speak in further detail in the sections below. My use case is generally due to my preference to use non-human characters in my stories. I expect that simpler use cases with fewer unusual characters/attributes will probably behave better and without as much force.

Testing will not always be described in significant detail, e.g. always including percentage of success/failure for certain things. At this stage, my goal is to test general ways of improving output. I will generall try to describe the result in relative terms (clearer, more accurate, more creative, etc.), compared to other settings/entries. 

## 1. Lorebook Settings

The Lorebook has incredibly helpful settings for use in context injection. It is extremely customizable. These are the settings I have found to be the most useful and why. I also address some testing completed.

The primary useful settings to change in Lorebook entries are `Priority` and `Insertion`. The other settings may be referenced in other areas of this guide, or in more detail in the future.

- `Priority` refers to, essentially, the order in which types of context are built in the overall context. The lower the number as an integer (`-700` as an example), the closer to input the priority type is injected into the context. The number is, in essence, completely arbitrary and used as the basis of their relative position to each other.
- `Insertion` is what occurs after the entries are sorted by priority, and refers to how many lines/sentences/tokens (depending on settings chosen) the entries is moved from its position in the context. In the example of an Author's Note set to have `-800` priority ("highest" priority) and `-4` insertion, the AN will be placed 3 new lines from the bottom of the context. A positive insertion value will push the entry down in the context.
  - Positive insertion value remains, to my knowledge, untested. It remains to be seen whether there is potential use for that.

### 1.1 Priority

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

Testing has shown this method to be excellent, both in terms of accuracy and quality of outputs.

I will be working with priority/insertion as part of testing for Featherlite, and may deviate from this system. I will include that information under [Featherlite](#21-featherlite-testing).

_Update (June 24, 2021):_ Changing insertion/priority under featherlite appears to be unnecessary in my use case (non-human non-standard race and characters). These settings appear to be very effective. I am not likely to attempt to test new settings in the near future.

**Older information:**

From NAI:

> Priority Entries are ordered by priority before context is built. Entries with higher priority will reserve and use tokens first. If two entries share the same priority there is no guarantee which will go first.

In the default Advanced Context Menu, the `Priority` for `Story`, `Author's Note`, and `Memory` are:
> **Story:** 0<br/>**Author's Notes:** -400<br/>**Memory:** 800

In practice, this means that `Author's Note` is placed at the front, then `Story`, then `Memory`. With the default `Priority` setting of 400 for Entries, the result puts Entries at the very back just in front of `Memory`. This leads to an especially problematic scenario when the higher tier `2048` tokens of mostly story overwhelms the context.

OPVAM suggested that `Priority` for Lorebook Entries should be set to `0` to avoid placing them in the back of the context with `Memory`. Upon testing, `0` worked. However, there was a side effect. Due to `0` being the same `Priority` as `Story`, I found that sometimes the `Story` and Entries would conflict with where they entered the context. Some generations would put all of the Entries at the very front, literally in front of the output. Others would split an output into two and put them in different parts of the context.

My solution to this problem was to set the `Priority` to **`-200.`** This places the entries essentially where directed by the `Injection` setting, as it sets Entries to a higher priority than `Story` or `Memory`.

### 1.2 Insertion

 `Insertion` setting for entries is similar to usage of `[t=x]` in EWI. Replace `[t=x]` with `-x`. For example, if you used `[t=9]` as a key for something such as `Theme:`, you could make a similar entry in NAI with `Insertion: -9`.

 My recommended insertion settings are above, under OPVAM's general lorebook settings.

From NAI:

> The location the entry will be inserted into the context. 0 is the very top of the context, 1 is one unit down, 2 is two units down etc. Negative numbers will count from the bottom of the context starting with -1 at the very bottom, making -2 one unit up, -3 two units up etc.

Default `Insertion` settings for `Story`, `Author Note`, and `Memory` are as follows:

> - **Story:** -1
> - **Author Note:** -4
> - **Memory:** 0

_To be expanded on later._

## 2. Format Testing

_June 22, 2021 update_: As mentioned below, with `[ ]` instead of `•`, Featherlite appears to work. Further testing is needed, but results have so far been promising.

Format testing so far has shown that use of encapsulation `[ .]` or just `[ ]` appears to work well, and works when combined with caveman. E.g.: `[ Mark age 30 male tall he skilled knight]`.

Monky research in NAI Discord suggests that keeping lines to 20 tokens then separating new lines seems to work well.

- I have confirmed that 20 tokens or less for new lines appears to be preferable for entries. Reinforcing entries with names on each line is important.
- Alternative formatting in the form of JSON/python-like formats may not need this line-splitting method.

### 2.1 Featherlite

Rinter, the creator of Featherlite, has a wiki that can be found here with all the up to date information on the format in NAI: [Rinter's Featherlite Wiki](https://github.com/RinterWaptor/NAI-research/wiki).

Initial testing of Featherlite was not necessary promising, due to leaking issues. However, with `•` swapped for `[ ]`, leaking has been tamped down to a minimum and outputs appear to be of good quality. As I did significant amounts of my research using Featherlite in AID, I intend to spend most of my time studying it and ways it can by used in NAI. Initial research will be contained in this document, but I may draft a separate document in the future should using this one become unweildy.

#### **2.1(a) Featherlite Conversion (with examples)**

Following Rinter's new guidelines for Featherlite in NAI, I converted my entries from AID-version to NAI-version. To show this, I will use an example with a race and character I commonly use. Please see [my document](https://github.com/Kalmarr120/Kalmarr_NAI_Public/blob/755de9ae8c29bb7cc8f33d339edfadf395008893/wolfkin_race_featherlite.md) for details on how I constructed the racial entries for AID.

The conversion primarily deals with replacing `•` as preceding syntax, and replacing it with `[ ]` incapsulation. In addition, terms that do not have a significant relation (unlike, for example, hair and hair colour), are separated. Word smashing is kept for related terms in order to potentially maintain their association.

>_My wolfkin race, in AID Featherlite (`EWIJSON`):_
>
>`•define wolfkin: Lupinebody muzzleBeastkinThey peaceful tribal` \\`[p=5]`<br>
>`•wolfkin behavior: expressivetail&ears They friendlyopen` \\ `[p=5]`
>
>_Converted to NAI Featherlite (`OPVAM race insertion`):_
>
>`[ wolfkin: Lupinebody muzzle Beastkin They peaceful tribal ]`<br>
>`[ wolfkin behavior: expressivetail&ears They friendly open ]`

Applying the principles of new Featherlite, the conversion is minor in this case:

- `•` encapsulation is removed and replaced with `[ ]`.
- `define` is removed. It will need to be tested to determine usefulness in NAI.
  - On principle, it should assist the AI with defining a new term, in this case `wolfkin`. The use case may be different from AID.
- `Lupinebody` remains smashed, as the intention is to describe their bodies/appearance as "lupine."
- `muzzle` is separated from `Beastkin`, as the two terms are not directly related.
- `They` is separated from Beastkin, as it is a generic pronoun.
- `friendly` is separated from `open`. The two terms are not associated.

To use another example, here is a character entry based on that race:

>Mark, a wolfkin character, in AID Featherlite:
>
>`• Mark:30♂︎wolfkin lean Hekind joyful` \\ [p=1]<br>
>`• Mark:Blackfur,White-spot tail,leftearscarHefriendVol` \\ [p=3]
>
> _Converted to NAI Featherlite:_
> `[ Mark: 30 male wolfkin lean He kind joyful]`<br>
> `[ Mark: Blackfur, White-spot tail, leftearscar He friend Vol]`

The conversion in this case should be a bit more of an obvious example of the new principles.

- `•` encapsulation is removed and replaced with `[ ]`.
- `♂︎` is removed, and replaced with `male`. It is unclear if NAI is able to properly understand and use `♂︎` in the context of this format.
- `30`, `male`, and `wolfkin` are broken out into their own words, as they are not associated.
- `kind` is broken off from `He`, as they are not associated.
- `Blackfur` remains smashed in order to maintain their association.
- `leftearscar` is broken off into its own word, as the association is a scar on his left ear.
- `He`, `friend`, and `Vol` are broken into separate words.

#### **2.1(b) Featherlite Testing**

_This section is currently incomplete_.

From initial testing, leaking is rare and outputs are accurate and high quality. There was only one significant leak of the format style in well over a hundred break tests, e.g. `Detailed description of wolfkin: wolfkin are`.

### 2.2 Current To-do for Format Testing

#### **2.2(a) `[ ]` Prose Format**

So far the current preference, with caveman type prose. See above.

#### **2.2(b) `{ }` Prose Format**

Initial testing did not show `{ }` as superior to `[ ]`. Will need to devote further time to review, but unlikely to continue. So far this method of encapsulation appears to have been dropped by serious testers, outside of JSON.

#### **2.2(c) Futureman**

TBC

#### **2.2(d) Cat[nip]**

TBC

#### **2.2(e) JSON/Python-like**

TBC

### 2.3 Miscellaneous

From NAI Server:

>Birb suggests formatting along the lines of `{Alice; age: 25; hair: black; eyes: blue; speech(Alice): Valley girl.}`. Another suggestion is to use `,` with multiple values. _(June 22, 2021: This may be out of date based on recent research)._

Tested Birb's suggested formatting. Some issues with intra-mixing entry information, but no significant leakage outside. Will want to test with different separators. `≡` could be viable. Will also test with `< >` encapsulation, similar to Cat<nip>, e.g. `hair<black& short>`. Results will be described here, if further testing is done on this formatting.

## 3. Story Settings

I am currently using Monky's suggested story settings.

Updated settings based on Monkys suggestions (_June 25, 2021_):

Only changes to default are Tail-Free Sampling set to `0.5`, Top-K Sampling `disabled`. So far seeing success combined with signpost and featherlite formatting. 

## 4. Author's Notes (TBC)

_To be completed_

This section will like not have significant work done on it until some of the other items in this document are properly researched. 

### 4.1 Writing Styles

I have been using the following as a generic writing style:

> `[ WritingStyle: grandiloquent, purple prose]`

Further additions that have shown some use (when added to the above in a list), that are otherwise niche, include:
> - `gay`
>   - This style has assisted with avoiding gender changes in gay-focussed stories. It is unclear if it has any other impact on writing.
> - `furry`
>   - This style seems to bring character's non-human attributes into greater focus. 


### 4.2 Genres, Themes, Etc.

TBC

### 4.3 Other Uses

TBC

## 5. Other Testing

### 5.1 Signposts

#### 5.1(a) `***` Signpost

_June 23/24 2021: Significant testing was done into the use of `***` as a signpost to help break the AI's concentration on the prompt/story while allowing it to focus on the more recent information available to it._

I am recommending signposts, in particular one signpost of `***` at insertion `-5` and priority `-1000`, based on the below. This applies especially if using OPVAM's settings (defined in this document above) and the featherlite format. The principles are likely to apply with other insertion levels and formats, but personal testing may be required to see what positioning will be effective for you.

My testing was first done with default settings and 0.6 randomness, then Monky's settings (now recommended):
> Randomness: `0.8`<br>
> Top-K Sampling: `disabled`<br>
> Nucleus Sampling: `disabled`<br>
> Tail-Free Sampling: `0.5`<br>
> Repitition Penalty: `1.2`<br>
> Repitition Penalty Range: `512`<br>
> Repitition Penalty Slope: `4.05`<br>

At Monky's suggestion, I tested a single `***` signpost at an insertion of `-5`. I chose a priority of `-1000`. After some time testing, I also adjusted the signpost entry to include surrounding newlines:

```

***

```

I tested with a simple break test of `Detailed description of Vol: Vol is`, using a character of mine, in addition to existing activated lorebook entries for another character and for my character race. Everything was tested using featherlite.

The results of the testing were successful. The AI's generations were generally more accurate, more descriptive, related to the race and the other character, and were less repititive/inclusive of too much information from the prompt/story. When references were made to previous story/prompt context, the descriptions were more creative and tended to expand on those reference (e.g. taking `deep emerald eyes` from the prompt and substituting another trait like `kind` or `forest green`). 

Overall, I am pleased with the results and I believe that at least the single one tested can be reasonably recommended. The initial testing is promising and additional testing will be certainly justified.

There are additional items with respect to signposts that I would like to test:

- Using multiple signposts at different insertion points
  - At specific points to separate types of lorebook entries
  - At intervals (e.g. every 4 lines)
- Use during actual play

#### 5.1(b) `***` In-Entry Signpost

Benvolio has mentioned that using `***` within an entry may show some promise, and therefore will be worth testing. The method appears as:
> `[ *** Name: entry information here ]`

I will test this methodology and report the results.

#### 5.1(c) `<<•>>>` Signpost

`<<•>>>` was developed by Monky as a signpost for use with EWIJSON in AI Dungeon. 

Previously, tests using `<<•>>>` as a signpost was unsuccessful. Additional testing of it may be necessary, as there is a possibility that it was merely inserted into the incorrect position at the time.

### 5.2 "Director" Entries

There appears to be some potential benefit with "director" entries, which are short entries telling the AI what to do. These include things like:

```
[ Do: take the book]
```

```
[ Describe in prose]
```

I have not conducted enough research into this to comment on its usefulness at this time. Initial testing shows that `[ Describe in prose]` may have an effect on how the AI outputs information from Lorebook entries.

Some people on NAI Discord report usefulness from this. In particular, the first `[ Do: x]` and similar (`[ Use: x]`, `[ Event: x]`) etc. appear to be able to significantly affect output in a desirable way.

### 5.3 Scene Separators

I have done some research on scene separators, and otherwise have tested other scene separators recommended on the NAI Discord.

#### **5.3(a) Asterix Separator**

Asterix separators for scenes appears to be relatively powerful, especially combined with newlines. In break testing within an NSFW scene, inputting only a newline, `***`, another newline, and `Mark`, I was getting results such as:

```
[Lewd stuff]

***

Mark woke up the next morning feeling refreshed and rested. He felt like he had a new lease on life. It was a perfect start to a wonderful weekend.
```

An issue that may occur with adding newlines is that the AI may output newlines itself in future generations. Play testing will be necessary to see if this impact is too strong to recommend using `***`.

#### **5.3(b) `<|endoftext|>` Separator**

I have performed some testing on the `<|endoftext|>` string that is inputted occasionally into stories, and saw some success. 

I found that, although `<|endoftext|>` was generally successful at separating out scenes, the outputs were shorter, less creative, and less cohesive than the recommended `***`.
